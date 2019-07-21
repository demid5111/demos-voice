import datetime

from sqlalchemy import Column, Integer, ForeignKey, String, DateTime, Float

from app.models.base import BaseModel


class TblComments(BaseModel):
    __tablename__ = 'comments'

    discussion_id = Column(Integer, ForeignKey('discussions.id'))
    text = Column(String, nullable=True)
    likes = Column(Integer, nullable=True)
    start_time = Column(DateTime, onupdate=datetime.datetime.utcnow, default=datetime.datetime.utcnow)
    end_time = Column(DateTime, onupdate=datetime.datetime.utcnow, default=datetime.datetime.utcnow)
    polarity = Column(Float, nullable=True)
    confidence = Column(Float, nullable=True)
    positive = Column(Float, nullable=True)
    neutral = Column(Float, nullable=True)
    negative = Column(Float, nullable=True)
