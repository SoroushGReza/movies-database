from django.urls import path
from .views import movie_list, approve_review, user_reviews
from .views import get_recent_searches, clear_search_history, delete_review
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'movies'


# URL patterns for "Movies" app
urlpatterns = [
    # Movie list page
    path('', movie_list, name='movie_list'),

    # Movie overview
    path(
        'overview/<int:movie_id>/',
        views.movie_overview,
        name='movie_overview',
    ),

    # Registration
    path('register/', views.register, name='register'),

    # Login
    path('login/', views.user_login, name='user_login'),

    # Logout
    path('logout/', views.user_logout, name='user_logout'),

    # User Profile
    path('user_profile/', views.user_profile, name='user_profile'),

    # Delete User Account
    path('delete_account/', views.delete_account, name='delete_account'),

    # User reviews
    path('user_reviews/', user_reviews, name='user_reviews'),

    # My reviews
    path('user_profile/my_reviews/', views.my_reviews, name='my_reviews'),

    # Delete user review ( As User )
    path(
        'delete_review/<int:review_id>/',
        views.delete_review, name='delete_review'
    ),

    # Edit User Review
    path(
        'edit_review/<int:review_id>/',
        views.edit_review, name='edit_review'
    ),

    # Movie Search
    path('search/', views.search_movies, name='search_movies'),

    # Clear search history
    path(
        'clear_search_history/',
        views.clear_search_history,
        name='clear_search_history',
    ),

    # Get recent searches
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

    # Contact
    path('contact/', views.contact, name='contact'),
]
