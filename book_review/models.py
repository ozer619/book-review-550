from book_review import db

class User(db.Model):
    __tablename__= "users"
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True,nullable=False)
    password_hash = db.Column(db.String(128),nullable=False)

    def __repr__(self):
        return '<User {}>'.format(self.username)  
        