from app import app
from flask import jsonify, render_template, request

from app.core.parsers.vk import VKParser
from app.factories.database import get_db
from app.models.regions import TblRegions
from app.utils import write_record


@app.route('/')
def home():
    return app.send_static_file('index.html')


@app.route('/new', methods=['POST'])
def import_from_post():
    data = request.get_json()
    # data = {
    #     'socialNetwork': 'vk',
    #     'fromUrl': 'https://vk.com/moneysecrets?w=wall-184648030_2',
    # }
    net = data['socialNetwork']
    if net != 'vk':
        raise NotImplementedError

    parser = VKParser()
    post = parser.parse(data['fromUrl'])

    region = TblRegions()
    region.name = 'Nizhny Novgorod'
    write_record(region, get_db().session)
    return jsonify({})


@app.route('/all', methods=['GET'])
def get_all():
    data = [
        {
            'title': 'First',
            'id': '1',
        },
        {
            'title': 'Second',
            'id': '2',
        },
        {
            'title': 'Third',
            'id': '3',
        }
    ]
    return jsonify(data)
