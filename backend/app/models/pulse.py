from sqlalchemy import Column, Integer, String
from app.database import Base
from sqlalchemy import DateTime
from datetime import datetime


class PulseDB(Base):
    __tablename__ = "pulses"

    id = Column(Integer, primary_key=True, index=True)
    value = Column(Integer)
    service = Column(String)
    status = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
