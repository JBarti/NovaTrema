from flask import jsonify


class DataHandler:
    def __init__(self, db):
        self.pageData = db.naslovnica.findOne()

    def get_page_data(self):
        json_data = jsonify(
            {
                "slika": self.pageData["slika"],
                "ravnateljica": self.pageData["ravnateljica"],
                "predmeti": self.pageData["predmeti"],
                "novosti": self.pageData["novosti"],
                "widgeti": self.pageData["widgeti"],
                "kontakti": self.pageData["kontakti"],
                "linkovi": self.pageData["linkovi"],
            }
        )
        return json_data
