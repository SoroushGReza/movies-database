from django.shortcuts import render, get_object_or_404
from .models import Movie, Genre, Review
from .forms import MovieForm
from .tmdb import get_movies_from_tmdb
from .env import TMDB_API_KEY


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
