from book_review import app
from flask import flash, jsonify, redirect, render_template, request


@app.route("/")
def index():
    return render_template("register.htm")
