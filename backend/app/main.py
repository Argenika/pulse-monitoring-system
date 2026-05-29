import threading
import time
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers.health import router as health_router
from app.routers.pulse import router as pulse_router
from app.routers.alert import router as alert_router

from app.database import engine, Base, SessionLocal
from app.models.pulse import PulseDB
from app.models.alert import AlertDB
from app.services.fetch_data import fetch_satellite_data

app = FastAPI()

# ✅ CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Crear tablas
Base.metadata.create_all(bind=engine)

# ✅ Routers
app.include_router(health_router)
app.include_router(pulse_router)
app.include_router(alert_router)

# ✅ Logs en memoria
logs = []

# ---------------------------
# 🔁 BACKGROUND PROCESS
# ---------------------------


def background_fetch():
    while True:
        db = SessionLocal()
        try:
            # 1. FETCH
            data = fetch_satellite_data()
            logs.append(f"📡 Fetch: velocity={data['value']}")

            # 2. STORE
            new_pulse = PulseDB(
                value=data["value"],
                service=data["service"],
                status=data["status"]
            )
            db.add(new_pulse)
            logs.append("💾 Pulse guardado en DB")

            # 3. ALERT LOGIC
            if data["value"] > 20000:
                alert = AlertDB(
                    message="High velocity detected",
                    service=data["service"],
                    level="critical"
                )
                db.add(alert)
                logs.append("🚨 ALERT GENERATED")

            db.commit()

        finally:
            db.close()

        time.sleep(10)

# ---------------------------
# 📡 LOGS ENDPOINT
# ---------------------------


@app.get("/logs")
def get_logs():
    return {"logs": logs[-20:]}


# ---------------------------
# 🚀 START THREAD
# ---------------------------
threading.Thread(target=background_fetch, daemon=True).start()
