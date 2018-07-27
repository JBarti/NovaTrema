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
        return None

    def change_back_photo(self, img_data):
        data = self.db.find_one()
        current = data
        if type(img_data["url"]) == str:
            data['slika']['url'] = img_data
            self.db.replace_one(current, data)
        return None

    def add_new_post(self, post_data):
        data = self.db.find_one()
        current = data
        check = {
            "title": "string",
            "body": "body",
            "date": datetime.now(),
            "publisher": "publisher",
            "img": "img"
        }

        try:
            date = parse_date(post_data["date"])
            post_data["date"] = date

        except ValueError:
            return None

        try:
            valid = True
            for key in post_data:
                if type(check[key]) != type(post_data[key]):
                    valid = False
            if valid:
                data['novosti'].append(post_data)
                self.db.replace_one(current, data)

        except KeyError:
            return None

        return None

    def add_new_achievement(self, data):
        pass

    def add_new_college(self, data):
        pass

    def add_new_subject(self, data):
        pass

    def add_new_contact(self, data):
        pass

    def add_new_link(self, data):
        pass


def parse_date(text_date):

    dict_month = {
        "Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5,
        "Jun": 6, "Jul": 7, "Aug": 8, "Sept": 9, "Oct": 10,
        "Nov": 11, "Dec": 12
    }

    lst_date = text_date.split()
    lst_time = lst_date[4].split(':')

    yyyy = int(lst_date[3])
    mm = int(dict_month[lst_date[1]])
    dd = int(lst_date[2])
    h = int(lst_time[0])
    _min = int(lst_time[1])

    return datetime(yyyy, mm, dd, h, _min)
