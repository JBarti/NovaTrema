from flask import jsonify


class DataHandler:
    def __init__(self, db):
        self.collection = db.naslovnica

    def get_page_data(self):
        json_data = jsonify(
            {
                "slika": self.collection["slika"],
                "ravnateljica": self.collection["ravnateljica"],
                "predmeti": self.collection["predmeti"],
                "novosti": self.collection["novosti"],
                "widgeti": self.collection["widgeti"],
                "kontakti": self.collection["kontakti"],
                "linkovi": self.collection["linkovi"],
            }
        )
        return json_data
