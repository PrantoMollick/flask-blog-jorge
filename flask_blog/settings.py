import os
class Settings(object):
    SECRET_KEY = 'MYSECRET000000000'
    DEBUG = True
    DB_USERNAME = 'root'
    DB_PASSWORD = 'pranto'
    BLOG_DATABASE_NAME = 'jorge_flask_app'
    DB_HOST = os.getenv('IP', '127.0.0.1')
    DB_PORT = 5506
    DB_URI = "mysql+pymysql://%s:%s@%s:%s/%s" % (DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT, BLOG_DATABASE_NAME)
    SQLALCHEMY_DATABASE_URI = DB_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False



