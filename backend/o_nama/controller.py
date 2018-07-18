from flask import jsonify, Blueprint


class DataHandler:
    def __init__(self, db):
        self.collection = db.onama

    def get_page_data(self):
        json_data = jsonify(
            {
                "kontakti": self.collection["kontakti"],
                "poslovanje": self.collection["poslovanje"],
                "projekti": self.collection["projekti"],
                "profesori": self.collection["profesori"],
                "nagrade": self.collection["nagrade"],
            }
        )
        return json_data
