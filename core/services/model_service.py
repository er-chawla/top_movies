from core.models import Movie
from core.db import db

class MovieService:
  
  @staticmethod()
  def get_all_movies():
    return Movie.query.all()
  
  