from flask import abort


class PostHandler:
    """
    Class that handles post requests
    """

    def __init__(self, db):
        """The __init__ method for PostHandler class

        Arguments:
            db {<class pymongo>} -- connection to database
        """

        self.db = db

    def call_function(self, value, data):
        """Function which decides what is the method that will be called

        Arguments:
            value {str} -- the url suffix, the method which will be called depends on it
            data {dict} -- data which is sent on the specific url

        Returns:
            function call -- data which is returned if the data has been posted to the db successfully,
            elsewise it returns an http status code
        """

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
        """Function which adds a background image to the db

        Arguments:
            img_data {dict}:
                {
                    "url": str
                }

        Returns:
            dict -- image data which was received
        """

        check = ["url"]

        data = self.db.naslovnica.find_one({'back_image': {'$exists': True}})
        if not data:
            self.db.naslovnica.insert({"back_image": {}})
            data = self.db.naslovnica.find_one(
                {'back_image': {'$exists': True}})

        try:
            if not isinstance(img_data['url'], str):
                return abort(400, "The data you have sent contains different value types than needed")
            if sorted(img_data.keys()) != sorted(check):
                return abort(400, "The data you have sent contains a different set of keys than needed")
            self.db.naslovnica.update_one(
                {"back_image": {"$exists": True}}, {"$set": {"back_image": img_data}})
        except KeyError:
            return abort(400, "The data you have sent does not have the required keys")

        return img_data

    def add_new_headmaster(self, welcome_data):
        """Function which adds headmaster data to the db

        Arguments:
            welcome_data {dict}:
                {
                    "image" : str,
                    "welcome_message": str
                }

        Returns:
            dict -- welcome data which was received
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
                    return abort(400, "The data you have sent contains different value types than needed")
            if sorted(check) != sorted(welcome_data.keys()):
                return abort(400, "The data you have sent contains a different set of keys than needed")
            self.db.naslovnica.update_one(
                {"headmaster": {"$exists": True}}, {"$set": {"headmaster": welcome_data}})
        except KeyError:
            return abort(400, "The data you have sent does not have the required keys")

        return welcome_data

    def add_new_post(self, post_data):
        """Function which adds a new post to the db

        Arguments:
            post_data {dict}:
                 {
                     "title": str,
                     "body": str,
                     "date": str,
                     "image": str,
                     "tldr":str,
                     "author":str
                 }

        Returns:
            dict -- post data which was received
        """

        check = ["title", "body", "date", "image", "tldr", "author"]

        try:
            for key in post_data:
                if not isinstance(post_data[key], str) and not isinstance(key, str):
                    return abort(400, "The data you have sent contains different value types than needed")
            if sorted(post_data.keys()) != sorted(check):
                return abort(400, "The data you have sent contains a different set of keys than needed")
            self.db.novosti.insert(post_data)

        except KeyError:
            return abort(400, "The data you have sent does not have the required keys")

        return post_data

    def add_new_achievement(self, achievement_data):
        """Function which adds a new achievement to the db

        Arguments:
            achievement_data {dict}:
                {
                    "title": str,
                    "image": str,
                    "body": str
                }

        Returns:
            dict -- achievement data which was received
        """

        check = ["title", "image", "body"]

        try:
            for key in achievement_data:
                if not isinstance(achievement_data[key], str) and not isinstance(key, str):
                    return abort(400, "The data you have sent contains different value types than needed")
            if sorted(achievement_data.keys()) != sorted(check):
                return abort(400, "The data you have sent contains a different set of keys than needed")
            self.db.postignuca.insert(achievement_data)

        except KeyError:
            return abort(400, "The data you have sent does not have the required keys")

        return achievement_data

    def add_new_college(self, college_data):
        """Function which adds new college info to the db

        Arguments:
            college_data {dict}:
                {
                    "icon":str,
                    "name":str
                }

        Returns:
            dict -- college data which was received
        """

        check = ["icon", "name"]
        data = self.db.naslovnica.find_one({'colleges': {'$exists': True}})
        if not data:
            self.db.naslovnica.insert({'colleges': []})
            data = self.db.naslovnica.find_one({'colleges': {'$exists': True}})

        try:
            for key in college_data:
                if not isinstance(college_data[key], str) and not isinstance(key, str):
                    return abort(400, "The data you have sent contains different value types than needed")
            if sorted(college_data.keys()) != sorted(check):
                return abort(400, "The data you have sent contains a different set of keys than needed")
            data['colleges'].append(college_data)
            self.db.naslovnica.update_one(
                {"colleges": {"$exists": True}},
                {'$set': {'colleges': data["colleges"]}})
        except KeyError:
            return abort(400, "The data you have sent does not have the required keys")

        return college_data

    def add_new_subject(self, subject_data):
        """Function which adds new subject info to the db

        Arguments:
            subject_data {dict}:
                {
                    "name":str,
                    "icon":str
                }

        Returns:
            dict -- college data which was received
        """

        check = ["name", "icon"]
        data = self.db.naslovnica.find_one({'subjects': {'$exists': True}})
        if not data:
            self.db.naslovnica.insert({'subjects': []})
            data = self.db.naslovnica.find_one({'subjects': {'$exists': True}})

        try:
            for key in subject_data:
                if not isinstance(subject_data[key], str) and not isinstance(key, str):
                    return abort(400, "The data you have sent contains different value types than needed")
                if sorted(check) != sorted(subject_data.keys()):
                    return abort(400, "The data you have sent contains a different set of keys than needed")
            print(data["subjects"])
            data['subjects'].append(subject_data)
            print(data["subjects"])
            self.db.naslovnica.update_one(
                {"subjects": {"$exists": True}},
                {'$set': {'subjects': data["subjects"]}})
            print(self.db.naslovnica.find_one({"subjects": {"$exists": True}}))
        except KeyError:
            return abort(400, "The data you have sent does not have the required keys")

        return subject_data

    def add_new_contact(self, contact_data):
        """Function which adds a new contact to the db

        Arguments:
            contact_data {dict}:
                {
                    "name": str,
                    "number":str,
                    "mail":str
                }

        Returns:
            dict -- contact data which was received
        """

        check = ["name", "number", "mail"]

        try:
            for key in contact_data:
                if not isinstance(contact_data[key], str) and not isinstance(key, str):
                    return abort(400, "The data you have sent contains different value types than needed")
            if sorted(check) != sorted(contact_data.keys()):
                return abort(400, "The data you have sent contains a different set of keys than needed")
            self.db.contacts.insert(contact_data)

        except KeyError:
            return abort(400, "The data you have sent does not have the required keys")

        return contact_data

    def add_new_link(self, link_data):
        """Function which adds a new link to the database

        Arguments:
            link_data {dict}:
                {
                    "name": str,
                    "link": str
                }

        Returns:
            dict -- link data which was received
        """

        check = ["name", "link"]

        data = self.db.naslovnica.find_one({'links': {'$exists': True}})
        if not data:
            self.db.naslovnica.insert({'links': []})
            data = self.db.naslovnica.find_one({'links': {'$exists': True}})

        try:
            for key in link_data:
                if not isinstance(link_data[key], str) and not isinstance(key, str):
                    return abort(400, "The data you have sent contains different value types than needed")
            if sorted(link_data.keys()) != sorted(check):
                return abort(400, "The data you have sent contains a different set of keys than needed")
            data['links'].append(link_data)
            self.db.naslovnica.update_one(
                {"links": {"$exists": True}}, {'$set': {'links': data["links"]}})

        except KeyError:
            return abort(400, "The data you have sent does not have the required keys")

        return link_data
