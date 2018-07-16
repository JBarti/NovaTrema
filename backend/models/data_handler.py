from flask import jsonify
from naslovna.app import MONGO

class DataHandler:

    def __init__(self):
        global MONGO
        self.mongo_db = MONGO.db
        self.collection = {}
        self.data = {}

    def get_data(self, key):
        json_data = jsonify(self.collection[key])
        return json_data
