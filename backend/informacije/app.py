from flask import Flask
from flask_cors import CORS
from config import db_create
from sys import argv


def app_create(debug=False):
    app = Flask(__name__)

    mongo = db_create(app)
    CORS(app)

    return app, mongo


APP, MONGO = app_create()

if __name__ == '__main__':
    from routes.informacije import info_bp
    APP.register_blueprint(info_bp)

    if argv[1]:
        APP.run(port=int(argv[1]))
    else:
        APP.run()
