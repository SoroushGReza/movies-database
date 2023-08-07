import requests
from .env import TMDB_API_KEY


def get_movies_from_tmdb():
    url = "https://api.themoviedb.org/3/movie/popular"
    querystring = {"api_key": "TMDB_API_KEY", "language": "en-US", "page": "1"}
    response = requests.request("GET", url, params=querystring)
    return response.json()
