import requests
import time

from core import config

class IMDBMovieService:
  def __init__(self):
    self.api_url = config.MOVIE_API_URL
    self.access_token = config.MOVIE_ACCESS_TOKEN
    self.timeout = 15  # seconds
    self.max_retries = 3

  def _make_request_with_retry(self, url, params=None, headers=None, retry_count=0):
    """Helper method to make requests with retry logic and timeout"""
    try:
      response = requests.get(url, params=params, headers=headers, timeout=self.timeout)
      response.raise_for_status()  # Raise exception for bad status codes
      return response
    except requests.exceptions.Timeout:
      print(f"Request timeout (attempt {retry_count + 1}/{self.max_retries}): {url}")
      if retry_count < self.max_retries - 1:
        time.sleep(2 ** retry_count)  # Exponential backoff
        return self._make_request_with_retry(url, params, headers, retry_count + 1)
      raise
    except requests.exceptions.ConnectionError as ex:
      print(f"Connection error (attempt {retry_count + 1}/{self.max_retries}): {ex}")
      if retry_count < self.max_retries - 1:
        time.sleep(2 ** retry_count)  # Exponential backoff
        return self._make_request_with_retry(url, params, headers, retry_count + 1)
      raise
    except Exception as ex:
      print(f"Error: {ex}")
      raise

  def get_movies(self, movie_title: str):
    endpoint = "search/movie"
    params = {
      'query': movie_title,
      'include_adult': 'false',
      'language': 'en-US',
      'page': 1
    }
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {self.access_token}",
    }
    try:
      response = self._make_request_with_retry(f"{self.api_url}/{endpoint}", params=params, headers=headers)
      movies = response.json()["results"]
      return movies
    except Exception as ex:
        print(f"Failed to get movies after {self.max_retries} attempts: {ex}")
        return []
  
  def get_movie_detail(self, id: int):
    """
      Get movie details by id
      param id: int - movie id
      return: dict - movie details
    """
    endpoint = f"movie/{id}"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {self.access_token}",
    }
    try:
      response = self._make_request_with_retry(f"{self.api_url}/{endpoint}", headers=headers)
      movie_detail = response.json()
      print(f"Movie detail: {movie_detail}")
      return movie_detail
    except Exception as ex:
        print(f"Failed to get movie detail after {self.max_retries} attempts: {ex}")
        return {}
    