from flask import jsonify
from datetime import datetime


class DataHandler:
    def __init__(self, db):
        self.db = db.naslovnica

    def get_page_data(self):
        json_data = jsonify(
            self.db.find_one()
        )
        return json_data

    def check_value(self, key, data):
        options = {
            "slika": self.change_back_photo,
            "novost": self.add_new_post,
            "uspjeh": self.add_new_achievement,
            "faks": self.add_new_college,
            "predmet": self.add_new_subject,
            "konakt": self.add_new_contact,
            "link": self.add_new_link
        }
        case = options.get(key, None)
        if case is not None:
            return case(data)
        return "Inserted key is not valid"

    def change_back_photo(self, img_data):
        data = self.db.find_one()
        current = data
        if len(img_data.keys()) == 1:
            try:
                if img_data['url'] == str:
                    data['slika']['url'] = img_data
                    self.db.replace_one(current, data)
                    return img_data
                else:
                    return "TypeError: The data sent is not of the required type"
            except KeyError:
                return "KeyError: Received data has an unknown key"

        return "Error: Sent data does not have the required number of keys"

    def add_new_post(self, post_data):
        data = self.db.find_one()
        current = data
        check = ["title", "body", "date", "publihser", "img"]

        try:
            valid = True
            for key in post_data:
                if str != type(post_data[key]):
                    valid = False
            if len(check) == len(post_data.keys()):
                return "Error: Sent data does not have the required number of keys"
            if valid:
                data['novosti'].append(post_data)
                self.db.replace_one(current, data)

        except KeyError:
            return "Key Error: Received data has an unknown key"

        return post_data

    def add_new_achievement(self, achievement_data):
        data = self.db.find_one()
        current = data
        check = ["ikona", "tekst"]

        try:
            valid = True
            for key in achievement_data:
                if str != type(achievement_data[key]):
                    valid = False
            if len(check) != len(achievement_data):
                return "Error: Sent data does not have the required number of keys"
            if valid:
                data['postignuca'].append(achievement_data)
                self.db.replace_one(current, data)

        except KeyError:
            return "Key Error: Received data has an unknown key"

        return achievement_data

    def add_new_college(self, college_data):
        data = self.db.find_one()
        current = data

        if len(college_data.keys()) == 1:
            try:
                if type(college_data['ikona']) == str:
                    data['faksovi'].append(college_data)
                    self.db.replace_one(current, data)
                    return college_data
                else:
                    return "TypeError: The data sent is not of the required type"
            except KeyError:
                return "KeyError: Received data has an unknown key"

        return "Error: Sent data does not have the required number of keys"

    def add_new_subject(self, subject_data):
        data = self.db.find_one()
        current = data

        if len(subject_data.keys()) == 1:
            try:
                if type(subject_data['ikona']) == str:
                    data['predmeti'].append(subject_data)
                    self.db.replace_one(current, data)
                    return subject_data
                else:
                    return "TypeError: The data sent is not of the required type"
            except KeyError:
                return "KeyError: Received data has an unknown key"

        return "Error: Sent data does not have the required number of keys"

    def add_new_contact(self, contact_data):
        data = self.db.find_one()
        current = data
        check = ["ime", "broj"]

        try:
            valid = True
            for key in contact_data:
                if str != type(contact_data[key]):
                    valid = False
            if len(check) != len(contact_data):
                return "Error: Sent data does not have the required number of keys"
            if valid:
                data['kontakti'].append(contact_data)
                self.db.replace_one(current, data)

        except KeyError:
            return "Key Error: Received data has an unknown key"

        return contact_data

    def add_new_link(self, link_data):
        data = self.db.find_one()
        current = data
        check = ["ime", "link"]

        try:
            valid = True
            for key in link_data:
                if str != type(link_data[key]):
                    valid = False
            if len(check) != len(link_data):
                return "Error: Sent data does not have the required number of keys"
            if valid:
                data['linkovi'].append(link_data)
                self.db.replace_one(current, data)

        except KeyError:
            return "Key Error: Received data has an unknown key"

        return link_data
