from fastapi import APIRouter
from app.database import SessionLocal
from app.models.alert import AlertDB

router = APIRouter()


@router.get("/alerts")
def get_alerts():
    db = SessionLocal()
    try:
        alerts = db.query(AlertDB).all()

        return {
            "alerts": [
                {
                    "id": a.id,
                    "message": a.message,
                    "service": a.service,
                    "level": a.level
                }
                for a in alerts
            ]
        }

    finally:
        db.close()
