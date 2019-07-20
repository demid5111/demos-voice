from flask_cors import CORS

from app import app
from app.constants import Config
from app.factories.database import init_db_app

if __name__ == '__main__':
    app.config.from_object(Config())
    init_db_app(app)
    CORS(app)
    app.run()
