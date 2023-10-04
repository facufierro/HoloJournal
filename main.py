# main.py
from flask import Flask
from utils.routes import Routes

app = Flask(__name__)

app.add_url_rule('/', 'index', Routes.index)
app.add_url_rule('/myposts', 'my_posts', Routes.my_posts)
app.add_url_rule('/ask_permission', 'ask_permission', Routes.ask_permission)

if __name__ == '__main__':
    app.run(debug=True)
