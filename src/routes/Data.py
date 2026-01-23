from fastapi import APIRouter, UploadFile, Depends,status,Request,File
from fastapi.responses import JSONResponse
import os 
import sys
from helpers.main_config.config import get_settings, Settings
from controllers import DataController,ProjectController,ProcessController  
import aiofiles
from models import ResponseSignal
import logging
from models.ProjectDataModel import ProjectDataModel
from models.ChunkDataModel import ChunkDataModle

from .schemes.Data import ProcessRequest
from models.db_schemes.data_chunk import DataChunk

logger = logging.getLogger('uvicorn.error')


data_router = APIRouter(
    prefix='/api/v1/data',
    tags=['api_v1', 'data']
)

@data_router.post('/upload/{project_id}')
async def upload_data(request:Request,
    project_id: str,
    file: UploadFile =File(...) ,
    app_settings: Settings = Depends(get_settings)
):
    project_data_model =await ProjectDataModel.create_instance(request.app.db_client)
    project = await project_data_model.get_project_or_create_one(
        project_id=project_id
    )

    data_obj =DataController()
    is_valid,signal = data_obj.validate_uploaded_file(file=file)
    
    if not is_valid:
        return JSONResponse(
            status_code = status.HTTP_400_BAD_REQUEST,
            content = {
                "signal" : signal
            }
        )
    project_dir_path = ProjectController().get_project_path(project_id)
    file_path,file_id = data_obj.generate_unique_filepath(file.filename,project_id)
    try:    
        async with aiofiles.open(file_path,'wb') as f:
            while chunk := await file.read(app_settings.FILE_DEFAULT_CHUNK_SIZE):
                await f.write(chunk)
    except Exception as e:
        logger.error(f"Error while uploading file: {e}")
        return JSONResponse(
            status_code = status.HTTP_400_BAD_REQUEST,
            content = {
                "signal" : ResponseSignal.FILE_UPLOAD_FAILED.value
            }
        )

    return JSONResponse(
        content = {
            "signal": ResponseSignal.FILE_UPLOAD_SUCCESS.value,
            "file_id" : file_id
            }
    )

@data_router.post('/process/{project_id}')
async def process_file(request:Request,project_id:str,Process_Request:ProcessRequest):

    file_id = Process_Request.file_id
    chunk_size = Process_Request.chunk_size
    overlap_size = Process_Request.overlap_size
    do_reset = Process_Request.do_reset

    project_data_model =await ProjectDataModel.create_instance(request.app.db_client)

    project = await project_data_model.get_project_or_create_one(
        project_id=project_id
    )
    
    chunk_model =await ChunkDataModle.create_instance(db_client= request.app.db_client)


   
    process_obj = ProcessController(project_id)
    file_content = process_obj.get_file_content(file_id)
    file_chunks = process_obj.process_file_content(file_content=file_content,file_id=file_id,
                                                   chunk_size=chunk_size,overlap_size=overlap_size)
    chunks = [{
            "metadata": chunk.metadata,
            "page_content": chunk.page_content,
            "type": chunk.type
        } for chunk in file_chunks]
    
    
    if file_chunks is None  or len(chunks) == 0:
        return JSONResponse(
            status_code = status.HTTP_400_BAD_REQUEST,
            content = {"signal" : ResponseSignal.PROCESSING_FAILED.value}
        )
    

    chunks_records = [
        DataChunk(
            chunk_text= chunk.page_content,
            chunk_metadata=chunk.metadata,
            chunk_order = i+1,
            chunk_project_id = project.id,
        )
        
        for i,chunk in enumerate (file_chunks)
    ]
    if do_reset == 1 :
        _= await chunk_model.delete_chunks_by_project_id(project_id=project.id)

    no_rec = await chunk_model.insert_many_chunks(chunks_records)
    return JSONResponse(
        content = {
            "signal" : ResponseSignal.PROCESSING_SUCCESS.value,
            "inserted_chunks" : no_rec
        }
    )