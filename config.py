import os
basedir = os.path.abspath(os.path.dirname(__file__))
class Config(object):
    # Configure session to use filesystem
    SESSION_PERMANENT = False
    SESSION_TYPE = "filesystem"

    # Ensure templates are auto-reloaded
    TEMPLATES_AUTO_RELOAD = True

    # set up database
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL") or "sqlite:///" + os.path.join(basedir, 'book-review.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #set SECRET KEY 
    SECRET_KEY="nou"
