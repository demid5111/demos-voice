from app import app
from flask import jsonify, request

from app.core.parsers.vk import VKParser

@app.route('/')
@app.route('/index')
def index():
    return 'Hello, World!'


@app.route('/new')
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
    parser.parse(data['fromUrl'])
    return jsonify({})
