# routes.py
from flask import request, jsonify, redirect
import pandas as pd
from data.meta_api_handler import MetaApiHandler
from access.meta_access import ACCESS_TOKEN


class Routes:
    meta_handler = MetaApiHandler(ACCESS_TOKEN)

    @staticmethod
    def index():
        return "Welcome to our project!"

    @staticmethod
    def ask_permission():
        return "Do you give permission to fetch your Facebook data? If yes, go to /myposts?permission=yes"

    @classmethod
    def my_posts(cls):
        # Check if user has given permission
        if 'permission' in request.args and request.args['permission'] == 'yes':
            data = cls.meta_handler.fetch_data('me/posts', {'limit': 10})  # Fetch the last 10 posts

            # Check if data contains the 'data' key
            if 'data' in data:
                df = pd.DataFrame(data['data'])
                return df.head().to_json(orient='records')
            else:
                return jsonify(data)  # Return the original data, which might contain an error message
        else:
            # Redirect to permission asking route
            return redirect("/ask_permission", code=302)
