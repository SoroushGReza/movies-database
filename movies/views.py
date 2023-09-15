from django.shortcuts import render, get_object_or_404, redirect
from .models import SearchHistory, Review, UserProfile
from .tmdb import get_movies_from_tmdb, get_movie_trailer, get_movie_title
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
from .forms import ReviewForm, UserProfileForm
from .forms import VerifyDeleteUserForm, UserRegisterForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings


# Registration for Users
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # Save user after valid registration
            user = form.save()
            user.is_active = True
            user.save()  # save as active

            # Login user
            login(request, user)

            # Send membership confirmation email
            # user_email = form.cleaned_data.get('email')
            # subject = "Welcome to Movie Base!"
            # message = (
            #     "We are thrilled to have you on board!"
            #     "If you have any suggestions for improvements, "
            #     "we would love to hear your ideas.\n\n"
            #     "We also want to inform you that in Movie Base, "
            #     "our users are expected to keep a respectful manner "
            #     "in their reviews. And we expect that users don't post "
            #     "content unrelated to the movie that the review "
            #     "is written, as violations would result "
            #     "in your review being rejected"
            # )
            # try:
            #     send_mail(
            #         subject,
            #         message,
            #         settings.EMAIL_HOST_USER,
            #         [user_email],
            #         fail_silently=False,
            #     )
            # except Exception as e:
            #     raise
            # Redirect to movie_list page
            return redirect('movies:movie_list')
    else:
        form = UserRegisterForm()
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
    user_profile, created = UserProfile.objects.get_or_create(
        user=request.user
    )

    update_success = False
    current_email = request.user.email

    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(
            request.POST,
            request.FILES,
            instance=user_profile
        )
        password_form = PasswordChangeForm(request.user, request.POST)

        # Validate and save user details form
        if form.has_changed():
            if form.is_valid():
                form.save()
                update_success = True
            else:
                for field, errors in form.errors.items():
                    for error in errors:
                        if error != "This field is required.":
                            messages.error(request, error)

        # Validate and save profile form
        if profile_form.has_changed():
            if profile_form.is_valid():
                # Get the email from the profile form
                email = profile_form.cleaned_data.get('email')

                # Control if email has been updated
                email_unchanged = email == current_email if email else True

                # Update the user's email address if an email was provided
                if email:
                    request.user.email = email
                    request.user.save()

                profile_form.save()
                # New check to only set update success
                # if email has been changed
                if not email_unchanged:
                    update_success = True
            else:
                for field, errors in profile_form.errors.items():
                    for error in errors:
                        if error != "This field is required.":
                            messages.error(request, error)

        # Validate and save password form
        if password_form.has_changed():
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(
                    request, user
                )  # Update session with new password
                update_success = True
            else:
                for field, errors in password_form.errors.items():
                    for error in errors:
                        if error != "This field is required.":
                            messages.error(request, error)

        if update_success:
            messages.success(request, "Profile updated successfully")

        return redirect('movies:user_profile')
    else:
        form = CustomUserChangeForm(instance=request.user)
        profile_form = UserProfileForm(instance=user_profile)
        password_form = PasswordChangeForm(request.user)

    return render(
        request,
        'profile/user_profile.html',
        {
            'form': form,
            'profile_form': profile_form,
            'password_form': password_form
        }
    )


# Delete User Account
def delete_account(request):
    if request.method == 'POST':
        form = VerifyDeleteUserForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data.get('password')
            user = authenticate(
                request,
                username=request.user.username,
                password=password
            )
            if user is not None:
                user.delete()
                logout(request)

                messages.success(
                    request,
                    "Your account has been deleted successfully."
                )

                return redirect('movies:register')
            else:
                messages.error(request, "Incorrect password")
    else:
        form = VerifyDeleteUserForm()

    return render(request, 'profile/user_profile.html', {'form': form})


# My Reviews
@login_required
def my_reviews(request):
    user = request.user
    reviews = Review.objects.filter(
        user=request.user, approved=True
    ).order_by('-date_created')

    # Fetch movie titles
    for review in reviews:
        review.movie_title = get_movie_title(review.movie_id)

    return render(
        request,
        'profile/my_reviews.html',
        {'reviews': reviews}
    )


# User reviews ( As User )
@login_required
def user_reviews(request):
    user = request.user
    reviews = Review.objects.filter(
        user=request.user, approved=True
    ).order_by('-date_created')

    # Fetch movie titles
    for review in reviews:
        review.movie_title = get_movie_title(review.movie_id)

    return render(
        request,
        'profile/user_profile.html',
        {'reviews': reviews}
    )


# Delete reviews ( As User )
@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id, user=request.user)
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        review.delete()
        return JsonResponse({'status': 'success'})
    else:
        review.delete()
        return redirect('movies:user_profile')


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


# Movie Overview
def movie_overview(request, movie_id):
    movie = get_movie_by_id(movie_id)
    trailer_key = get_movie_trailer(movie_id)

    # Get approved reviews for movie
    reviews = Review.objects.filter(
        movie_id=movie_id, status='approved'
    )
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.movie_id = movie_id
            review.save()

            return redirect('movies:movie_overview', movie_id=movie_id)
    else:
        form = ReviewForm()
    context = {
        'movie': movie,
        'form': form,
        'reviews': reviews,  # Include approved reviews
        'trailer_key': trailer_key,  # Include Trailer
    }
    return render(request, 'movies/movie_overview.html', context)


# Managing Reviews
@user_passes_test(lambda user: user.is_staff)
def manage_reviews(request):
    # Get all reviews that is pending
    pending_reviews = Review.objects.filter(status='pending')

    return render(request, 'movies/manage')


# Review approval
@user_passes_test(lambda user: user.is_staff)
def approve_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    review.approved = True
    review.status = 'approved'
    review.save()
    return HttpResponseRedirect(
        reverse('movies:movie_overview', args=[review.movie_id])
    )


# Reject Review
@user_passes_test(lambda user: user.is_staff)
def reject_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    review.status = 'rejected'
    review.save()
    return HttpResponseRedirect(
        reverse('movies:movie_overview', args=[review.movie_id])
    )


# Contact
def contact(request):
    return render(request, 'contact/contact.html')
