from sqlalchemy import Column, Integer, Text, DateTime
from app.database.db import Base
from sqlalchemy.sql import func

class LogTable(Base):

    __tablename__ = "logs"

    id = Column(Integer,primary_key=True, index=True)
    raw_log = Column(Text, nullable=False)
    summary = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

