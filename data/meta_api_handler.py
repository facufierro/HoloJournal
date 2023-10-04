# meta_api_handler.py
import requests


class MetaApiHandler:
    BASE_URL = 'https://graph.facebook.com/v12.0/'

    def __init__(self, access_token):
        self.access_token = access_token

    def fetch_data(self, endpoint, params={}):
        params['access_token'] = self.access_token
        response = requests.get(self.BASE_URL + endpoint, params=params)
        return response.json()
