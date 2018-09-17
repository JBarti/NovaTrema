from flask import abort
from bson import ObjectId


class DeleteHandler:
    """
    Class used for handling delete requests

    """

    def __init__(self, db):
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
            "post": self.delete_post,
            "achievement": self.delete_achievement,
            "college": self.delete_college,
            "contact": self.delete_contact,
            "subject": self.delete_subject,
            "link": self.delete_link
        }
        case = switcher.get(value, None)
        return case(data)

    def delete_post(self, post_data):
        """Function which deletes a post from the db

        Arguments:
            post_data {dict}

        Returns:
            dict -- post data which was received
        """

        try:
            for post in self.db.novosti.find():
                if post["_id"] == ObjectId(post_data["_id"]):
                    self.db.novosti.delete_one({"_id": ObjectId(post["_id"])})
                    return post
        except KeyError:
            return abort(400, "The data you have sent does not have the required keys")

        return abort(400)

    def delete_achievement(self, achievement_data):
        """Function which deletes an achievement from the db

        Arguments:
            achievement_data {dict}

        Returns:
            dict -- achievement data which was received
        """

        try:
            for achievement in self.db.postignuca.find():
                if achievement['_id'] == ObjectId(achievement_data['_id']):
                    self.db.postignuca.delete_one(
                        {"_id": ObjectId(achievement["_id"])})
                    return achievement
        except KeyError:
            return abort(400, "The data you have sent does not have the required keys")

        return abort(400)

    def delete_college(self, college_data):
        """Function which deletes a colleges' info from the db

        Arguments:
            college_data {dict}

        Returns:
            dict -- college data which was received
        """

        data = self.db.naslovnica.find_one({'colleges': {'$exists': True}})
        if not data:
            return abort(400, "The data you are trying to delete does not yet exist")
        count = True
        try:
            for college in data['colleges']:
                if college['icon'] == college_data['icon']:
                    data['colleges'].remove(college)
                    count = False
                    break
            if count:
                return abort(400)
        except KeyError:
            return abort(400, "The data you have sent does not have the required keys")
        self.db.naslovnica.update_one(
            data, {'$set': {'colleges': data['colleges']}}
        )
        return college_data

    def delete_subject(self, subject_data):
        """Function which deletes a subjects' info from the db

        Arguments:
            subject_data {dict} 

        Returns:
            [type] -- subject data which was received
        """

        data = self.db.naslovnica.find_one({'subjects': {'$exists': True}})
        if not data:
            return abort(400, "The data you are trying to delete does not yet exist")
        current = data['subjects']
        try:
            for subject in data['subjects']:
                if subject['icon'] == subject_data['icon']:
                    current.remove(subject)
                    break
        except KeyError:
            return abort(400, "The data you have sent does not have the required keys")
        self.db.naslovnica.update_one(
            data, {'$set': {'subjects': current}}
        )
        return subject_data

    def delete_contact(self, contact_data):
        """Function which deletes a contact from the db

        Arguments:
            contact_data {dict}

        Returns:
            dict -- contact data which was received
        """
        try:
            for contact in self.db.contacts.find():
                print(contact)
                if contact['_id'] == ObjectId(contact_data['_id']):
                    self.db.postignuca.delete_one(contact)
                    return contact
        except KeyError:
            return abort(400, "The data you have sent does not have the required keys")
        return abort(400)

    def delete_link(self, link_data):
        """Function which deletes a links' info from the db

        Arguments:
            link_data {dict}

        Returns:
            dict -- link data which was received
        """

        data = self.db.naslovnica.find_one({'links': {'$exists': True}})
        if not data:
            return abort(400, "The data you are trying to delete does not yet exist")
        try:
            for link in data['links']:
                if link['name'] == link_data['name']:
                    data['links'].remove(link)
                    break
        except KeyError:
            return abort(400, "The data you have sent does not have the required keys")
        self.db.naslovnica.update_one(
            data, {'$set': {'links': data['links']}}
        )
        return link_data
