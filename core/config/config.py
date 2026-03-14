import os

from dotenv import load_dotenv

load_dotenv()

MOVIE_API_URL = os.getenv('MOVIES_API_URL')
MOVIE_ACCESS_TOKEN = os.getenv('API_READ_ACCESS_TOKEN')