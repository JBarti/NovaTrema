from flask import jsonify, Blueprint


class DataHandler:
    def __init__(self, db):
        self.pageData = db.onama.findOne()

    def get_page_data(self):
        json_data = jsonify(
            {
                "kontakti": self.pageData["kontakti"],
                "poslovanje": self.pageData["poslovanje"],
                "projekti": self.pageData["projekti"],
                "profesori": self.pageData["profesori"],
                "nagrade": self.pageData["nagrade"],
            }
        )
        return json_data
