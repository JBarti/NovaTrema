from flask import jsonify, abort
from datetime import datetime
from flask_pymongo import pymongo


class DataHandler:
    def __init__(self, db):
        self.db = db

    def get_page_data(self):
        
        """Return data required for page /naslovnica"""
        
        data = self.db.naslovnica.find()
        list_of_posts = [post for post in self.db.novosti.find()]
        latest_four = []
        parsed_data = {}
        for document in data:
            parsed_data[document.keys()[0]] = document

        while len(latest_four) != 4 or not list_of_posts:
            latest_post = [post for post in list_of_posts if parse_date(post['date']) == parse_date(max(
                post['date'] for post in list_of_posts))][0]
            latest_four.append(latest_post)
            list_of_posts.remove(latest_post)

        parsed_data['news'] = latest_four
        return jsonify(parsed_data)

    def check_value(self, key, data, req_method):

        """
        Checks what kind of request is sent on what route and then calls function accordingly
        Returns 404 Not Found page if bad route is sent

        Arguments:
        key -- string from the end of the route
            proper values are: 'image', 'headmaster', 'post', 'achievement', 'college', 'subject',
            'contact', 'link'
        data -- data which is sent with the request
        req_method -- type of request

        """

        if req_method == 'POST':
            case = getattr(self, "add_new_"+key, None)
        elif req_method == 'PUT':
            case = getattr(self, "update_"+key, None)
        elif req_method == 'DELETE':
            case = getattr(self, "delete_"+key, None)

        if case is not None:
            return case(data)
        return abort(404)

    def add_new_image(self, img_data):
        data = self.db.naslovnica.find({'image': {'$exists': True}})
        if not data:
            self.db.naslovnica.insert({"image": {}})
            data = self.db.naslovnica.find({'headmaster': {'$exists': True}})

        try:
            valid = True
            if not isinstance(img_data['url'], str):
                valid = False
            if len(img_data.keys()) != 1:
                return abort(400)
            if valid:
                self.db.naslovnica.update_one(
                    data, {"$set": {"headmaster": img_data}})
        except KeyError:
            return abort(400)

        return img_data

    def add_new_headmaster(self, hello_data):
        data = self.db.naslovnica.find({'headmaster': {'$exists': True}})
        if not data:
            self.db.naslovnica.insert({'headmaster': {}})
            data = self.db.naslovnica.find({'headmaster': {'$exists': True}})

        try:
            valid = True
            for key in hello_data:
                if not isinstance(hello_data[key], str):
                    valid = False
            if len(hello_data.keys()) != 2:
                return abort(400)
            if valid:
                self.db.naslovnica.update_one(
                    data, {"$set": {"headmaster": hello_data}})
        except KeyError:
            return abort(400)

        return hello_data

    def add_new_post(self, post_data):
        try:
            valid = True
            for key in post_data:
                if not isinstance(post_data[key], str):
                    valid = False
            if len(post_data.keys()) != 5:
                return abort(400)
            if valid:
                self.db.novosti.insert(post_data)

        except KeyError:
            return abort(400)

        return post_data

    def add_new_achievement(self, achievement_data):
        try:
            valid = True
            for key in achievement_data:
                if not isinstance(achievement_data[key], str):
                    valid = False
            if len(achievement_data) != 3:
                return abort(400)
            if valid:
                self.db.postginuca.insert(achievement_data)

        except KeyError:
            return abort(400)

        return achievement_data

    def add_new_college(self, college_data):
        data = self.db.naslovnica.find({'colleges': {'$exists': True}})
        if not data:
            self.db.naslovnica.insert({'colleges': []})
            data = self.db.naslovnica.find({'colleges': {'$exists': True}})

        if len(college_data.keys()) == 1:
            try:
                if not isinstance(college_data['icon'], str):
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
        if not data:
            self.db.naslovnica.insert({'subject': []})
            data = self.db.naslovnica.find({'subjects': {'$exists': True}})

        if len(subject_data.keys()) == 1:
            try:
                if not isinstance(subject_data['icon'], str):
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
        try:
            valid = True
            for key in contact_data:
                if not isinstance(contact_data[key], str):
                    valid = False
            if len(contact_data) != 2:
                return abort(400)
            if valid:
                self.db.contacts.insert(contact_data)

        except KeyError:
            return abort(400)

        return contact_data

    def add_new_link(self, link_data):
        data = self.db.naslovnica.find({'links': {'$exists': True}})
        if not data:
            self.db.naslovnica.insert({'links': []})
            data = self.db.naslovnica.find({'links': {'$exists': True}})

        try:
            valid = True
            for key in link_data:
                if not isinstance(link_data[key], str):
                    valid = False
            if len(link_data) != 2:
                return abort(400)
            if valid:
                current = data['links']
                self.db.update_one(
                    data, {'$set': {'links': current.append(link_data)}})

        except KeyError:
            return abort(400)

        return link_data

    def update_image(self, img_data):
        data = self.db.naslovnica.find({'image': {'$exists': True}})

        try:
            valid = True
            if not isinstance(img_data['url'], str):
                valid = False
            if len(img_data.keys()) != 1:
                return abort(400)
            if valid:
                self.db.naslovnica.update_one(
                    data, {"$set": {"image": img_data}})
        except KeyError:
            return abort(400)

        return img_data

    def update_headmaster(self, hello_data):
        data = self.db.naslovnica.find({'headmaster': {'$exists': True}})

        try:
            valid = True
            for key in hello_data:
                if not isinstance(hello_data[key], str):
                    valid = False
            if len(hello_data.keys()) != 2:
                return abort(400)
            if valid:
                self.db.naslovnica.update_one(
                    data, {"$set": {"headmaster": hello_data}})
        except KeyError:
            return abort(400)

        return hello_data
    
    def update_post(self, post_data):
        try:
            valid = True
            for key in post_data:
                if not isinstance(post_data[key], str) and key != "_id":
                    valid = False
            if len(post_data.keys()) != 6:
                return abort(400)
            if valid:
                self.db.novosti.update_one(
                    {"_id": post_data['_id']}, {"$set": post_data})
        except KeyError:
            return abort(400)

        return post_data

    def update_achievement(self, achievement_data):
        try:
            valid = True
            for key in achievement_data:
                if not isinstance(achievement_data[key], str) and key != "_id":
                    valid = False
            if len(achievement_data) != 4:
                return abort(400)
            if valid:
                self.db.postignuca.update_one(
                    {"_id": achievement_data['_id']}, {"$set": achievement_data})

        except KeyError:
            return abort(400)

        return achievement_data

    def update_contact(self, contact_data):
        try:
            valid = True
            for key in contact_data:
                if not isinstance(contact_data[key], str) and key != '_id':
                    valid = False
            if len(contact_data) != 3:
                return abort(400)
            if valid:
                self.db.contacts.update_one(
                    {"_id": contact_data['_id']}, {"$set": contact_data})
        except KeyError:
            return abort(400)

        return contact_data

    def update_link(self, link_data):
        data = self.db.naslovnica.find({'links': {'$exists': True}})
        if not data:
            return abort(400)

        try:
            valid = True
            for key in link_data:
                if not isinstance(link_data[key], str):
                    valid = False
            if len(link_data) != 2:
                return abort(400)
            if valid:
                current = data['links']
                for link in data['links']:
                    if link['name'] == link_data['name'] or link['link'] == link_data['link']:
                        current.remove(link)
                        break
                self.db.update_one(
                    data, {'$set': {'links': current.append(link_data)}}
                )
        except KeyError:
            return abort(400)
        return link_data

    def delete_post(self, post_data):
        try:
            for post in self.db.novosti.find():
                if post['_id'] == post_data['_id']:
                    self.db.novosti.delete_one(post)
                    return post
        except KeyError:
            return abort(400)

        return abort(400)

    def delete_achievement(self, achievement_data):
        try:
            for achievement in self.db.postignuca.find():
                if achievement['_id'] == achievement_data['_id']:
                    self.db.postignuca.delete_one(achievement)
                    return achievement
        except KeyError:
            return abort(400)

        return abort(400)

    def delete_college(self, college_data):
        data = self.db.naslovnica.find({'colleges':{'$exists':True}})
        if not data:
            return abort(400)
        current = data['colleges']
        for college in data['colleges']:
            if college['icon'] == college_data['icon']:
                current.remove(college)
                break

        self.db.naslovnica.update_one(
            data, {'$set': {'colleges': current}}
        )
        return college_data

    def delete_subject(self, subject_data):
        data = self.db.naslovnica.find({'subjects': {'$exists': True}})
        if not data:
            return abort(400)
        current = data['subjects']
        for subject in data['subjects']:
            if subject['icon'] == subject_data['icon']:
                current.remove(subject)
                break

        self.db.naslovnica.update_one(
            data, {'$set': {'subjects': current}}
        )
        return subject_data

    def delete_contact(self, contact_data):
        for contact in self.db.contacts.find():
            if contact['_id'] == contact_data['id']:
                self.db.postignuca.delete_one(contact)
                return contact
        return abort(400)

    def delete_link(self, link_data):
        data = self.db.naslovnica.find({'links': {'$exists': True}})
        if not data:
            return abort(400)
        current = data['links']
        for link in data['links']:
            if link['name'] == link_data['name']:
                current.remove(link)
                break

        self.db.naslovnica.update_one(
            data, {'$set': {'links': current}}
        )
        return link_data


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
