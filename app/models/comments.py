import datetime

from sqlalchemy import Column, Integer, ForeignKey, String, DateTime

from app.models.base import BaseModel


class TblComments(BaseModel):
    __tablename__ = 'comments'

    discussion_id = Column(Integer, ForeignKey('discussions.id'), primary_key=True)
    type = Column(String, nullable=True)
    likes = Column(Integer, nullable=True)
    start_time = Column(DateTime, onupdate=datetime.datetime.utcnow, default=datetime.datetime.utcnow)
    end_time = Column(DateTime, onupdate=datetime.datetime.utcnow, default=datetime.datetime.utcnow)
