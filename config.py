from book_review import app

import os
from flask import session
from flask_session import Session

class Config(object):
    # Configure session to use filesystem
    app.config["SESSION_PERMANENT"] = False
    app.config["SESSION_TYPE"] = "filesystem"
    # Ensure templates are auto-reloaded
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    Session(app)
    
  
    

