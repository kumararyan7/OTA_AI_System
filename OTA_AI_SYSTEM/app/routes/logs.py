from fastapi import APIRouter
from app.database import SessionLocal
from app.models import Logs

router = APIRouter()

@router.get("/logs/{device_id}")
def get_logs(device_id:str):
    db = SessionLocal()

    logs = db.query(Logs).filter(Logs.device_id== device_id).all()

    db.close()

    return {"logs": [log.message for log in logs]}
