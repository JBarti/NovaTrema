from flask import Blueprint
from app import MONGO
from controller import DataHandler

o_nama_bp = Blueprint('o_nama_api', __name__, url_prefix='/o_nama')

@o_nama_bp.route('/test', methods=['GET'])
def test():
    return 'test'

@o_nama_bp.route('/', methods=['GET'])
def onama():
    data_handler = DataHandler(MONGO.db)
    data = data_handler.get_page_data()
    return data
