import datetime

from sqlalchemy import Column, DateTime, Integer

from app.factories.database import get_db

DB = get_db()


class BaseModel(DB.Model):
    __abstract__ = True

    last_modified = Column(DateTime, onupdate=datetime.datetime.utcnow, default=datetime.datetime.utcnow)
    id = Column(Integer, primary_key=True, autoincrement=True)
