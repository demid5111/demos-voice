from sqlalchemy import Column, Integer, String, Float

from app.models.base import BaseModel


class TblRegions(BaseModel):
    __tablename__ = 'regions'

    name = Column(String, nullable=True)
    longitude = Column(Float, nullable=True)
    latitude = Column(Float, nullable=True)
