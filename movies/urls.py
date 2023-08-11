from django.urls import path
from .views import movie_list, movie_detail, movie_create
from . import views


app_name = 'movies'

# defining URL patterns for **MOVIES** app
urlpatterns = [
    # Path for list of movies
    path('', movie_list, name='movie_list'),
    # Path for details of a SINGLE movie
    path('<int:pk>/', movie_detail, name='movie_detail'),
    # Path for creating a **NEW** movie
    path('new/', movie_create, name='movie_create'),
    # Path for Registration
    path('register/', views.register, name='register'),
    # Path for Login
    path('login/', views.user_login, name='user_login'),
    # Path fot Logout
    path('logout/', views.user_logout, name='user_logout'),
    # Path to User Profile
    path('user_profile/', views.user_profile, name='user_profile'),
    # Path to Movie Search
    path('search/', views.search_movies, name='search_movies'),
]
