from app import MONGO
from flask import Blueprint, request, abort, jsonify
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


@naslovnica_bp.route('/<value>', methods=['GET', 'POST'])
def elementi(value):
    if request.method != 'GET':
        data_handler = DataHandler(MONGO.db)
        data = request.get_json()
        data_handler.check_value(value, data, request.method)
        return jsonify(data)

    return abort(400)
