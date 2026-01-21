from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv()
from routes import base,Data

app = FastAPI()


app.include_router(base.base_router)
app.include_router(Data.data_router)