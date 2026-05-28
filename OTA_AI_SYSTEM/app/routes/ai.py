from fastapi import APIRouter
from app.database import SessionLocal
from app.models import Logs
from app.services import ai_service

router = APIRouter()

@router.get("/analyze/{device_id}")
def analyze_device(device_id: str):
    db = SessionLocal()

    logs = db.query(Logs).filter(Logs.device_id == device_id).all()
    log_messages = [log.message for log in logs]

    db.close()

    analysis = ai_service.analyze_logs(log_messages)

    return {
        "device_id": device_id,
        "analysis": analysis
    }
