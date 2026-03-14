from core.models import Movie
from core.db import db

class MovieService:
  
  @staticmethod
  def get_all_movies():
    return Movie.query.all()
  
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