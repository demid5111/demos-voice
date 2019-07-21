from app import app
from flask import jsonify, render_template, request

from app.core.parsers.vk import VKParser
from app.factories.database import get_db
from app.models.answers import TblAnswers
from app.models.comments import TblComments
from app.models.discussions import TblDiscussions
from app.models.proposals import TblProposals
from app.models.regions import TblRegions
from app.utils import write_record


@app.route('/')
def home():
    return app.send_static_file('index.html')


@app.route('/new', methods=['POST', 'GET'])
def import_from_post():
    # data = request.get_json()
    data = {
        'socialNetwork': 'vk',
        'fromUrl': 'https://vk.com/moneysecrets?w=wall-184648030_2',
    }
    net = data['socialNetwork']
    if net != 'vk':
        raise NotImplementedError

    parser = VKParser()
    post = parser.parse(data['fromUrl'])

    proposal = TblProposals()
    proposal.name = post.title
    proposal.content = post.text
    proposal.county_id = 1
    proposal.subject = 'ЖКХ'
    write_record(proposal, get_db().session)

    discussion = TblDiscussions()
    discussion.type = 'VK'
    discussion.proposal_id = proposal.id
    discussion.likes = post.likes
    discussion.poll_likes = post.poll.votes
    discussion.poll_question = post.poll.question
    write_record(discussion, get_db().session)

    for c in post.comments:
        comment = TblComments()
        comment.text = c.text
        comment.discussion_id = discussion.id
        comment.likes = c.likes
        write_record(comment, get_db().session)

    for a in post.poll.answers:
        answer = TblAnswers()
        answer.text = a.text
        answer.rate = a.rate
        answer.likes = a.votes
        write_record(answer, get_db().session)

    return jsonify({})


@app.route('/all', methods=['GET'])
def get_all():
    return jsonify([p.json() for p in TblProposals.query.all()])
