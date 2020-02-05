from config import Config
from flask import Flask, session
from flask_session import Session
from flask_migrate import Migrate
from sqlalchemy.orm import scoped_session, sessionmaker
import os

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

app.config.from_object(Config)
migrate = Migrate(app, db)
db = scoped_session(sessionmaker(bind=engine))

from book_review import routes