from app import MONGO
from flask import Blueprint
from controller import DataHandler

naslovnica_bp = Blueprint('naslovnica_api', __name__, url_prefix='/naslovnica')


@naslovnica_bp.route('/test', methods=['GET'])
def test():
    return "test"


@naslovnica_bp.route('/', methods=['GET'])
def naslovnica():
    data_handler = DataHandler(MONGO.db)
    data = data_handler.get_page_data()
    return data
