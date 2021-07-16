from flask import Flask

app = Flask(__name__)

app.config.from_object('settings')

from flask_blog.home import views
