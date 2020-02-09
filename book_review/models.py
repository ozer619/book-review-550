from book_review import db
from flask_login import UserMixin

class User(UserMixin,db.Model):
    __tablename__= "users"
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True,nullable=False)
    password_hash = db.Column(db.String(128),nullable=False)

    def __repr__(self):
        return '<User {}>'.format(self.username)  
    
class Books(db.Model):
    __tabelname__='books'
  
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.BigInteger, index=True , unique=True ,nullable=False)
    title = db.Column(db.String(150),nullable=False)
    author = db.Column(db.String(120),nullable=False)
    year = db.Column(db.Integer,nullable=False) 

    def __repr__(self):
        return '<Books {}>'.format(self.title)  
    
