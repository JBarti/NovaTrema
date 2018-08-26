from app import MONGO
from flask import Blueprint, request, abort, jsonify
from controller import DataHandler, JSONEncoder

naslovnica_bp = Blueprint('naslovnica_api', __name__, url_prefix='/naslovnica')


@naslovnica_bp.route('/test', methods=['GET'])
def test():
    return "test"


@naslovnica_bp.route('/', methods=['GET'])
def naslovnica():
    data_handler = DataHandler(MONGO.db)
    data = data_handler.get_page_data()
    return JSONEncoder().encode(data)


@naslovnica_bp.route('/<value>', methods=['POST', 'PUT', 'DELETE'])
def elementi(value):
    data_handler = DataHandler(MONGO.db)
    data = request.get_json()
    returned_data = data_handler.check_value(value, data, request.method)
    return JSONEncoder().encode(returned_data)
