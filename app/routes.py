from app import app
from flask import jsonify, render_template, request

from app.core.parsers.vk import VKParser


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
