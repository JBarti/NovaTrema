from app import MONGO
from flask import Blueprint, request
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


@naslovnica_bp.route('/slika', methods=['POST'])
def update_slika():
    data_handler = DataHandler(MONGO.db)
    slika = request.get_json()['slika']
    if slika is not None:
        data_handler.post_background_photo(slika)

    return data_handler.get_page_data()


@naslovnica_bp.route('/post', methods=['POST'])
def add_post():
    data_handler = DataHandler(MONGO.db)
    post_data = request.get_json()
    data_handler.post_new_post(post_data)

    return data_handler.get_page_data()
