from datetime import datetime
from flask import jsonify
from bson import ObjectId


class GetHandler:
    def __init__(self, db):
        self.db = db

    def get_page_data(self):
        """Returns data required for main page"""

        data = self.db.naslovnica.find()
        list_of_posts = [post for post in self.db.novosti.find()]
        latest_four = []
        parsed_data = {}
        for document in data:
            parsed_data[list(document.keys())[0]] = document

        if list_of_posts:
            while len(latest_four) != 4 or not list_of_posts:
                latest_post = [post for post in list_of_posts if parse_date(post['date']) == parse_date(
                    max(post['date'] for post in list_of_posts))][0]
                latest_four.append(latest_post)
                list_of_posts.remove(latest_post)

        parsed_data['news'] = latest_four
        return parsed_data


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


def jsonify_objectId(data):
    """
    Deals with jsonifying ObjectId

    Arguments:
    data -- dictionary containing data

    """
    for key in data:
        if isinstance(data[key], ObjectId):
            data[key] = str(data[key])
    return jsonify(data)
