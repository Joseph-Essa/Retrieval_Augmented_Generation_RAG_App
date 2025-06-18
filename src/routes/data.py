from fastapi import FastAPI ,APIRouter ,Depends , UploadFile , status , Request
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
import os
from helpers.config import get_settings , Settings
from controllers import DataController ,ProjectController , ProcessController
import aiofiles
from models import ResponseSignal
import logging
from .schemes.data import ProcessRequest
from models.enums.AssetTypeEnum import AssetTypeEnum
from services.db_factory import DatabaseModelFactory 

logger = logging.getLogger('uvicorn.error')


data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api_v1","data"] 
)

@data_router.post("/upload/{database_type}/{project_id}")

async def upload_data(request : Request ,  project_id : int, database_type : str , file : UploadFile , 
                        app_settings: Settings = Depends(get_settings) ):
    
    project_model, asset_model, chunk_model, DataChunk ,Asset = await DatabaseModelFactory.get_models(database_type, request)
    project = await project_model.get_project_or_create_one(project_id=project_id)

    #val file properties 
    data_controller = DataController()
    is_valid , result_signal = data_controller.validate_uploaded_file(file=file)

    if not is_valid:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content = {
                "signal" : result_signal
            }
        )

    project_dir_path = ProjectController().get_project_path(project_id=project_id)

    file_path , file_id = data_controller.generate_unique_filepath(orig_file_name = file.filename , project_id=project_id)

    try :
        async with aiofiles.open(file_path , 'wb') as f:
            while chunk := await file.read(app_settings.FILE_DEFAULT_CHUNK_SIZE):
                await f.write(chunk)
    except Exception as e:

        logger.error(f"Error while uploading file {e}")

        return JSONResponse(
        content = {
            "signal" : ResponseSignal.FILE_UPLOAD_FAILED.value ,
        }
        )

    #store asset to db 

    asset_resource = Asset(
        asset_project_id = project.id,
        asset_type = AssetTypeEnum.FILE.value , 
        asset_name = file_id ,
        asset_size = os.path.getsize(file_path) 
                            )
    
    asset_record = await asset_model.create_asset(asset=asset_resource)
    
    return JSONResponse(
        content = {
            "signal" : ResponseSignal.FILE_UPLOAD_SUCCESS.value ,
            "file_id" : str(asset_record.id),
        }
    )
    

@data_router.post("/process/{database_type}/{project_id}")

async def process_endpoint(request: Request,project_id: int,database_type: str,
                            process_request: ProcessRequest):
    chunk_size = process_request.chunk_size
    overlap_size = process_request.overlap_size
    do_reset = process_request.do_reset

    project_model, asset_model, chunk_model, DataChunk, Asset = await DatabaseModelFactory.get_models(database_type, request)
    project = await project_model.get_project_or_create_one(project_id=project_id)

    project_files_ids = {}

    if process_request.file_id:
        asset_record = await asset_model.get_asset_record(
            asset_project_id=project.id,
            asset_name=process_request.file_id
        )

        if asset_record is None:
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={"signal": ResponseSignal.FILE_ID_ERROR.value}
            )

        project_files_ids = {asset_record.id: asset_record}
    else:
        project_files = await asset_model.get_all_project_assets(
            asset_project_id=project.id,
            asset_type=AssetTypeEnum.FILE.value
        )
        project_files_ids = {
            record.id: record for record in project_files
        }

    if len(project_files_ids) == 0:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"signal": ResponseSignal.NO_FILES_ERROR.value}
        )

    process_controller = ProcessController(project_id=project_id)

    no_records = 0
    no_files = 0

    if do_reset == 1:
        _ = await chunk_model.delete_chunks_by_project_id(project_id=project.id)
        for asset in project_files_ids.values():
            await asset_model.mark_as_processed(asset.id, False)

    for asset_id, asset in project_files_ids.items():
        if asset.is_processed:
            logger.info(f"Skipping already processed asset: {asset.asset_name}")
            continue

        file_content = process_controller.get_file_content(file_id=asset.asset_name)
        if file_content is None:
            logger.error(f"Error while processing file: {asset.asset_name}")
            continue

        file_chunks = process_controller.process_file_content(
            file_content=file_content,
            file_id=asset.asset_name,
            chunk_size=chunk_size,
            overlap_size=overlap_size
        )
        if not file_chunks:
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={"signal": ResponseSignal.PROCESSING_FAILED.value}
            )

        file_chunks_records = [
            DataChunk(
                chunk_text=chunk.page_content,
                chunk_metadata=chunk.metadata,
                chunk_order=i + 1,
                chunk_project_id=project.id,
                chunk_asset_id=asset_id
            )
            for i, chunk in enumerate(file_chunks)
        ]

        no_records += await chunk_model.insert_many_chunks(chunks=file_chunks_records)
        await asset_model.mark_as_processed(asset_id)
        no_files += 1

    return JSONResponse(
        content={
            "signal": ResponseSignal.PROCESSING_SUCCESS.value,
            "inserted_chunks": no_records,
            "processed_files": no_files
        }
    )