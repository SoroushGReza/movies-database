from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie, Genre, Review
from .forms import MovieForm
from .tmdb import get_movies_from_tmdb
from .env import TMDB_API_KEY
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


# Registration for Users
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Login after registration
            return redirect('movie_list')  # Redirect to movie list after Login
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


# Display of all movies
def movie_list(request):
    movies = get_movies_from_tmdb()
    print(movies)
    return render(
        request, 'movies/movie_list.html', {'movies': movies['results']}
    )


# Display of a SINGLE movie detail
def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'movies/movies_detail.html', {'movie': movie})


# Creation of a new movie
def movie_create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    # If request is nt POST, form is being displayed for 1st time
    else:
        # Create a empty form
        form = MovieForm()
    return render(request, 'movies/movie_form.html', {'form': form})
