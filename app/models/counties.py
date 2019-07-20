from sqlalchemy import Column, Integer, ForeignKey

from app.models.regions import TblRegions


class TblCounties(TblRegions):
    __tablename__ = 'counties'

    region_id = Column(Integer, ForeignKey('regions.id'), primary_key=True)
