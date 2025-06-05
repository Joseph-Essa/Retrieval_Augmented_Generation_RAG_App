from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv(".env")
from routes import base ,data
from motor.motor_asyncio import AsyncIOMotorClient
from helpers.config import get_settings
from stores.llm.LLMProviderFactory import LLMProviderFactory


app = FastAPI()

# @app.on_event("startup")
async def startup_db_client():
    setting = get_settings()
    app.mongo_conn = AsyncIOMotorClient(setting.MONGODB_URL)
    app.db_client = app.mongo_conn[setting.MONGODB_DATABASE]
    llm_provider_factory = LLMProviderFactory(setting)
    
    # generation client
    app.generation_client = llm_provider_factory.create(provider=setting.GENERATION_BACKEND)
    app.generation_client.set_generation_model(model_id=setting.GENERATION_MODEL_ID)
    
    # embedding client
    app.embedding_client = llm_provider_factory.create(provider=setting.EMBEDDING_BACKEND)
    app.embedding_client.set_embedding_model(model_id=setting.EMBEDDING_MODEL_ID ,
                                             model_size=setting.EMBEDDING_MODEL_SIZE)
    

# @app.on_event("shutdown")
async def shutdown_db_client():
    app.mongo_conn.close()


app.router.lifespam.on_startup.append(startup_db_client)
app.router.lifespam.on_shutdown.append(shutdown_db_client)

app.include_router(base.base_router)
app.include_router(data.data_router)

