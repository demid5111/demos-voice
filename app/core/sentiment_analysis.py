import json

from requests import post

from app.constants import SENTIMENT_TOKEN


def analyze_sentiments(text):
    data = {
        'txt': text,
        'lang': 'rus'
    }
    url = 'https://tt-api.tech/1.0/sentiment'
    headers = {
        'Authorization': 'Token {}'.format(SENTIMENT_TOKEN),
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    r = post(url, data=json.dumps(data), headers=headers)
    return json.loads(r.text)['result']