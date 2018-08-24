from flask import jsonify, abort
from datetime import datetime


class DataHandler:
    def __init__(self, db):
        self.db = db

    def get_page_data(self):
        """Returns data required for main page"""

        data = self.db.naslovnica.find()
        list_of_posts = [post for post in self.db.novosti.find()]
        latest_four = []
        parsed_data = {}
        for document in data:
            parsed_data[document.keys()[0]] = document

        if list_of_posts:
            while len(latest_four) != 4 or not list_of_posts:
                latest_post = [post for post in list_of_posts if parse_date(post['date']) == parse_date(max(
                    post['date'] for post in list_of_posts))][0]
                latest_four.append(latest_post)
                list_of_posts.remove(latest_post)

            parsed_data['news'] = latest_four
        return jsonify(parsed_data)

    def check_value(self, key, data, req_method):
        """
        Checks what kind of request is sent on what route and then returns a function call accordingly
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
        """
        Method is called on its corresponding route 
        Adds an background image to database
        Returns the same data if no errors, elsewise it returns the http status code for bad request

        Arguments: 
        img_data -- dictionary containing image data

        """
        check = ["url"]

        data = self.db.naslovnica.find_one({'image': {'$exists': True}})
        if not data:
            self.db.naslovnica.insert({"image": {}})
            data = self.db.naslovnica.find_one({'image': {'$exists': True}})

        try:
            if not isinstance(img_data['url'], str):
                return abort(400)
            if sorted(img_data.keys()) != sorted(check):
                return abort(400)
            self.db.naslovnica.update_one(
                data, {"$set": {"image": img_data}})
        except KeyError:
            return abort(400)

        return img_data

    def add_new_headmaster(self, welcome_data):
        """
        Method is called on its corresponding route 
        Adds the headmaster welcome data to database 
        Returns the same data if no errors, elsewise it returns the http status code for bad request ( 400) 

        Arguments: 
        welcome_data -- dictionary containing headmaster welcome data 

        """
        check = ["image", "welcome_message"]

        data = self.db.naslovnica.find_one({'headmaster': {'$exists': True}})
        if not data:
            self.db.naslovnica.insert({'headmaster': {}})
            data = self.db.naslovnica.find_one(
                {'headmaster': {'$exists': True}})

        try:
            for key in welcome_data:
                if not isinstance(welcome_data[key], str) and not isinstance(key, str):
                    return abort(400)
            if sorted(check) != sorted(welcome_data.keys()):
                return abort(400)
            self.db.naslovnica.update_one(
                data, {"$set": {"headmaster": welcome_data}})
        except KeyError:
            return abort(400)

        return welcome_data

    def add_new_post(self, post_data):
        """
        Method is called on corresponding route
        Adds a new post to the database
        Returns the same data if no errors, elsewise it returns the http status code for bad request ( 400)

        Arguments:
        post_data -- dictionary containing post data

        """
        check = ["title","body","date", "image", "tldr", "author"]

        try:
            for key in post_data:
                if not isinstance(post_data[key], str) and not isinstance(key, str):
                    return abort(400)
            if sorted(post_data.keys()) != sorted(check):
                return abort(400)
            if valid:
                self.db.novosti.insert(post_data)

        except KeyError:
            return abort(400)

        return post_data

    def add_new_achievement(self, achievement_data):
        """
        Method is called on corresponding route 
        Adds a new achievement to the database 
        Returns the same data if no errors, elsewise it returns the http status code for bad request ( 400 ) 

        Arguments: 
        achievement_data -- dictionary containing achievement data

        """
        check = ["title", "image","body"]

        try:
            for key in achievement_data:
                if not isinstance(achievement_data[key], str) and not isinstance(key, str):
                    return abort(400)
            if sorted(achievement_data.keys()) != sorted(check):
                return abort(400)
            self.db.postginuca.insert(achievement_data)

        except KeyError:
            return abort(400)

        return achievement_data

    def add_new_college(self, college_data):
        """
        Method is called on corresponding route
        Adds a new college to the database
        Returns the same data if no errors, elsewise it returns the http status code for bad request ( 400 )

        Arguments:
        college_data -- dictionary containing college data

        """
        check = ["icon", "name"]

        data = self.db.naslovnica.find_one({'colleges': {'$exists': True}})
        if not data:
            self.db.naslovnica.insert({'colleges': []})
            data = self.db.naslovnica.find_one({'colleges': {'$exists': True}})

        try:
            for key in college_data:
                if not isinstance(college_data[key], str) and not isinstance(key,str):
                    return abort(400)
            if sorted(college_data.keys()) != sorted(check):
                return abort(400)
            current = data['colleges']
            self.db.update_one(
                data, {'$set': {'colleges': current.append(college_data)}})
        except KeyError:
            return abort(400)

        return college_data

    def add_new_subject(self, subject_data):
        """
        Method is called on corresponding route 
        Adds a new subject to the database 
        Returns the same data if no errors, elsewise it returns the http status code for bad request ( 400 ) 

        Arguments: 
        subject_data -- dictionary containing subject data

        """
        check = ["name","icon"]

        data = self.db.naslovnica.find_one({'subjects': {'$exists': True}})
        if not data:
            self.db.naslovnica.insert({'subject': []})
            data = self.db.naslovnica.find_one({'subjects': {'$exists': True}})

        try:
            for key in subject_data:
                if not isinstance(subject_data[key], str) and not isinstance(key, str):
                    return abort(400)
                if sorted(check) != sorted(subject_data.keys()):
                    return abort(400)
            current = data['subjects']
            self.db.update_one(
                data, {'$set': {'subjects': current.append(subject_data)}})
        except KeyError:
            return abort(400)

        return subject_data

    def add_new_contact(self, contact_data):
        """
        Method is called on corresponding route 
        Adds a new contact to the database 
        Returns the same data if no errors, elsewise it returns the http status code for bad request ( 400 ) 

        Arguments: 
        contact_data -- dictionary containing contact data

        """
        check = ["name", "number","mail"]

        try:
            for key in contact_data:
                if not isinstance(contact_data[key], str) and not isinstance(key, str):
                    return abort(400)
            if sorted(check) != sorted(contact_data.keys()):
                return abort(400)
            self.db.contacts.insert(contact_data)

        except KeyError:
            return abort(400)

        return contact_data

    def add_new_link(self, link_data):
        """
        Method is called on corresponding route 
        Adds a new link to the database 
        Returns the same data if no errors, elsewise it returns the http status code for bad request ( 400 ) 

        Arguments: 
        link_data -- dictionary containing link data

        """
        check = ["name", "link"]

        data = self.db.naslovnica.find_one({'links': {'$exists': True}})
        if not data:
            self.db.naslovnica.insert({'links': []})
            data = self.db.naslovnica.find_one({'links': {'$exists': True}})

        try:
            for key in link_data:
                if not isinstance(link_data[key], str) and not isinstance(key,str):
                    return abort(400)
            if sorted(link_data.keys()) != sorted(check):
                return abort(400)
            current = data['links']
            self.db.update_one(
                data, {'$set': {'links': current.append(link_data)}})

        except KeyError:
            return abort(400)

        return link_data

    def update_image(self, img_data):
        """
        Method is called on corresponding route 
        Updates the existing image data in the database
        Returns the updated data if no errors, elsewise it returns the http status code for bad request ( 400 ) 

        Arguments: 
        img_data -- dictionary containing image data

        """
        check = ["url"]

        data = self.db.naslovnica.find_one({'image': {'$exists': True}})
        if not data:
            abort(400)

        try:
            if not isinstance(img_data['url'], str):
                return abort(400)
            if sorted(img_data.keys()) != sorted(check):
                return abort(400)
            self.db.naslovnica.update_one(
                data, {"$set": {"image": img_data}})
        except KeyError:
            return abort(400)

        return img_data

    def update_headmaster(self, hello_data):
        """
        Method is called on corresponding route 
        Updates the existing headmaster welcome data in the database 
        Returns the updated data if no errors, elsewise it returns the http status code for bad request ( 400 ) 

        Arguments: 
        hello_data -- dictionary containing headmaster welcome data

        """
        check = ["image", "welcome_message"]

        data = self.db.naslovnica.find_one({'headmaster': {'$exists': True}})
        if not data:
            abort(400)

        try:
            for key in welcome_data:
                if not isinstance(welcome_data[key], str) and not isinstance(key, str):
                    return abort(400)
            if sorted(check) != sorted(welcome_data.keys()):
                return abort(400)
            self.db.naslovnica.update_one(
                data, {"$set": {"headmaster": welcome_data}})
        except KeyError:
            return abort(400)

        return hello_data

    def update_post(self, post_data):
        """
        Method is called on corresponding route 
        Updates an existing post in the database 
        Returns the updated data if no errors, elsewise it returns the http status code for bad request ( 400 ) 

        Arguments: 
        post_data -- dictionary containing post data

        """
        check = ["title", "body", "date", "image", "tldr", "author", "_id"]

        try:
            for key in post_data:
                if not isinstance(post_data[key], str) and not isinstance(key,str) and key != "_id":
                    return abort(400)
            if sorted(check) != sorted(post_data.keys()):
                return abort(400)
            self.db.novosti.update_one(
                {"_id": post_data['_id']}, {"$set": post_data})
        except KeyError:
            return abort(400)

        return post_data

    def update_achievement(self, achievement_data):
        """
        Method is called on corresponding route 
        Updates an existing achievement in the database 
        Returns the updated data if no errors, elsewise it returns the http status code for bad request ( 400 ) 

        Arguments: 
        achievement_data -- dictionary containing achievement data

        """
        check = ["title", "image", "body", "_id"]

        try:
            for key in achievement_data:
                if not isinstance(achievement_data[key], str) and not isinstance(key,str) and key != "_id":
                    return abort(400)
            if sorted(check) != sorted(achievement_data.keys()):
                return abort(400)
            self.db.postignuca.update_one(
                {"_id": achievement_data['_id']}, {"$set": achievement_data})

        except KeyError:
            return abort(400)

        return achievement_data

    def update_contact(self, contact_data):
        """
        Method is called on corresponding route 
        Updates an existing contact in the database 
        Returns the updated data if no errors, elsewise it returns the http status code for bad request ( 400 ) 

        Arguments: 
        contact_data -- dictionary containing contact data

        """
        check = ["name", "number","mail", "_id"]

        try:
            for key in contact_data:
                if not isinstance(contact_data[key], str) and not isinstance(key, str) and key != "key":
                    return abort(400)
            if sorted(check) != sorted(contact_data.keys()):
                return abort(400)
            self.db.contacts.update_one(
                {"_id": contact_data['_id']}, {"$set": contact_data})
        except KeyError:
            return abort(400)

        return contact_data

    def update_link(self, link_data):
        """
        Method is called on corresponding route 
        Updates an existing link in the database 
        Returns the updated data if no errors, elsewise it returns the http status code for bad request ( 400 ) 

        Arguments: 
        link_data -- dictionary containing link data

        """
        check = ["name", "link"]

        data = self.db.naslovnica.find_one({'links': {'$exists': True}})
        if not data:
            return abort(400)

        try:
            for key in link_data:
                if not isinstance(link_data[key], str) and not isinstance(key,str):
                    abort(400)
            if sorted(check) != sorted(link_data.keys()):
                return abort(400)
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
        """
        Method is called on corresponding route 
        Deletes a post from the database 
        Returns the deleted data if no errors, elsewise it returns the http status code for bad request ( 400 ) 

        Arguments: 
        post_data -- dictionary containing post data

        """

        try:
            for post in self.db.novosti.find():
                if post['_id'] == post_data['_id']:
                    self.db.novosti.delete_one(post)
                    return post
        except KeyError:
            return abort(400)

        return abort(400)

    def delete_achievement(self, achievement_data):
        """
        Method is called on corresponding route 
        Deletes a achievement from the database 
        Returns the deleted data if no errors, elsewise it returns the http status code for bad request ( 400 ) 

        Arguments: 
        achievement_data -- dictionary containing achievement data

        """
        try:
            for achievement in self.db.postignuca.find():
                if achievement['_id'] == achievement_data['_id']:
                    self.db.postignuca.delete_one(achievement)
                    return achievement
        except KeyError:
            return abort(400)

        return abort(400)

    def delete_college(self, college_data):
        """
        Method is called on corresponding route 
        Deletes a college from the database 
        Returns the deleted data if no errors, elsewise it returns the http status code for bad request ( 400 ) 

        Arguments: 
        college_data -- dictionary containing college data

        """
        data = self.db.naslovnica.find_one({'colleges': {'$exists': True}})
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
        """
        Method is called on corresponding route 
        Deletes a subject from the database 
        Returns the deleted data if no errors, elsewise it returns the http status code for bad request ( 400 ) 

        Arguments: 
        subject_data -- dictionary containing subject data

        """
        data = self.db.naslovnica.find_one({'subjects': {'$exists': True}})
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
        """
        Method is called on corresponding route 
        Deletes a contact from the database 
        Returns the deleted data if no errors, elsewise it returns the http status code for bad request ( 400 ) 

        Arguments: 
        contact_data -- dictionary containing contact data

        """
        for contact in self.db.contacts.find():
            if contact['_id'] == contact_data['id']:
                self.db.postignuca.delete_one(contact)
                return contact
        return abort(400)

    def delete_link(self, link_data):
        """
        Method is called on corresponding route 
        Deletes a link from the database 
        Returns the deleted data if no errors, elsewise it returns the http status code for bad request ( 400 ) 

        Arguments: 
        link_data -- dictionary containing link data

        """
        data = self.db.naslovnica.find_one({'links': {'$exists': True}})
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
    """
    Convert js datetime to python datetime
    Returns a datetime object.

    Arguments:
    text_date -- string in the format of javascript datetime objects
    """

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
