from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5

from core.db import SQLiteDb
from core.services import MovieService, IMDBMovieService
from core.forms import UpdateMovieForm, AddMovieForm
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CREATE DB
db_instance = SQLiteDb(app)
imdb_instance = IMDBMovieService()

# CREATE TABLE
db_instance.create_table()

@app.route("/")
def home():
    movies = MovieService.get_all_movies()
    return render_template("index.html", movies=movies)

@app.route("/edit/<int:id>", methods=["POST", "GET"])
def edit(id: int):
    form = UpdateMovieForm()
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

@app.route("/add", methods=["POST", "GET"])
def add():
    form = AddMovieForm()
    if form.validate_on_submit():
        title = form.title.data
        movies = imdb_instance.get_movies(title)
        return render_template("select.html", movies=movies)
    return render_template("add.html", form=form)

@app.route("/movie_detail/<int:movie_id>")
def movie_detail(movie_id: int):
    movie_detail = imdb_instance.get_movie_detail(id=movie_id)
    with app.app_context():
        title = movie_detail["title"]
        year = int(movie_detail["release_date"].split("-")[0])
        overview = movie_detail["overview"]
        img_url = f"https://image.tmdb.org/t/p/w500{movie_detail['poster_path']}"
        
        print(f"Title: {title}, Year: {year}, Overview: {overview}, Image URL: {img_url}")
        id = MovieService.add_movie(title=title, year=year, description=overview, img_url=img_url)
    return redirect(url_for("edit", id=id))
        
if __name__ == '__main__':
    app.run(debug=True)
