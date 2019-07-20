from flask_sqlalchemy import SQLAlchemy


def get_db() -> SQLAlchemy:
    return get_db.DB


get_db.DB = SQLAlchemy()


def init_db_app(app):
    database = get_db()
    with app.app_context():
        database.init_app(app)
    database.drop_all(app=app)
    database.create_all(app=app)
