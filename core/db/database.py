from flask import Flask
from .config import db

DATABASE_NAME = "movies-collection.db"

class SQLiteDb():
  def __init__(self, app: Flask):
    self.app = app
    # configure the SQLite database, relative to the app instance folder
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DATABASE_NAME}"  
    # initialize the app with the extension
    db.init_app(app)
    self.db = db
  
  def create_table(self):
    with self.app.app_context():
        self.db.create_all()