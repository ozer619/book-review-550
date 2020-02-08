from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
app = Flask(__name__)


from config import Config
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

login_manager=LoginManager()
login_manager.login_view='routes.login'
login_manager.init_app(app)

from book_review import models

@login_manager.user_loader
def load_user(user_id):
    return user.query.get(int(user_id))

from book_review import routes
