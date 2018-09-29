import requests


class PymgurApi:
    """class that formats Pymgur rest-api to a python class

    Keyword arguments: 
        pymgur_url (str) -- url where pymgur api is run
    """

    def __init__(self, pymgur_url):
        if pymgur_url[-1] == '/':
            self.pymgur_url = pymgur_url
        else:
            self.pymgur_url = pymgur_url+'/'

    def upload_image(self, img_object):
        """function for uploading a python image object to pymgur

        Keyword arguments: 
            img_object (_io.TextIOWrapper) -- python file object containing the image being sent to pymgur

        Returns:
            json: a json object with format {'img_url': <url of image posted to pymgur api>}
        """
        try:
            r = requests.post(self.pymgur_url, files={'img': img_object})
            return r.json()
        except:
            return r.status_code
