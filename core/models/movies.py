from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import mapped_column, Mapped

from core.db import db


"""
  Movie Table Orm
  
  Columns Name
  
  # id 
  # title 
  # year 
  # description 
  # rating 
  # ranking
  # review
  # img_url

"""


class Movie(db.Model):
  __tablename__ = "movie"
  
  id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
  title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
  year: Mapped[int] = mapped_column(Integer, nullable=False)
  description: Mapped[str] = mapped_column(String(800), nullable=True)
  rating: Mapped[float] = mapped_column(Float, nullable=True)
  ranking: Mapped[int] = mapped_column(Integer, nullable=False)
  review: Mapped[str] = mapped_column(String(250), nullable=True)
  img_url: Mapped[str] = mapped_column(String(250), nullable=True)