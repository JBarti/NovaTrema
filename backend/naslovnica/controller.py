from flask import jsonify


class DataHandler:
    def __init__(self, db):
        self.db = db.naslovnica

    def get_page_data(self):
        json_data = jsonify(
            self.db.find_one()
        )
        return json_data

    def post_background_photo(self, photoURL):
        data = self.db.find_one()
        current = data
        data['slika']['url'] = photoURL
        self.db.replace_one(current, data)
        return None

    def post_new_post(self, post_data):
        data = self.db.find_one()
        current = data
        check = ["title", "body", "date", "publisher", "img"]
        if len(check) == len([keyA for keyA, keyB in zip(check, post_data.keys()) if keyA == keyB]):
            data['novosti'].append(post_data)
            self.db.replace_one(current, data)

        return None
