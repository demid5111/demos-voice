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

    discussion1 = TblProposals()
    discussion1.name = 'Ustanovka mosta'
    discussion1.region_id = 1
    write_record(county1, get_db().session)

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
