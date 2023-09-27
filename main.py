import requests
import pandas as pd
from flask import Flask, request, jsonify

app = Flask(__name__)


ACCESS_TOKEN = 'EAAD5IZCrp7ZCMBO3UO9I7XS8t0tGEeP6Bxl95SZB7H7EEFQJaGo0w9dw64jwcgbtCbe3DwHVgYWOHUpRzigSSBvuNcaFQghSOy7MRBNZAtJh3euagfLWE0j2LVMDdHSB4gBZCw5j2GrWmZCSn20taJXt9Euq1J7sfVY9Mo4IrZAEeKCxcaPyy4NrdueZAW8K7DrgPyxX7mwhspNN82GTB1eE46tdIU3p9Lz8z8kmsVqWr8AXJQbLn8SohkeFuK7NFOZCS6SaBKugZD'  # Replace with your access token


def fetch_facebook_data(endpoint, params={}):
    BASE_URL = 'https://graph.facebook.com/v12.0/'  # Adjust the version if needed
    params['access_token'] = ACCESS_TOKEN
    response = requests.get(BASE_URL + endpoint, params=params)
    return response.json()


@app.route('/')
def index():
    return "Welcome to our project!"


@app.route('/myposts')
def my_posts():
    data = fetch_facebook_data('me/posts', {'limit': 10})  # Fetch the last 10 posts

    # Check if data contains the 'data' key
    if 'data' in data:
        df = pd.DataFrame(data['data'])
        # For demonstration purposes, let's just return the first 5 rows as JSON
        return df.head().to_json(orient='records')
    else:
        return jsonify(data)  # Return the original data, which might contain an error message


if __name__ == '__main__':
    app.run(debug=True)
