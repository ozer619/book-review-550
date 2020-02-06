from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

from config import Config
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
#db.init_app(app)
#db.create_all()

from book_review import routes, models
