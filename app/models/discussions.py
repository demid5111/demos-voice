import datetime

from sqlalchemy import Column, Integer, ForeignKey, String, DateTime

from app.models.base import BaseModel


class TblDiscussions(BaseModel):
    __tablename__ = 'discussions'

    proposal_id = Column(Integer, ForeignKey('proposals.id'))
    type = Column(String, nullable=True)
    likes = Column(Integer, nullable=True, default=0)
    start_time = Column(DateTime, onupdate=datetime.datetime.utcnow, default=datetime.datetime.utcnow, nullable=True)
    end_time = Column(DateTime, onupdate=datetime.datetime.utcnow, default=datetime.datetime.utcnow, nullable=True)
    poll_question = Column(String, nullable=True)
    poll_likes = Column(Integer, nullable=True, default=0)
    url = Column(String, nullable=True)
