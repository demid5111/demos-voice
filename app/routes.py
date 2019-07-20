from app import app
from flask import jsonify, request


@app.route('/')
@app.route('/index')
def index():
    return 'Hello, World!'


@app.route('/new')
def import_from_post():
    # data = request.get_json()
    data = {
        'socialNetwork': 'vk',
        'fromUrl': 'vk',
    }
    net = data['socialNetwork']
    if net != 'vk':
        raise NotImplementedError

    parser = VKParser()
    parser.parse(data['fromUrl'])
    return jsonify({})
