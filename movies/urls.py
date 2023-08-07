from django.urls import path
from .views import movie_list, movie_detail, movie_create

# defining URL patterns for **MOVIES** app
urlpatterns = [
    # Path for list of movies
    path('', movie_list, name='movie_list'),
    # Path for details of a SINGLE movie
    path('<int:pk>/', movie_detail, name='movie_detail'),
    # Path for creating a **NEW** movie
    path('new/', movie_create, name='movie_create'),
]
