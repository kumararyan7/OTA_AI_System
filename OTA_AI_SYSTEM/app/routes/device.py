from fastapi import APIRouter

print("Creating router...")

router = APIRouter()

print("Router created:", router)

devices = []

@router.post("/register-device")
def register_device(device_id: str):
    devices.append(device_id)
    return {"message": f"Device {device_id} registered"}

@router.get("/devices")
def get_devices():
    return {"devices": devices}