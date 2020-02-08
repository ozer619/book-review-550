from book_review import app
from flask import flash, jsonify, redirect, render_template, request, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from book_review.models import User
from book_review import db

@app.route("/")
def index():
    return render_template("login.htm")

@app.route("/login")
def login():
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
        return redirect(url_for("login"))
    else:
        return render_template("register.htm")
        