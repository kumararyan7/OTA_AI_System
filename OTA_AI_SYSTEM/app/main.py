#(run): uvicorn app.main:app --reload

from fastapi import FastAPI
from app.routes import device,update,logs
# from app.routes.device import router
from app.database import engine, Base
from app import models

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(device.router)
app.include_router(update.router)
app.include_router(logs.router)


@app.get("/")
def home():
    return {"message": "OTA AI System Running"}