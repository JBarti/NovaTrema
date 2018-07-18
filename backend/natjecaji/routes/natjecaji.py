from flask import Blueprint
from app import MONGO
from controller import DataHandler

natjecaji_bp = Blueprint('natjecaji_api', __name__, url_prefix='/natjecaji')

@natjecaji_bp.route('/test', methods=['GET'])
def test():
    return 'test'

@natjecaji_bp.route('/', methods=['GET'])
def natjecaji():
    data_handler = DataHandler(MONGO.db)
    data = data_handler.get_page_data()
    return data