from django.shortcuts import render, get_object_or_404, redirect
from .models import Genre, SearchHistory, Review
from .tmdb import get_movies_from_tmdb
from .env import TMDB_API_KEY
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from django.http import JsonResponse
import requests
from .forms import ReviewForm


# Registration for Users
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Login after registration
            return redirect(
                'movies:user_profile'
            )  # Redirect to profile after Login
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
            messages.success(
                request,
                'Profile information updated succesfully!'
            )
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
    query = request.GET.get('query')
    if query:
        # Save search history
        if request.user.is_authenticated:
            search_history = SearchHistory(user=request.user, query=query)
            search_history.save()

    url = (
        f"https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}"
        f"&query={query}"
    )
    response = requests.get(url)
    movies = response.json()['results']

    # Get 5 last searches from database
    recent_searches = SearchHistory.objects.all().order_by('-timestamp')[:5]

    return render(
        request,
        'movies/search_results.html',
        {'movies': movies, 'recent_searches': recent_searches}
    )


# Get movie by ID
def get_movie_by_id(movie_id):
    url = (
        f"https://api.themoviedb.org/3/movie/{movie_id}"
        f"?api_key={TMDB_API_KEY}"
    )
    response = requests.get(url)
    return response.json()


# Get recent seaarches
@login_required
def get_recent_searches(request):
    # Get the 5 last searches from loged in user
    recent_searches = SearchHistory.objects.filter(
        user=request.user
    ).order_by('-timestamp')[:5]
    # Make a search list
    search_queries = [search.query for search in recent_searches]
    # Return as JSON
    return JsonResponse({'recent_searches': search_queries})


# Clear Search History
@login_required
def clear_search_history(request):
    # Delete search history for the logged-in user from the database
    SearchHistory.objects.filter(user=request.user).delete()
    return JsonResponse({'status': 'success'})


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


# Movie Overview
def movie_overview(request, movie_id):
    movie = get_movie_by_id(movie_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.movie_id = movie_id
            review.save()
    else:
        form = ReviewForm()
    return render(
        request, 'movies/movie_overview.html', {'movie': movie, 'form': form}
    )


# Review approval
@user_passes_test(lambda user: user.is_staff)
def approve_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    review.approved = True
    review.save()
    return redirect('movies:movie_overview', movie_id=review.movie_id)
