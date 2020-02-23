from book_review import app
from flask import flash, jsonify, redirect, render_template, request, url_for, session

from werkzeug.security import check_password_hash, generate_password_hash
from book_review.models import *

from book_review import db
from flask_login import login_required, current_user, login_user, logout_user
from flask_session import Session
from sqlalchemy import or_
import requests
import os

@app.route("/")
@login_required
def index():
    return redirect("search")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        message = ""
        username = request.form.get("username")
        password = request.form.get("password")
        user = User.query.filter_by(username=username).first()
        if not user:
            message = "username or password incorrect"
            return render_template("apology.htm", message=message)
        if not check_password_hash(user.password_hash, password):
            message = "username or password incorrect"
            return render_template("apology.htm", message=message)

        login_user(user, remember=False)
        session["user_id"] = user.id
        # Redirect user to home page
        return redirect("/")
    else:
        return render_template("login.htm")


@app.route("/register", methods=["POST", "GET"])
def register():
    """Register user"""
    if request.method == "POST":
        message = ""
        username = request.form.get("username")
        password = request.form.get("password")
        if not password:
            message = "missing password"
            return render_template("apology.htm", message=message)
        password = generate_password_hash(password)
        print(password)
        confirm_password = request.form.get("confirmation")
        if not username:
            message = "missing username"
            return render_template("apology.htm", message=message)
        if not confirm_password:
            message = "missing confirm-password"
            return render_template("apology.htm", message=message)
        if not request.form.get("password") == confirm_password:
            message = "password and confirm-password field donot match"
            return render_template("apology.htm", message=message)

        new_user = User(username=username, password_hash=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect("/login")
    else:
        return render_template("register.htm")


@app.route("/logout")
@login_required
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()
    logout_user()

    # Redirect user to login form
    return redirect("/")


@app.route("/search", methods=["POST", "GET"])
@login_required
def search():
    if request.method == "POST":
        flag = 1
        search = request.form.get("search")
        books = Books.query.filter(or_(Books.author.like('%' + search + '%'),
                                       Books.title.like('%' + search + '%'),
                                       Books.isbn.like('%' + search + '%'))).all()
        if not books:
            message = "no results found"
            return render_template("apology.htm", message=message)

        return render_template("search.htm", flag=flag, books=books)
    else:
        flag = 0
        return render_template("search.htm", flag=flag)


@app.route('/review/<int:book_id>', methods=["GET"])
@login_required
def review(book_id):
 
    kitab = Books.query.get(book_id)
    session['book_id'] = book_id
    review_of_book = Review.query.filter_by(book_id=book_id)
    isbns=db.session.query(Books.isbn).filter(Books.id==book_id).all()
    isbns=str(isbns[0][0])

    review_of_book = db.session.query(User, Review.comment, Review.rating).filter(
        Review.book_id == session["book_id"]).join(Review, User.id == Review.user_id).all()
    if len(isbns)==10:
        res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key":"mA2E8ydIgLk4hEdtw57DXA", "isbns":isbns }).json()
        
    if(len(isbns)==9):
        res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key":"mA2E8ydIgLk4hEdtw57DXA", "isbns":'0' + isbns }).json()
    if(len(isbns)==8):
        res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key":"mA2E8ydIgLk4hEdtw57DXA", "isbns":'00' + isbns }).json()
    if(len(isbns)==7):
        res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key":"mA2E8ydIgLk4hEdtw57DXA", "isbns":'000' + isbns }).json()    
        
    
  
    return render_template("review.htm", kitab=kitab, book_id=book_id, review_of_book=review_of_book,res=res)


@app.route('/review', methods=["POST"])
@login_required
def review_1():
    book_id = session['book_id']

    rating_b = request.form.get("rating_b")
    rating_t = request.form.get("rating_t")

    if not rating_b:
        message = "Rating not provided"
        return render_template("apology.htm", message=message)
    if not rating_t:
        message = "comment not provided"
        return render_template("apology.htm", message=message)
    if (rating_b != '1' and rating_b != '2' and rating_b != '3' and rating_b != '4' and rating_b != '5'):
        message = "invalid rating"
        return render_template("apology.htm", message=message)

    else:
        new_rating = Review(user_id=current_user.id,
                            book_id=book_id, rating=rating_b, comment=rating_t)
        db.session.add(new_rating)
        db.session.commit()

    return redirect(url_for('review', book_id=session["book_id"]))

 