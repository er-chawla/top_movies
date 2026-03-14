from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

from core import SQLiteDb
from core.models import Movie
from core.services import MovieService
from core.forms import MovieForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CREATE DB
db_instance = SQLiteDb(app)

# CREATE TABLE
db_instance.create_table()

@app.route("/")
def home():
    movies = MovieService.get_all_movies()
    return render_template("index.html", movies=movies)

@app.route("/edit/<int:id>", methods=["POST", "GET"])
def edit(id: int):
    form = MovieForm()
    if form.validate_on_submit():
        new_rating = form.rating.data
        new_review = form.review.data
        
        print(f"New rating: {new_rating}, New review: {new_review}")
        with app.app_context():
            MovieService.update_movie(id=id, new_rating=new_rating, new_review=new_review)
        return redirect(url_for("home"))
    return render_template("edit.html", form=form)

@app.route("/delete/<int:id>")
def delete(id: int):
    with app.app_context():
        MovieService.delete_movie(id=id)
    return redirect(url_for("home"))

if __name__ == '__main__':
    app.run(debug=True)
