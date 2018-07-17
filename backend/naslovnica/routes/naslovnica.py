from app import MONGO
from flask import jsonify, Blueprint
from controller import DataHandler

naslovnica_bp = Blueprint('naslovnica_api', __name__, url_prefix='/naslovnica')


@naslovnica_bp.route('/test', methods=['GET'])
def test():
    return "test"


@naslovnica_bp.route('/', methods=['GET'])
def naslovnica():
    data_handler = DataHandler(MONGO.db)
    data_handler.collection = data_handler.mongo_db.naslovnica
    data = {
        "slika": data_handler.get_data("slika"),
        "predmeti": data_handler.get_data("predmeti")
    }
    return jsonify(data)
