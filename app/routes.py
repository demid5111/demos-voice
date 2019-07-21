from app import app
from flask import jsonify, request

from app.core.parsers.vk import VKParser
from app.core.sentiment_analysis import analyze_sentiments
from app.factories.database import get_db
from app.models.answers import TblAnswers
from app.models.comments import TblComments
from app.models.discussions import TblDiscussions
from app.models.proposals import TblProposals
from app.utils import write_record, fill_sentiments


@app.route('/')
def home():
    return app.send_static_file('index.html')


@app.route('/new', methods=['POST', 'GET'])
def import_from_post():
    data = request.get_json()
    if not data:
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

    fill_sentiments(proposal.id)
    return jsonify({})


@app.route('/all', methods=['GET'])
def get_all():
    res = []
    for proposal in TblProposals.query.all():
        discussion = TblDiscussions.query.filter_by(proposal_id=proposal.id).first()
        answers = TblAnswers.query.filter_by(discussion_id=discussion.id).all()

        res.append({
            **proposal.json(),
            'poll': [a.json() for a in answers]
        })
    return jsonify(res)


@app.route('/analyze', methods=['GET', 'POST'])
def analyze_proposal():
    data = request.get_json()
    if not data:
        data = {
            'proposalId': '1'
        }
    fill_sentiments(data['proposalId'])
    return jsonify({})

