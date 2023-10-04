# routes.py
from flask import request, jsonify, redirect
from utils.meta_api_handler import MetaApiHandler
from access.meta_access import ACCESS_TOKEN
from utils.data_manager import DataManager
from utils.debug import Log


class Routes:
    meta_handler = MetaApiHandler(ACCESS_TOKEN)

    @staticmethod
    def index():
        return '<h1>HoloJournal</h1></br><h3><a href="/myposts">My Posts</a></h3>'

    @staticmethod
    def ask_permission():
        return '<h1>HoloJournal</h1></br><h3>Do you give permission to get your Facebook data?</br> <a href="/myposts?permission=yes">Yes</a> / <a href="/">No</a><h3>'

    @classmethod
    def my_posts(cls, limit: int = 10):
        # Check if user has given permission
        try:
            if 'permission' in request.args and request.args['permission'] == 'yes':
                data = cls.meta_handler.fetch_data('me/posts', {'limit': limit})  # Fetch the last 10 posts

                df = DataManager.convert_to_dataframe(data)  # Convert the data to a DataFrame

                if df is not None:
                    return df.head().to_json(orient='records')
                else:
                    return jsonify(data)  # Return the original data, which might contain an error message
            else:
                # Redirect to permission asking route
                return redirect("/ask_permission", code=302)
        except Exception as e:
            Log.error(f"Failed to retrieve posts: {e}")

    @classmethod
    def classify_by_topic(cls):
        pass
