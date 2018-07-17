from flask import jsonify


class DataHandler:
    def __init__(self, db):
        self.mongo_db = db
        self.collection = {}
        self.data = {}

    def get_data(self, key):
        json_data = jsonify(self.collection[key])
        return json_data
