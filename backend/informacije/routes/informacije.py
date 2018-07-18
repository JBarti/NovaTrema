from flask import Blueprint
from app import MONGO
from controller import DataHandler

info_bp = Blueprint('info_api', __name__, url_prefix='/info')

@info_bp.route('/test')
def test():
    return 'test'

@info_bp.route('/', methods=['GET'])
def info():
    data_handler = DataHandler(MONGO.db)
    data = data_handler.get_page_data()
    return data