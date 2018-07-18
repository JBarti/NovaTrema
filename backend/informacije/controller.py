from flask import jsonify

class DataHandler:
    def __init__(self, db):
        self.collection = db.natjecaji

    def get_page_data(self):
        json_data = jsonify(
            {
                "dokumenti": self.collection["dokumenti"],
            }
        )
        return json_data
