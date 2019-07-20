import os

ACCESS_TOKEN = 'ask Alexander about VK app'
with open('.secret_access_token') as f:
    ACCESS_TOKEN = f.read()

DATA_FOLDER = '../db'


class Config:
    # database config
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{}/test.db'.format(DATA_FOLDER)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
