from book_review import db
from flask_login import UserMixin

class User(UserMixin,db.Model):
    __tablename__= "users"
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True,nullable=False)
    password_hash = db.Column(db.String(128),nullable=False)
    reviews = db.relationship("Review", back_populates="user")    

    def __repr__(self):
        return '<User {}>'.format(self.username)  
    
class Books(db.Model):
    __tabelname__='books'
  
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String(256), index=True , unique=True ,nullable=False)
    title = db.Column(db.String(150),nullable=False)
    author = db.Column(db.String(120),nullable=False)
    year = db.Column(db.Integer,nullable=False) 
    
    def __repr__(self):
        return '<Books {}>'.format(self.title)  
class Review(db.Model):
    __tabelname__='review'
    id=db.Column(db.Integer,primary_key=True)
    user_id=db.Column(db.Integer,db.ForeignKey("users.id"),nullable=False)
    book_id=db.Column(db.Integer,db.ForeignKey("books.id"),nullable=False)
    rating=db.Column(db.Integer,nullable=False)
    
    comment=db.Column(db.String(400),nullable=False)
    user=db.relationship("User", back_populates="reviews")

##db.session.query(User.username, Review.comment, Review.rating).filter_by(User.id=Review.user_id)import requests

