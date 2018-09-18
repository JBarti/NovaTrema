from flask import abort
from bson import ObjectId


class PutHandler:
    """
    Class that handles put requests
    """

    def __init__(self, db):
        """The __init__ method for the class

        Arguments:
            db {<class pymongo>} -- connection to the database
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
            "image": self.update_image,
            "headmaster": self.update_headmaster,
            "post": self.update_post,
            "achievement": self.update_achievement,
            "college": self.update_achievement,
            "contact": self.update_contact,
            "link": self.update_link
        }
        case = switcher.get(value, None)
        return case(data)

    def update_image(self, img_data):
        """Function which updates the background image in the db

        Arguments:
            img_data {dict}:
                {
                    "url": str
                }

        Returns:
            dict -- image data which was received
        """

        check = ["url"]

        data = self.db.naslovnica.find_one(
            {'back_image': {'$exists': True}})
        if not data:
            return abort(400)

        try:
            if not isinstance(img_data['url'], str):
                return abort(400, "The data you have sent contains different value types than needed")
            if sorted(img_data.keys()) != sorted(check):
                return abort(400, "The data you have sent contains a different set of keys than needed")
            matches = self.db.naslovnica.update_one(
                {"back_image": {"$exists": True}}, {"$set": {"back_image": img_data}})
        except KeyError:
            return abort(400, "The data you have sent does not have the required keys")
        if matches.matched_count == 1:
            return img_data
        return abort(400, "The data you are trying to update does not exist in the database")

    def update_headmaster(self, welcome_data):
        """Function which updates the headmaster info in the db

        Arguments:
            welcome_data {dict}:
                {
                    "image": str,
                    "welcome_message": str
                }

        Returns:
            dict -- welcome data which was received
        """

        check = ["image", "welcome_message"]

        data = self.db.naslovnica.find_one({'headmaster': {'$exists': True}})
        if not data:
            abort(400)

        try:
            for key in welcome_data:
                if not isinstance(welcome_data[key], str) and not isinstance(key, str):
                    return abort(400, "The data you have sent contains different value types than needed")
            if sorted(check) != sorted(welcome_data.keys()):
                return abort(400, "The data you have sent contains a different set of keys than needed")
            matches = self.db.naslovnica.update_one(
                {"headmaster": {"$exists": True}}, {"$set": {"headmaster": welcome_data}})
        except KeyError:
            return abort(400, "The data you have sent does not have the required keys")
        if matches.matched_count == 1:
            return welcome_data
        return abort(400, "The data you are trying to update does not exist in the database")

    def update_post(self, post_data):
        """Function which updates a post in the db

        Arguments:
            post_data {dict}:
                {
                    "title": str,
                    "body": str,
                    "date": str,
                    "image": str,
                    "tldr": str,
                    "author": str,
                    "_id": str
                }

        Returns:
            dict -- post data which was received
        """

        check = ["title", "body", "date", "image", "tldr", "author", "_id"]

        try:
            for key in post_data:
                if not isinstance(post_data[key], str) and not isinstance(key, str) and key != "_id":
                    return abort(400, "The data you have sent contains different value types than needed")
            if sorted(check) != sorted(post_data.keys()):
                return abort(400, "The data you have sent contains a different set of keys than needed")
            post_data["_id"] = ObjectId(post_data["_id"])
            matches = self.db.novosti.update_one(
                {"_id": post_data["_id"]}, {"$set": post_data})

        except KeyError:
            return abort(400, "The data you have sent does not have the required keys")
        if matches.matched_count == 1:
            return post_data
        return abort(400, "The data you are trying to update does not exist in the database")

    def update_achievement(self, achievement_data):
        """Function which updates an achievement in the db

        Arguments:
            achievement_data {dict}:
                {
                    "title": str,
                    "image": str,
                    "body": str,
                    "_id": str
                }

        Returns:
            dict -- achievement data which was received
        """

        check = ["title", "image", "body", "_id"]

        try:
            for key in achievement_data:
                if not isinstance(achievement_data[key], str) and not isinstance(key, str) and key != "_id":
                    return abort(400, "The data you have sent contains different value types than needed")
            if sorted(check) != sorted(achievement_data.keys()):
                return abort(400, "The data you have sent contains a different set of keys than needed")
            achievement_data["_id"] = ObjectId(achievement_data["_id"])
            matches = self.db.postignuca.update_one(
                {"_id": achievement_data['_id']}, {"$set": achievement_data})

        except KeyError:
            return abort(400, "The data you have sent does not have the required keys")

        if matches.matched_count == 1:
            return achievement_data
        return abort(400, "The data you are trying to update does not exist in the database")

    def update_contact(self, contact_data):
        """Function which updates a contact in the db

        Arguments:
            contact_data {dict}:
                {
                    "name": str,
                    "number": str,
                    "mail": str,
                    "_id": str
                }

        Returns:
            dict -- contact data which was received
        """

        check = ["name", "number", "mail", "_id"]

        try:
            for key in contact_data:
                if not isinstance(contact_data[key], str) and not isinstance(key, str) and key != "key":
                    return abort(400, "The data you have sent contains different value types than needed")
            if sorted(check) != sorted(contact_data.keys()):
                return abort(400, "The data you have sent contains a different set of keys than needed")
            contact_data["_id"] = ObjectId(contact_data["_id"])
            matches = self.db.contacts.update_one(
                {"_id": contact_data['_id']}, {"$set": contact_data})
        except KeyError:
            return abort(400, "The data you have sent does not have the required keys")
        if matches.matched_count == 1:
            return contact_data
        return abort(400, "The data you are trying to update does not exist in the database")

    def update_link(self, link_data):
        """Function which updates a link in the db

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
            return abort(400)

        try:
            for key in link_data:
                if not isinstance(link_data[key], str) and not isinstance(key, str):
                    return abort(400, "The data you have sent contains different value types than needed")
            if sorted(check) != sorted(link_data.keys()):
                return abort(400, "The data you have sent contains a different set of keys than needed")
            for link in data['links']:
                if link['name'] == link_data['name'] or link['link'] == link_data['link']:
                    data["links"].remove(link)
                    break
            data['links'].append(link_data)
            matches = self.db.naslovnica.update_one(
                {"links": {"$exists": True}}, {
                    '$set': {'links': data["links"]}}
            )
        except KeyError:
            return abort(400, "The data you have sent does not have the required keys")
        if matches.matched_count == 1:
            return link_data
        return abort(400, "The data you are trying to update does not exist in the database")
