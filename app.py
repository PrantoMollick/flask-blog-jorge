from flask_blog import app
app.config.from_object('flask_blog.settings.Settings')

if __name__== '__main__':
    app.run()
