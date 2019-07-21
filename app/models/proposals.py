import datetime

from sqlalchemy import Column, Integer, Float, ForeignKey, String, DateTime, Text

from app.models.base import BaseModel
from app.models.comments import TblComments
from app.models.discussions import TblDiscussions


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
        discussion = TblDiscussions.query.filter_by(proposal_id=self.id).first()
        comments = TblComments.query.filter_by(discussion_id=discussion.id).all()

        comments_spam = sum([1 if c.is_spam else 0 for c in comments])
        comments_likes = sum([c.likes if c.likes else 0 for c in comments])

        try:
            mean_polarity = sum([c.polarity for c in comments])/len(comments)
        except (TypeError, ZeroDivisionError):
            mean_polarity = None

        try:
            sum_positive = sum([c.positive for c in comments])/3
        except TypeError:
            sum_positive = None

        try:
            sum_negative = sum([c.negative for c in comments])/3
        except TypeError:
            sum_negative = None

        try:
            sum_neutral = sum([c.neutral for c in comments])/3
        except TypeError:
            sum_neutral = None

        return {
            'id': self.id,
            'county_id': self.county_id,
            'subject': self.subject,
            'name': self.name,
            'content': self.content,
            'creationTime': self.creation_time,
            'longitude': self.longitude,
            'latitude': self.latitude,
            'meanPolarity': mean_polarity,
            'sumPositive': sum_positive,
            'sumNegative': sum_negative,
            'sumNeutral': sum_neutral,
            'likes': discussion.likes,
            'numComments': len(comments),
            'commentsLikes': comments_likes,
            'spamComments': comments_spam,
            'url': discussion.url
        }
