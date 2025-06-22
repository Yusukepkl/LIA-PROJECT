from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
import os

Base = declarative_base()
DATABASE_URL = os.getenv('LIA_DB', 'sqlite:///lia.db')
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)


class History(Base):
    __tablename__ = 'history'
    id = Column(Integer, primary_key=True)
    question = Column(String)
    answer = Column(String)


def init_db():
    Base.metadata.create_all(bind=engine)
