from fastapi import APIRouter,Depends
import os 
from helpers.main_config.config import get_settings , Settings

base_router = APIRouter(
    prefix = '/api/v1',
    tags = ['api_v1']
)

@base_router.get('/')
def welcome_message():
    return {"message": "Hello world!"}

@base_router.get('/name')
def app_name(app_settings: Settings = Depends(get_settings)):
    app_name = app_settings.APP_NAME
    return{"message": f"{app_name}"}