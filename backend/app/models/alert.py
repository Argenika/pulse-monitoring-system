from sqlalchemy import Column, Integer, String
from app.database import Base


class AlertDB(Base):
    __tablename__ = "alerts"

    id = Column(Integer, primary_key=True, index=True)
    message = Column(String)
    service = Column(String)
    level = Column(String)
