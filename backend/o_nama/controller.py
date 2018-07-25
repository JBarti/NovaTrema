from flask import jsonify, Blueprint


class DataHandler:
    def __init__(self, db):
        self.db = db.db.onama

    def get_page_data(self):
        json_data = jsonify(
            self.db.find_one()
        )
        return json_data
