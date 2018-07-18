from flask import jsonify


class DataHandler:
    def __init__(self, db):
        self.collection = db.natjecaji

    def get_page_data(self):
        json_data = jsonify(
            {
                "slika": self.collection["slika"],
                "naslov": self.collection["naslov"],
                "datum": self.collection["datum"],
                "ukratko": self.collection["ukratko"],
                "tekst": self.collection["tekst"],
            }
        )
        return json_data
