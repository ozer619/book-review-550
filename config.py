from book_review import app
from sqlalchemy import create_engine
import os

class Config(object):
    # Configure session to use filesystem
    app.config["SESSION_PERMANENT"] = False
    app.config["SESSION_TYPE"] = "filesystem"
    Session(app)
    # Set up database
    engine = create_engine(os.getenv("DATABASE_URL"))
    

