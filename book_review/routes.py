from book_review import app
from flask import flash, jsonify, redirect, render_template, request, url_for,session
from werkzeug.security import check_password_hash, generate_password_hash
from book_review.models import *
from book_review import db
from flask_login import login_required,current_user,login_user
from flask_session import Session

@app.route("/")
@login_required
def index():
    message="u are logged in"
    return render_template("apology.htm",message=message)

@app.route("/login",methods=["POST","GET"])
def login():
    session.clear()
    if request.method == "POST":
        message=""
        username=request.form.get("username")
        password=request.form.get("password")
        user=User.query.filter_by(username=username).first()
        if not user:
            message="username or password incorrect"
            return render_template("apology.htm",message=message)
        if not check_password_hash(user.password_hash,password):
            message="username or password incorrect"
            return render_template("apology.htm",message=message)
        login_user(user)
        # Redirect user to home page
        return redirect("/")
    else:
        return render_template("login.htm")

@app.route("/register",methods=["POST","GET"])
def register():
    """Register user"""
    if request.method == "POST":
        message=""
        username= request.form.get("username")
        password= request.form.get("password")
        if not password:
            message="missing password"
            return render_template("apology.htm",message=message)
        password=generate_password_hash(password)
        print(password)
        confirm_password=request.form.get("confirmation")
        if not username:
            message="missing username"
            return render_template("apology.htm",message=message)
        if not confirm_password:
            message="missing confirm-password"
            return render_template("apology.htm",message=message)
        if not request.form.get("password")==confirm_password:
            message="password and confirm-password field donot match"
            return render_template("apology.htm",message=message)

        new_user=User(username=username,password_hash=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect("/login")
    else:
        return render_template("register.htm")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")