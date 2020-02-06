from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy("sqlite:///book-review.db")

class User(db.Model):
    __tabelname__="users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True,nullable=False)
    password_hash = db.Column(db.String(128),nullable=False)

    def __repr__(self):
        return '<User {}>'.format(self.username)  