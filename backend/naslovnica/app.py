from flask import Flask
from flask_cors import CORS
from config import db_create


def app_create(debug=False):
    app = Flask(__name__)

    mongo_db = db_create(app)
    CORS(app)

    return app, mongo_db


APP, MONGO = app_create()


@APP.route('/test', methods=['GET'])
def test():
    return "test"


if __name__ == '__main__':

    from routes import naslovnica_bp
    APP.register_blueprint(naslovnica_bp)

    APP.run()
