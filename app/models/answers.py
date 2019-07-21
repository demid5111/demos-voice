from sqlalchemy import Column, Integer, ForeignKey, String, Float

from app.models.base import BaseModel


class TblAnswers(BaseModel):
    __tablename__ = 'answers'

    discussion_id = Column(Integer, ForeignKey('discussions.id'))
    text = Column(String, nullable=True)
    likes = Column(Integer, nullable=True)
    rate = Column(Float, nullable=True)

    def json(self):
        return {
            'text': self.text,
            'likes': self.likes,
            'rate': self.rate,
        }
