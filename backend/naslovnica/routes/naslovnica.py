from app import MONGO
from flask import Blueprint, request, abort, jsonify
from controller_post import PostHandler
from controller_put import PutHandler
from controller_utility import GetHandler, jsonify_objectId
from controller_delete import DeleteHandler

naslovnica_bp = Blueprint('naslovnica_api', __name__, url_prefix='/naslovnica')


@naslovnica_bp.route('/test', methods=['GET'])
def test():
    """Test route for /naslovnica blueprint

    Returns:
        str 
    """

    return "test"


@naslovnica_bp.route('/', methods=['GET'])
def naslovnica():
    """Route which gets all the data needed for the homepage

    Returns:
        <class flask.Response> -- jsonified data needed for the homepage
    """

    data_handler = GetHandler(MONGO.db)
    data = data_handler.get_page_data()
    return jsonify(data)


@naslovnica_bp.route('/<element>', methods=['POST'])
def post_elements(element):
    """Route used for posting data.
    Data which is received on this route is a dictionary containing
    the data concerning the element which is being posted.

    Arguments:
        element {str} -- text value which defines which element will be posted

    Returns:
        <class flask.Response> or html status code -- jsonified data which has been received in the first place.
        The data is returned in case of no errors, and the html status code in case of an error
    """

    data = request.get_json()
    data_handler = PostHandler(MONGO.db)
    dict_data = data_handler.call_function(element, data)
    if isinstance(dict_data, dict):
        return jsonify_objectId(dict_data)
    return abort(400, "This is a non existant route")


@naslovnica_bp.route('/<element>', methods=['PUT'])
def put_elements(element):
    """Route used for updating data.
    Data which is received on this route is a dictionary containing
    the data concerning the element which is being updated.

    Arguments:
        element {str} -- text value which defines which element will be updated

    Returns:
        <class flask.Response> or html status code -- jsonified data which has been received in the first place.
        The data is returned in case of no errors, and the html status code in case of an error
    """
    data = request.get_json()
    data_handler = PutHandler(MONGO.db)
    dict_data = data_handler.call_function(element, data)
    if isinstance(dict_data, dict):
        return jsonify_objectId(dict_data)
    return abort(400, "This is a non existant route")


@naslovnica_bp.route('/<element>', methods=['DELETE'])
def delete_elements(element):
    """Route used for deleteing data.
    Data which is received on this route is a dictionary containing
    the data concerning the element which is being deleted

    Arguments:
        element {str} -- text value which defines which element will be deleted.

    Returns:
        <class flask.Response> or html status code -- jsonified data which has been received in the first place.
        The data is returned in case of no errors, and the html status code in case of an error
    """
    data = request.get_json()
    data_handler = DeleteHandler(MONGO.db)
    dict_data = data_handler.call_function(element, data)
    if isinstance(dict_data, dict):
        return jsonify_objectId(dict_data)
    return abort(400, "This is a non existant route")
