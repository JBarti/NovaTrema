from flask import jsonify, Blueprint
from models.data_handler import DataHandler

naslovnica_bp = Blueprint('naslovnica_api', __name__, url_prefix='/naslovnica')

@naslovnica_bp.route('/', methods=['GET'])
def naslovna():
    data_handler = DataHandler()
    data_handler.collection = data_handler.mongo_db.naslovnica
    data = {
        "slika": data_handler.get_data("slika"),
        "predmeti":data_handler.get_data("predmeti")
    }
    return jsonify(data)