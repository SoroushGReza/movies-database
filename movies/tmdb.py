import requests
from env import TMDB_API_KEY
import os

# TMDB_API_KEY = os.environ.get("TMDB_API_KEY")


def get_movies_from_tmdb():
    url = "https://api.themoviedb.org/3/movie/popular"
    querystring = {"api_key": TMDB_API_KEY, "language": "en-US", "page": "1"}
    response = requests.request("GET", url, params=querystring)
    return response.json()


def get_movie_trailer(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/videos"
    querystring = {"api_key": TMDB_API_KEY, "language": "en-US"}
    response = requests.request("GET", url, params=querystring)
    trailers = response.json().get('results', [])
    # Return the first trailer if available
    return trailers[0]['key'] if trailers else None


# Get movie title (User Reviews in Profile page)
def get_movie_title(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    querystring = {"api_key": TMDB_API_KEY, "language": "en-US"}
    response = requests.request("GET", url, params=querystring)
    data = response.json()
    return data.get("title", "Unknown")
