from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie, Genre, Review
from .forms import MovieForm
from .tmdb import get_movies_from_tmdb
from .env import TMDB_API_KEY
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import requests


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


# User Login
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to movielist after login is completed
            return redirect('movies:movie_list')
        else:
            messages.error(request, 'Incorrect username or  password.')
            form = AuthenticationForm(request.POST)
    else:
        form = AuthenticationForm()  # Create empty form
    return render(request, 'login/login.html', {'form': form})


# User Logout
def user_logout(request):
    logout(request)
    return redirect('movies:movie_list')


# User Profile
@login_required
def user_profile(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        password_form = PasswordChangeForm(request.user, request.POST)

        if form.is_valid() and password_form.is_valid():
            form.save()
            user = password_form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Profile information updated succesfully!')
            return redirect('movies:user_profile')
    else:
        form = CustomUserChangeForm(instance=request.user)
        password_form = PasswordChangeForm(request.user)
    return render(
        request,
        'profile/user_profile.html',
        {'form': form, 'password_form': password_form}
    )


# Searching for movie
def search_movies(request):
    query = request.GET.get('query', '')
    url = f"https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&query={query}"
    response = requests.get(url)
    movies = response.json().get('results', [])
    return render(request, 'movies/search_results.html', {'movies': movies})


# User Change Form
class CustomUserChangeForm(UserChangeForm):
    password = None  # To not shoe password

    class Meta:
        model = User
        fields = ('username', 'email')


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
