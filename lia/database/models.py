from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func
from .db import Base

class Conversation(Base):
    __tablename__ = 'conversations'
    id = Column(Integer, primary_key=True)
    question = Column(Text)
    answer = Column(Text)
    timestamp = Column(DateTime, server_default=func.now())
