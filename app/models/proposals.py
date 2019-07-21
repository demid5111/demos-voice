import datetime

from sqlalchemy import Column, Integer, Float, ForeignKey, String, DateTime, Text

from app.models.base import BaseModel


class TblProposals(BaseModel):
    __tablename__ = 'proposals'

    county_id = Column(Integer, ForeignKey('counties.id'))
    subject = Column(String, nullable=True)
    name = Column(String, nullable=True)
    content = Column(Text, nullable=True)
    creation_time = Column(DateTime, onupdate=datetime.datetime.utcnow, default=datetime.datetime.utcnow)
    longitude = Column(Float, nullable=True)
    latitude = Column(Float, nullable=True)

    def json(self):
        return {
            'id': self.id,
            'county_id': self.county_id,
            'subject': self.subject,
            'name': self.name,
            'content': self.content,
            'creationTime': self.creation_time,
            'longitude': self.longitude,
            'latitude': self.latitude,
        }
