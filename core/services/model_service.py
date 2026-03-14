from core.models import Movie
from core.db import db

class MovieService:
  
  @staticmethod
  def get_all_movies():
    result = db.session.execute(db.select(Movie).order_by(Movie.rating),)
    all_movies = result.scalars().all() # convert ScalarResult to Python List

    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    
    return all_movies
  
  @staticmethod
  def update_movie(id: int, new_rating: str, new_review: str):
    movie_to_update = Movie.query.get(id)
    movie_to_update.rating = new_rating
    movie_to_update.review = new_review
    db.session.commit()
  
  @staticmethod
  def delete_movie(id: int):
    movie_to_delete = Movie.query.get(id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    
  @staticmethod
  def add_movie(title: str, year: int, description: str, img_url: str):
    new_movie = Movie(title=title, year=year, description=description, img_url=img_url)
    db.session.add(new_movie)
    db.session.commit()
    db.session.refresh(new_movie)

    
    return new_movie.id