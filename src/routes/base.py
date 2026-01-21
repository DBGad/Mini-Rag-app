from fastapi import APIRouter
import os 

base_router = APIRouter(
    prefix = '/api/v1',
    tags = ['api_v1']
)

@base_router.get('/')
def welcome_message():
    return {"message": "Hello world!"}

@base_router.get('/name')
def app_name():
    return{"message": f"{os.getenv('APP_NAME')}"}