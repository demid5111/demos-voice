from sqlalchemy import Column, Integer, ForeignKey, String, Float

from app.models.base import BaseModel


class TblCounties(BaseModel):
    __tablename__ = 'counties'

    region_id = Column(Integer, ForeignKey('regions.id'))
    name = Column(String, nullable=True)
    longitude = Column(Float, nullable=True)
    latitude = Column(Float, nullable=True)
