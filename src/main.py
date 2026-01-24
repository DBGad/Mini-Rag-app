from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv()
from routes import base,Data
from motor.motor_asyncio import AsyncIOMotorClient
from helpers.main_config.config import get_settings
from stores.llm.LLMProviderFactory import LLMProviderFactory

app = FastAPI()

@app.on_event("startup")
async def startup_db_client():
    settings = get_settings()
    app.mongo_conn = AsyncIOMotorClient(settings.MONGODB_URL)
    app.db_client = app.mongo_conn[settings.MONGODB_DATABASE]

    LLM_Provider_Factory = LLMProviderFactory(settings)
    
    app.generation_client = LLM_Provider_Factory.create(settings.GENERATION_BACKEND)
    app.generation_client.set_generation_model(settings.GENERATION_MODEL_ID)

    
    app.embedding_client = LLM_Provider_Factory.create(settings.EMBEDDING_BACKEND)
    app.embedding_client.set_embedding_model(settings.EMBEDDING_MODEL_ID,settings.EMBEDDING_MODEL_SIZE)
    
@app.on_event("shutdown")
async def shutdown_db_client():
    app.mongo_conn.close()


app.include_router(base.base_router)
app.include_router(Data.data_router)