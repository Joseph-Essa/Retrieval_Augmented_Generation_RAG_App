from typing import Tuple
from fastapi import Request

from models.db_schemes.ragapp_mongodb import (
    ProjectModel as MongoProjectModel,
    ChunkModel as MongoChunkModel,
    AssetModel as MongoAssetModel,
)
from models.db_schemes.ragapp_mongodb.schemes import (
    Asset as MongoAsset,
    DataChunk as MongoDataChunk
)

from models.db_schemes.ragapp_postgresdb import (
    ProjectModel as PgProjectModel,
    ChunkModel as PgChunkModel,
    AssetModel as PgAssetModel,
)
from models.db_schemes.ragapp_postgresdb.schemes import(
    Asset as PgAsset,
    DataChunk as PgDataChunk
)


class DatabaseModelFactory:
    @staticmethod
    async def get_models(database_type: str, request: Request) -> Tuple:
        if database_type == "mongodb":
            db_client = request.app.db_client
            ProjectModelCls, ChunkModelCls, AssetModelCls = MongoProjectModel, MongoChunkModel, MongoAssetModel
            DataChunkCls = MongoDataChunk
            AssetCls = MongoAsset

        elif database_type == "postgres":
            db_client = request.app.main_db_client
            ProjectModelCls, ChunkModelCls, AssetModelCls = PgProjectModel, PgChunkModel, PgAssetModel
            DataChunkCls = PgDataChunk
            AssetCls = PgAsset

        else:
            raise ValueError(f"Unsupported database type: {database_type}")

        project_model = await ProjectModelCls.create_instance(db_client)
        asset_model = await AssetModelCls.create_instance(db_client)
        chunk_model = await ChunkModelCls.create_instance(db_client)

        return project_model, asset_model, chunk_model, DataChunkCls ,AssetCls
