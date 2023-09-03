from django.urls import path
from .views import movie_list, approve_review, user_reviews
from .views import get_recent_searches, clear_search_history, delete_review
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'movies'


# defining URL patterns for **MOVIES** app
urlpatterns = [
    # Path for list of "News"  in movie_list.html
    path('', movie_list, name='movie_list'),

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
    path('user_profile/', views.user_reviews, name='user_profile'),

    # User reviews
    path('user_reviews/', user_reviews, name='user_reviews'),

    # My reviews
    path('user_profile/my_reviews/', views.my_reviews, name='my_reviews'),

    # Delete user review ( As User )
    path(
        'delete_review/<int:review_id>/',
        views.delete_review, name='delete_review'
    ),


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
        approve_review,
        name='approve_review',
    ),
    # Reject Review
    path(
        'reject_review/<int:review_id>/',
        views.reject_review,
        name='reject_review',
    ),

]
