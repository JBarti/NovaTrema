from flask import jsonify, abort
from datetime import datetime


class DataHandler:
    def __init__(self, db):
        self.db = db

    def get_page_data(self):
        data = self.db.naslovnica.find()
        list_of_posts = [post for post in self.db.novosti.find()]
        latest_four = []
        parsed_data = {}
        for document in data:
            parsed_data[document.keys()[0]] = document

        while len(latest_four) != 4 or not list_of_posts:
            latest_post = [post for post in list_of_posts if parse_date(post['date']) == max(
                parse_date(post['date']) for post in list_of_posts)][0]
            latest_four.append(latest_post)
            list_of_posts.remove(latest_post)

        parsed_data['news'] = latest_four
        return jsonify(parsed_data)

    def check_value(self, key, data, req_method):
        post_options = {
            "slika": self.add_back_photo,
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

    def add_back_photo(self, img_data):
        data = self.db.naslovnica.find({'slika': {'$exists': True}})
        if len(img_data.keys()) == 1:
            try:
                if img_data['url'] == str:
                    self.db.update_one(
                        data, {'$set': {'slika': img_data}})
                    return img_data
                else:
                    return abort(400)
            except KeyError:
                return abort(400)

        return abort(400)

    def add_new_post(self, post_data):
        check = ["title", "body", "date", "publisher", "img"]

        try:
            valid = True
            for key in post_data:
                if str != type(post_data[key]):
                    valid = False
            if len(check) != len(post_data.keys()):
                return abort(400)
            if valid:
                self.db.novosti.insert(post_data)

        except KeyError:
            return abort(400)

        return post_data

    def add_new_achievement(self, achievement_data):
        check = ["icon", "text", "body"]

        try:
            valid = True
            for key in achievement_data:
                if str != type(achievement_data[key]):
                    valid = False
            if len(check) != len(achievement_data):
                return abort(400)
            if valid:
                self.db.postginuca.insert(achievement_data)

        except KeyError:
            return abort(400)

        return achievement_data

    def add_new_college(self, college_data):
        data = self.db.naslovnica.find({'colleges': {'$exists': True}})

        if len(college_data.keys()) == 1:
            try:
                if type(college_data['icon']) == str:
                    current = data['colleges']
                    self.db.update_one(
                        data, {'$set': {'colleges': current.append(college_data)}})
                    return college_data
                else:
                    return abort(404)
            except KeyError:
                return abort(400)

        return abort(400)

    def add_new_subject(self, subject_data):
        data = self.db.naslovnica.find({'subjects': {'$exists': True}})

        if len(subject_data.keys()) == 1:
            try:
                if type(subject_data['icon']) == str:
                    current = data['subjects']
                    self.db.update_one(
                        data, {'$set': {'subjects': current.append(subject_data)}})
                    return subject_data
                else:
                    return abort(404)
            except KeyError:
                return abort(400)

        return abort(400)

    def add_new_contact(self, contact_data):
        check = ["name", "number"]

        try:
            valid = True
            for key in contact_data:
                if str != type(contact_data[key]):
                    valid = False
            if len(check) != len(contact_data):
                return abort(400)
            if valid:
                self.db.contacts.insert(contact_data)

        except KeyError:
            return abort(400)

        return contact_data

    def add_new_link(self, link_data):
        data = self.db.naslovnica.find({'links': {'$exists': True}})
        check = ["name", "link"]

        try:
            valid = True
            for key in link_data:
                if str != type(link_data[key]):
                    valid = False
            if len(check) != len(link_data):
                return abort(400)
            if valid:
                current = data['links']
                self.db.update_one(
                    data, {'$set': {'links': current.append(link_data)}})

        except KeyError:
            return abort(400)

        return link_data

    def update_post(self, post_data):
        check = ["title", "body", "date", "publisher", "img"]

        try:
            valid = True
            for key in post_data:
                if str != type(post_data[key]) and key != "_id":
                    valid = False
            if len(check)+1 != len(post_data.keys()):
                return abort(400)
            if valid:
                self.db.novosti.update_one(
                    post_data['_id'], post_data)
        except KeyError:
            return abort(400)

        return post_data

    def update_achievement(self, achievement_data):
        check = ["icon", "text", "title"]

        try:
            valid = True
            for key in achievement_data:
                if str != type(achievement_data[key]) and key != "_id":
                    valid = False
            if len(check)+1 != len(achievement_data):
                return abort(400)
            if valid:
                self.db.postignuca.update_one(
                    achievement_data['_id'], achievement_data)

        except KeyError:
            return abort(400)

        return achievement_data

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
