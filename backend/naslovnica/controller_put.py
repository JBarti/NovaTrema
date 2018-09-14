from flask import abort
from bson import ObjectId


class PutHandler:
    def __init__(self, db):
        self.db = db

    def call_function(self, value, data):
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
        """
        Method is called on corresponding route
        Updates the existing image data in the database
        Returns the updated data if no errors,
        elsewise it returns the http status code for bad request ( 400 )

        Arguments:
        img_data -- dictionary containing image data

        """
        check = ["url"]

        data = self.db.naslovnica.find_one({'image': {'$exists': True}})
        if not data:
            return abort(400)

        try:
            if not isinstance(img_data['url'], str):
                return abort(400)
            if sorted(img_data.keys()) != sorted(check):
                return abort(400)
            matches = self.db.naslovnica.update_one(
                {"headmaster": {"$exists": True}}, {"$set": {"image": img_data}})
        except KeyError:
            return abort(400)
        if matches.matched_count == 1:
            return img_data

    def update_headmaster(self, welcome_data):
        """
        Method is called on corresponding route
        Updates the existing headmaster welcome data in the database
        Returns the updated data if no errors,
        elsewise it returns the http status code for bad request ( 400 )

        Arguments:
        welcome_data -- dictionary containing headmaster welcome data

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
            matches = self.db.naslovnica.update_one(
                {"headmaster": {"$exists": True}}, {"$set": {"headmaster": welcome_data}})
        except KeyError:
            return abort(400)
        if matches.matched_count == 1:
            return welcome_data
        return abort(400)

    def update_post(self, post_data):
        """
        Method is called on corresponding route
        Updates an existing post in the database
        Returns the updated data if no errors,
        elsewise it returns the http status code for bad request ( 400 )

        Arguments:
        post_data -- dictionary containing post data

        """
        check = ["title", "body", "date", "image", "tldr", "author", "_id"]

        try:
            for key in post_data:
                if not isinstance(post_data[key], str) and not isinstance(key, str) and key != "_id":
                    return abort(400)
            if sorted(check) != sorted(post_data.keys()):
                return abort(400)
            post_data["_id"] = ObjectId(post_data["_id"])
            matches = self.db.novosti.update_one(
                {"_id": post_data["_id"]}, {"$set": post_data})

        except KeyError:
            return abort(400)
        if matches.matched_count == 1:
            return post_data
        return abort(400)

    def update_achievement(self, achievement_data):
        """
        Method is called on corresponding route
        Updates an existing achievement in the database
        Returns the updated data if no errors,
        elsewise it returns the http status code for bad request ( 400 )

        Arguments:
        achievement_data -- dictionary containing achievement data

        """
        check = ["title", "image", "body", "_id"]

        try:
            for key in achievement_data:
                if not isinstance(achievement_data[key], str) and not isinstance(key, str) and key != "_id":
                    return abort(400)
            if sorted(check) != sorted(achievement_data.keys()):
                return abort(400)
            achievement_data["_id"] = ObjectId(achievement_data["_id"])
            matches = self.db.postignuca.update_one(
                {"_id": achievement_data['_id']}, {"$set": achievement_data})

        except KeyError:
            return abort(400)

        if matches.matched_count == 1:
            return achievement_data
        return abort(400)

    def update_contact(self, contact_data):
        """
        Method is called on corresponding route
        Updates an existing contact in the database
        Returns the updated data if no errors,
        elsewise it returns the http status code for bad request ( 400 )

        Arguments:
        contact_data -- dictionary containing contact data

        """
        check = ["name", "number", "mail", "_id"]

        try:
            for key in contact_data:
                if not isinstance(contact_data[key], str) and not isinstance(key, str) and key != "key":
                    return abort(400)
            if sorted(check) != sorted(contact_data.keys()):
                return abort(400)
            contact_data["_id"] = ObjectId(contact_data["_id"])
            matches = self.db.contacts.update_one(
                {"_id": contact_data['_id']}, {"$set": contact_data})
        except KeyError:
            return abort(400)
        if matches.matched_count == 1:
            return contact_data
        return abort(400)

    def update_link(self, link_data):
        """
        Method is called on corresponding route
        Updates an existing link in the database
        Returns the updated data if no errors,
        elsewise it returns the http status code for bad request ( 400 )

        Arguments:
        link_data -- dictionary containing link data

        """
        check = ["name", "link"]

        data = self.db.naslovnica.find_one({'links': {'$exists': True}})
        if not data:
            return abort(400)

        try:
            for key in link_data:
                if not isinstance(link_data[key], str) and not isinstance(key, str):
                    abort(400)
            if sorted(check) != sorted(link_data.keys()):
                return abort(400)
            current = data['links']
            for link in data['links']:
                if link['name'] == link_data['name'] or link['link'] == link_data['link']:
                    current.remove(link)
                    break
            matches = self.db.naslovnica.update_one(
                {"links": {"$exists": True}}, {
                    '$set': {'links': current.append(link_data)}}
            )
        except KeyError:
            return abort(400)
        if matches.matched_count == 1:
            return link_data
        return abort(400)
