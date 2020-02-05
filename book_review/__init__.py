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

# Set up database
engine = create_engine(os.getenv("DATABASE_URL")) 
db = scoped_session(sessionmaker(bind=engine))

from book_review import routes