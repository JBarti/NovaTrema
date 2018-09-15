from flask import abort


class PostHandler:
    """
    Class used for handling post requests

    """

    def __init__(self, db):
        self.db = db

    def call_function(self, value, data):
        switcher = {
            "image": self.add_new_image,
            "headmaster": self.add_new_headmaster,
            "post": self.add_new_post,
            "achievement": self.add_new_achievement,
            "college": self.add_new_college,
            "contact": self.add_new_contact,
            "subject": self.add_new_subject,
            "link": self.add_new_link
        }
        case = switcher.get(value, None)
        return case(data)

    def add_new_image(self, img_data):
        """
        Method is called on its corresponding route
        Adds an background image to database
        Returns the same data if no errors, elsewise it returns the http status code for bad request

        Arguments:
        img_data -- dictionary containing image data

        """
        check = ["url"]

        data = self.db.naslovnica.find_one({'back_image': {'$exists': True}})
        if not data:
            self.db.naslovnica.insert({"back_image": {}})
            data = self.db.naslovnica.find_one(
                {'back_image': {'$exists': True}})

        try:
            if not isinstance(img_data['url'], str):
                return abort(400)
            if sorted(img_data.keys()) != sorted(check):
                return abort(400)
            self.db.naslovnica.update_one(
                {"back_image": {"$exists": True}}, {"$set": {"back_image": img_data}})
        except KeyError:
            return abort(400)

        return img_data

    def add_new_headmaster(self, welcome_data):
        """
        Method is called on its corresponding route
        Adds the headmaster welcome data to database
        Returns the same data if no errors,
        elsewise it returns the http status code for bad request ( 400)

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
                {"headmaster": {"$exists": True}}, {"$set": {"headmaster": welcome_data}})
        except KeyError:
            return abort(400)

        return welcome_data

    def add_new_post(self, post_data):
        """
        Method is called on corresponding route
        Adds a new post to the database
        Returns the same data if no errors,
        elsewise it returns the http status code for bad request ( 400)

        Arguments:
        post_data -- dictionary containing post data

        """
        check = ["title", "body", "date", "image", "tldr", "author"]

        try:
            for key in post_data:
                if not isinstance(post_data[key], str) and not isinstance(key, str):
                    return abort(400)
            if sorted(post_data.keys()) != sorted(check):
                return abort(400)
            self.db.novosti.insert(post_data)

        except KeyError:
            return abort(400)

        return post_data

    def add_new_achievement(self, achievement_data):
        """
        Method is called on corresponding route
        Adds a new achievement to the database
        Returns the same data if no errors,
        elsewise it returns the http status code for bad request ( 400 )

        Arguments:
        achievement_data -- dictionary containing achievement data

        """
        check = ["title", "image", "body"]

        try:
            for key in achievement_data:
                if not isinstance(achievement_data[key], str) and not isinstance(key, str):
                    return abort(400)
            if sorted(achievement_data.keys()) != sorted(check):
                return abort(400)
            self.db.postignuca.insert(achievement_data)

        except KeyError:
            return abort(400)

        return achievement_data

    def add_new_college(self, college_data):
        """
        Method is called on corresponding route
        Adds a new college to the database
        Returns the same data if no errors,
        elsewise it returns the http status code for bad request ( 400 )

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
                if not isinstance(college_data[key], str) and not isinstance(key, str):
                    return abort(400)
            if sorted(college_data.keys()) != sorted(check):
                return abort(400)
            data['colleges'].append(college_data)
            self.db.naslovnica.update_one(
                {"colleges": {"$exists": True}},
                {'$set': {'colleges': data["colleges"]}})
        except KeyError:
            return abort(400)

        return college_data

    def add_new_subject(self, subject_data):
        """
        Method is called on corresponding route
        Adds a new subject to the database
        Returns the same data if no errors,
        elsewise it returns the http status code for bad request ( 400 )

        Arguments:
        subject_data -- dictionary containing subject data

        """
        check = ["name", "icon"]
        data = self.db.naslovnica.find_one({'subjects': {'$exists': True}})
        if not data:
            self.db.naslovnica.insert({'subjects': []})
            data = self.db.naslovnica.find_one({'subjects': {'$exists': True}})

        try:
            for key in subject_data:
                if not isinstance(subject_data[key], str) and not isinstance(key, str):
                    return abort(400)
                if sorted(check) != sorted(subject_data.keys()):
                    return abort(400)
            print(data["subjects"])
            data['subjects'].append(subject_data)
            print(data["subjects"])
            self.db.naslovnica.update_one(
                {"subjects": {"$exists": True}},
                {'$set': {'subjects': data["subjects"]}})
            print(self.db.naslovnica.find_one({"subjects": {"$exists": True}}))
        except KeyError:
            return abort(400)

        return subject_data

    def add_new_contact(self, contact_data):
        """
        Method is called on corresponding route
        Adds a new contact to the database
        Returns the same data if no errors,
        elsewise it returns the http status code for bad request ( 400 )

        Arguments:
        contact_data -- dictionary containing contact data

        """
        check = ["name", "number", "mail"]

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
        Returns the same data if no errors,
        elsewise it returns the http status code for bad request ( 400 )

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
                if not isinstance(link_data[key], str) and not isinstance(key, str):
                    return abort(400)
            if sorted(link_data.keys()) != sorted(check):
                return abort(400)
            data['links'].append(link_data)
            self.db.naslovnica.update_one(
                {"links": {"$exists": True}}, {'$set': {'links': data["links"]}})

        except KeyError:
            return abort(400)

        return link_data
