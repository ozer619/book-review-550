from flask import Flask
from flask_migrate import Migrate
from sqlalchemy.orm import scoped_session, sessionmaker
import os
from sqlalchemy import create_engine


app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

from config import Config
app.config.from_object(Config)
from models import *
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL") or "sqlite:///book-review.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
db.create_all()



from book_review import routes