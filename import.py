import csv
from book_review import db
from flask import session
from book_review.models import Books

file=open("books.csv","r")
reader=csv.reader(file)
info=list(reader)

i=0

for book in info:
    if i==0:
        i=i+1
        continue
    else:
        kitab=Books(isbn=book[0],title=book[1],author=book[2],year=book[3])
        db.session.add(kitab)
        db.session.commit()
