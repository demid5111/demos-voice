import json

from requests import post

from app.constants import SENTIMENT_TOKEN


def analyze_spam(text):
    data = {
        'txt': text,
        'lang': 'rus'
    }
    url = 'https://tt-api.tech/1.0/spam'
    headers = {
        'Authorization': 'Token {}'.format(SENTIMENT_TOKEN),
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    try:
        r = post(url, data=json.dumps(data), headers=headers)
        return json.loads(r.text)['result']
    except:
        return dict(spam=False, confidence=1)