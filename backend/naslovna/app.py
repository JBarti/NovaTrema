from flask import Flask
from flask_cors import CORS
from config import db_create
from config import config

def app_create(debug=False):
    app = Flask(__name__)

    db_create(app)
    CORS(app)

    return app


app = app_create()

if __name__=='__main__':
    app.run()