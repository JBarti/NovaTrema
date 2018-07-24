from flask import jsonify

class DataHandler:
    def __init__(self, db):
        self.pageData = db.natjecaji.findOne()

    def get_page_data(self):
        json_data = jsonify(
            {
                "dokumenti": self.pageData["dokumenti"],
            }
        )
        return json_data
