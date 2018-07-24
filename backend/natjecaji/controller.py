from flask import jsonify


class DataHandler:
    def __init__(self, db):
        self.pageData = db.natjecaji.findOne()

    def get_page_data(self):
        json_data = jsonify(
            {
                "slika": self.pageData["slika"],
                "naslov": self.pageData["naslov"],
                "datum": self.pageData["datum"],
                "ukratko": self.pageData["ukratko"],
                "tekst": self.pageData["tekst"],
            }
        )
        return json_data
