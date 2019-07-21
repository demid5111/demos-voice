from app.core.sentiment_analysis import analyze_sentiments
from app.factories.database import get_db
from app.models.answers import TblAnswers
from app.models.comments import TblComments
from app.models.counties import TblCounties
from app.models.discussions import TblDiscussions
from app.models.proposals import TblProposals
from app.models.regions import TblRegions


def write_record(record, session):
    session.add(record)
    session.commit()


def fill_database():
    region1 = TblRegions()
    region1.name = 'Chuvashia'
    region1.region_id = 1
    write_record(region1, get_db().session)

    county1 = TblCounties()
    county1.name = 'Cheboksary'
    county1.region_id = 1
    write_record(county1, get_db().session)

    proposal1 = TblProposals()
    proposal1.name = 'Ustanovka mosta'
    proposal1.region_id = 1
    write_record(proposal1, get_db().session)

    discussion1 = TblDiscussions()
    discussion1.type = 'VK'
    discussion1.proposal_id = 1
    write_record(discussion1, get_db().session)

    comment1 = TblComments()
    comment1.text = 'want to build it'
    comment1.discussion_id = 1
    write_record(comment1, get_db().session)

    answer1 = TblAnswers()
    answer1.text = 'option 1'
    answer1.rate = 100
    write_record(comment1, get_db().session)

    answer2 = TblAnswers()
    answer2.text = 'option 2'
    answer2.rate = 100
    write_record(comment1, get_db().session)


def fill_sentiments(proposal_id):
    proposal = TblProposals.query.get(proposal_id)
    discussion = TblDiscussions.query.filter_by(proposal_id=proposal.id).first()
    comments = TblComments.query.filter_by(discussion_id=discussion.id).all()
    for c in comments:
        res = analyze_sentiments(c.text)
        c.polarity = res['polarity']
        c.confidence = res['confidence']
        c.positive = res['positive']
        c.neutral = res['neutral']
        c.negative = res['negative']
        write_record(c, get_db().session)
