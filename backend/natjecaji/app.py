from flask import Flask
from flask_cors import CORS
from config import db_create

def app_create(debug=False):
    app = Flask(__name__)

    mongo = db_create(app)
    CORS(app)

    return app, mongo

APP, MONGO = app_create()

if __name__ == '__main__':
    from routes.natjecaji import natjecaji_bp
    APP.register_blueprint(natjecaji_bp)
    
    APP.run()