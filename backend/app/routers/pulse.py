from fastapi import APIRouter
from app.database import SessionLocal
from app.models.pulse import PulseDB
from pydantic import BaseModel


class Pulse(BaseModel):
    value: int
    service: str
    status: str


router = APIRouter()

# -------------------
# POST /pulse
# -------------------


@router.post("/pulse")
def create_pulse(pulse: Pulse):
    db = SessionLocal()
    try:

        # 🔥 AÑADE ESTO
        if pulse.value > 100:
            pulse.status = "critical"

        new_pulse = PulseDB(
            value=pulse.value,
            service=pulse.service,
            status=pulse.status
        )

        db.add(new_pulse)
        db.commit()
        db.refresh(new_pulse)

        return {
            "message": "Pulse saved",
            "data": {
                "id": new_pulse.id,
                "value": new_pulse.value,
                "service": new_pulse.service,
                "status": new_pulse.status
            }
        }

    finally:
        db.close()


# -------------------
# GET /pulse
# -------------------
@router.get("/pulse")
def get_pulses():
    db = SessionLocal()
    try:
        pulses = db.query(PulseDB).all()

        return {
            "pulses": [
                {
                    "id": p.id,
                    "value": p.value,
                    "service": p.service,
                    "status": p.status
                }
                for p in pulses
            ]
        }

    finally:
        db.close()
