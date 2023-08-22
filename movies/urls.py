from django.urls import path
from .views import movie_list, movie_detail
from .views import get_recent_searches, clear_search_history
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'movies'


# defining URL patterns for **MOVIES** app
urlpatterns = [
    # Path for list of "News"  in movie_list.html
    path('', movie_list, name='movie_list'),

    # Path for details of a SINGLE movie
    path('<int:pk>/', movie_detail, name='movie_detail'),

    # path for movie overview
    path(
        'overview/<int:movie_id>/',
        views.movie_overview,
        name='movie_overview',
    ),

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

    # Path to Clear search history
    path(
        'clear_search_history/',
        views.clear_search_history,
        name='clear_search_history',
    ),

    # Path to get recent searches
    path(
        'get_recent_searches/',
        get_recent_searches,
        name='get_recent_searches',
    ),

    # Approving review
    path(
        'approve_review/<int:review_id>/',
        views.approve_review, name='approve_review',
    ),

]
