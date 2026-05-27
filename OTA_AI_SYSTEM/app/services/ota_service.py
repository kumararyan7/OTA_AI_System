import time
import random
from app.database import SessionLocal
from app.models import UpdateStatus, Logs


def log_event(db, device_id, message):
    log = Logs(device_id=device_id, message=message)
    db.add(log)
    db.commit()


def process_update(device_id: str):
    db = SessionLocal()

    # ✅ Correct stages
    stages = ["Pending", "Downloading", "Installing"]

    # 🔄 Loop through stages
    for stage in stages:
        update = UpdateStatus(device_id=device_id, status=stage)
        db.merge(update)
        db.commit()

        log_event(db, device_id, f"{stage} started")
        time.sleep(1)

    # ✅ Final stage (OUTSIDE loop)
    final_status = random.choice(["Success", "Failed"])

    update = UpdateStatus(device_id=device_id, status=final_status)
    db.merge(update)

    log_event(db, device_id, f"Update {final_status}")

    db.commit()
    db.close()

    return final_status


# ✅ REQUIRED FUNCTION (you were missing this)
def get_device_status(device_id: str):
    db = SessionLocal()

    update = db.query(UpdateStatus).filter(UpdateStatus.device_id == device_id).first()

    db.close()

    if update:
        return update.status
    return "Not Found"


def retry_update(device_id: str):
    return process_update(device_id)