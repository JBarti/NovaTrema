from app import MONGO
from flask import Blueprint, request, abort, jsonify
from controller_post import PostHandler
from controller_put import PutHandler
from controller_utility import GetHandler, jsonify_objectId
from controller_delete import DeleteHandler

naslovnica_bp = Blueprint('naslovnica_api', __name__, url_prefix='/naslovnica')


@naslovnica_bp.route('/test', methods=['GET'])
def test():
    return "test"


@naslovnica_bp.route('/', methods=['GET'])
def naslovnica():
    data_handler = GetHandler(MONGO.db)
    data = data_handler.get_page_data()
    return jsonify(data)


@naslovnica_bp.route('/<value>', methods=['POST', 'PUT', 'DELETE'])
def elementi(value):
    data = request.get_json()
    if request.method == 'POST':
        data_handler = PostHandler(MONGO.db)
        func = data_handler.call_function(value, data)
        if func is not None:
            return jsonify_objectId(func)
        return abort(400)
    if request.method == 'PUT':
        data_handler = PutHandler(MONGO.db)
        func = data_handler.call_function(value, data)
        if func is not None:
            return jsonify_objectId(func)
        return abort(400)
    if request.method == 'DELETE':
        data_handler = DeleteHandler(MONGO.db)
        func = data_handler.call_function(value, data)
        if func is not None:
            return jsonify_objectId(func)
        return abort(400)
