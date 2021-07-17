from flask import Flask
from flask_blog import settings
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object('flask_blog.settings.Settings')

db = SQLAlchemy(app)
from flask_blog.blog import views
from flask_blog.author import views
