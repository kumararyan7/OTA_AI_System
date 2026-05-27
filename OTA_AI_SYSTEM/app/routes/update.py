from fastapi import APIRouter
# from app.services import ota_service
from app.services.ota_service import process_update, get_device_status
from app.services import ota_service
router = APIRouter()

device_status={}

@router.post("/send-update")
def send_update(device_id: str):
    status = process_update(device_id)
    return{"device_id": device_id,"status":status}

@router.get("/status/{device_id}")
def get_status(device_id:str):
    status = get_device_status(device_id)
    return{"device_id": device_id,"status":status}

@router.post("/retry-update")
def retry_update(device_id : str):
    status = ota_service.retry_update(device_id)
    return {"device_id": device_id,"status":status}
