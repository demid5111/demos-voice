import datetime

from sqlalchemy import Column, Integer, ForeignKey, String, DateTime

from app.models.base import BaseModel


class TblDiscussions(BaseModel):
    __tablename__ = 'discussions'

    proposal_id = Column(Integer, ForeignKey('proposals.id'), primary_key=True)
    type = Column(String, nullable=True)
    likes = Column(Integer, nullable=True)
    start_time = Column(DateTime, onupdate=datetime.datetime.utcnow, default=datetime.datetime.utcnow)
    end_time = Column(DateTime, onupdate=datetime.datetime.utcnow, default=datetime.datetime.utcnow)
