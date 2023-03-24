# Databases and with SQLite and SQLAlchemy

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from typing import Callable

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# BY-PASSING THE INTEGRITY ERROR:
class MySQLAlchemy(SQLAlchemy):
    Column: Callable
    String: Callable
    Integer: Callable
    Float: Callable


# CREATE SQLITE DATABASE:
db = MySQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)


# db.drop_all()  # Reset database if needed


@app.route('/', methods=["GET", "POST"])
def home():
    all_books = db.session.query(Book).all()
    return render_template('index.html', books=all_books)


@app.route('/delete')
def delete():
    book_id = request.args.get('id')
    # DELETE RECORD:
    book_to_delete = Book.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        # new_book_dict = {
        #     "title": request.form['title'],
        #     "author": request.form['author'],
        #     "rating": int(request.form['rating'])
        # }
        # all_books.append(new_book_dict)
        new_book = Book(title=request.form['title'], author=request.form['author'], rating=int(request.form['rating']))
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')


@app.route('/edit', methods=["POST", "GET"])
def edit():
    if request.method == "POST":
        # UPDATE RECORD:
        book_id = request.form["id"]
        book_to_update = Book.query.get(book_id)
        book_to_update.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for('home'))
    book_id = request.args.get('id')
    book_selected = Book.query.get(book_id)
    return render_template('edit.html', book=book_selected)


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
