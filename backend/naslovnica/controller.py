from flask import jsonify, abort
from datetime import datetime


class DataHandler:
    def __init__(self, db):
        self.db = db.naslovnica

    def get_page_data(self):
        json_data = jsonify(
            self.db.find_one()
        )
        return json_data

    def check_value(self, key, data, req_method):
        post_options = {
            "slika": self.change_back_photo,
            "novost": self.add_new_post,
            "uspjeh": self.add_new_achievement,
            "faks": self.add_new_college,
            "predmet": self.add_new_subject,
            "kontakt": self.add_new_contact,
            "link": self.add_new_link
        }
        put_options = {
            "novost": self.update_post,
            "uspjeh": self.update_achievement,
            "kontakt": self.update_contact,
            "link": self.update_link
        }

        delete_options = {
            "novost": self.delete_post,
            "uspjeh": self.delete_achievement,
            "faks": self.delete_college,
            "predmet": self.delete_subject,
            "kontakt": self.delete_contact,
            "link": self.delete_link
        }

        if req_method == 'POST':
            case = post_options.get(key, None)
        elif req_method == 'PUT':
            case = put_options.get(key, None)
        elif req_method == 'DELETE':
            case = delete_options.get(key, None)

        if case is not None:
            return case(data)
        return abort(404)

    def change_back_photo(self, img_data):
        data = self.db.find_one()
        if len(img_data.keys()) == 1:
            try:
                if img_data['url'] == str:
                    self.db.update_one(data, {'$set': {'slika': img_data['url']}}})
                    return img_data
                else:
                    return abort(400)
            except KeyError:
                return abort(400)

        return abort(400)

    def add_new_post(self, post_data):
        data = self.db.find_one()
        check = ["title", "body", "date", "publihser", "img"]

        try:
            valid = True
            for key in post_data:
                if str != type(post_data[key]):
                    valid = False
            if len(check) == len(post_data.keys()):
                return abort(400)
            if valid:
                current = data['novosti']
                self.db.update_one(
                    data, {'$set': {'novosti': current.append(post_data)}})

        except KeyError:
            return abort(400)

        return post_data

    def add_new_achievement(self, achievement_data):
        data=self.db.find_one()
        check=["ikona", "tekst"]

        try:
            valid=True
            for key in achievement_data:
                if str != type(achievement_data[key]):
                    valid=False
            if len(check) != len(achievement_data):
                return abort(400)
            if valid:
                current=data['postignuca']
                self.db.update_one(
                    data, {'$set': {'postignuca': current.append(achievement_data)}})

        except KeyError:
            return abort(400)

        return achievement_data

    def add_new_college(self, college_data):
        data=self.db.find_one()

        if len(college_data.keys()) == 1:
            try:
                if type(college_data['ikona']) == str:
                    current=data['faksovi']
                    self.db.update_one(
                        data, {'$set': {'faksovi': current.append(college_data)}})
                    return college_data
                else:
                    return abort(404)
            except KeyError:
                return abort(400)

        return abort(400)

    def add_new_subject(self, subject_data):
        data=self.db.find_one()

        if len(subject_data.keys()) == 1:
            try:
                if type(subject_data['ikona']) == str:
                    current=data['predmeti']
                    self.db.update_one(
                        data, {'$set': {'predmeti': current.append(subject_data)}})
                    return subject_data
                else:
                    return abort(404)
            except KeyError:
                return abort(400)

        return abort(400)

    def add_new_contact(self, contact_data):
        data=self.db.find_one()
        check=["ime", "broj"]

        try:
            valid=True
            for key in contact_data:
                if str != type(contact_data[key]):
                    valid=False
            if len(check) != len(contact_data):
                return abort(400)
            if valid:
                current=data['kontakti']
                self.db.update_one(data, {'$set'{'kontakti': current.append(contact_data)}})

        except KeyError:
            return abort(400)

        return contact_data

    def add_new_link(self, link_data):
        data=self.db.find_one()
        check=["ime", "link"]

        try:
            valid=True
            for key in link_data:
                if str != type(link_data[key]):
                    valid=False
            if len(check) != len(link_data):
                return abort(400)
            if valid:
                current=data['linkovi']
                self.db.update_one(
                    data, {'$set': {'linkovi': current.append(link_data)}})

        except KeyError:
            return abort(400)

        return link_data

    def update_post(self, post_data):
        pass

    def update_achievement(self, achievement_data):
        pass

    def update_contact(self, contact_data):
        pass

    def update_link(self, link_data):
        pass

    def delete_post(self):
        pass

    def delete_achievement(self):
        pass

    def delete_college(self):
        pass

    def delete_subject(self):
        pass

    def delete_contact(self):
        pass

    def delete_link(self):
        pass
