from flask import abort
from bson import ObjectId


class DeleteHandler:
    """
    Class used for handling delete requests

    """

    def __init__(self, db):
        self.db = db

    def call_function(self, value):
        switcher = {
            "post": self.delete_post,
            "achievement": self.delete_achievement,
            "college": self.delete_college,
            "contact": self.delete_contact,
            "subject": self.delete_subject,
            "link": self.delete_link
        }
        case = switcher.get(value, None)
        return case

    def delete_post(self, post_data):
        """
        Method is called on corresponding route
        Deletes a post from the database
        Returns the deleted data if no errors,
        elsewise it returns the http status code for bad request ( 400 )

        Arguments:
        post_data -- dictionary containing post data

        """

        try:
            for post in self.db.novosti.find():
                if post["_id"] == ObjectId(post_data["_id"]):
                    self.db.novosti.delete_one({"_id": ObjectId(post["_id"])})
                    return post
        except KeyError:
            return abort(400)

        return abort(400)

    def delete_achievement(self, achievement_data):
        """
        Method is called on corresponding route
        Deletes a achievement from the database
        Returns the deleted data if no errors,
        elsewise it returns the http status code for bad request ( 400 )

        Arguments:
        achievement_data -- dictionary containing achievement data

        """
        try:
            for achievement in self.db.postignuca.find():
                if achievement['_id'] == ObjectId(achievement_data['_id']):
                    self.db.postignuca.delete_one(
                        {"_id": ObjectId(achievement["_id"])})
                    return achievement
        except KeyError:
            return abort(400)

        return abort(400)

    def delete_college(self, college_data):
        """
        Method is called on corresponding route
        Deletes a college from the database
        Returns the deleted data if no errors,
        elsewise it returns the http status code for bad request ( 400 )

        Arguments:
        college_data -- dictionary containing college data

        """

        data = self.db.naslovnica.find_one({'colleges': {'$exists': True}})
        if not data["colleges"]:
            return abort(400)
        current = data['colleges']
        count = True
        for college in data['colleges']:
            if college['icon'] == college_data['icon']:
                current.remove(college)
                count = False
                break
        if count:
            return abort(400)

        self.db.naslovnica.update_one(
            data, {'$set': {'colleges': current}}
        )
        return college_data

    def delete_subject(self, subject_data):
        """
        Method is called on corresponding route
        Deletes a subject from the database
        Returns the deleted data if no errors,
        elsewise it returns the http status code for bad request ( 400 )

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
        Returns the deleted data if no errors,elsewise it returns the http status code for bad request ( 400 )

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
        Returns the deleted data if no errors,
        elsewise it returns the http status code for bad request ( 400 )

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
