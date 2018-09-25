from flask import Flask, jsonify
from flask_cors import CORS
from config import db_create
from sys import argv


def app_create(debug=False):
    """[summary]

    Keyword Arguments:
        debug {bool} --  (default: {False})

    Returns:
        <class flask.Flask>, <classs flask_pymongo.PyMongo>
    """

    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.config['SECRET_KEY'] = '6E732C635B575C7831315C7839645C783830505C7830385C786234225C7838645C7838383B3F4B7D5C786633475C7866654F5C783063'
    mongo_db = db_create(app)
    CORS(app)

    return app, mongo_db


APP, MONGO = app_create()


@APP.route('/test', methods=['GET'])
def test():
    return "test"


@APP.route('/', methods=['GET'])
def index():
    data = MONGO.db.naslovnica.find_one()
    return jsonify(data)


if __name__ == '__main__':

    from routes import naslovnica_bp
    APP.register_blueprint(naslovnica_bp)

    if argv[1]:
        APP.run(port=int(argv[1]))
    else:
        APP.run()
