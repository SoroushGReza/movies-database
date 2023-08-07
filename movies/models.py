from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


# Movie model
class Movie(models.Model):
    title = models.CharField(max_length=200)  # Movie title
    genre = models.CharField(max_length=100)  # Movie Genre
    release_date = models.DateField()  # Movie Release date
    rating = models.DecimalField(max_digits=5, decimal_places=1)  # Rating
    description = models.TextField()  # Movie Description


# Review Model
class Review(models.Model):
    movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE, related_name='reviews'
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reviews'
    )
    review_text = models.TextField(
        max_length=1000, help_text="Enter your review here."
    )
    date = models.DateField(auto_now_add=True)


# Rating Model
class Rating(models.Model):
    movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE, related_name='ratings'
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='ratings'
    )
    rating_value = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )  # Rating values between 1 to 5
    date = models.DateTimeField(auto_now_add=True)


# User list  Model
class UserList(models.Model):
    """
    Represents Users list of movies
    """
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='lists'
    )
    movies = models.ManyToManyField(Movie, related_name='lists')
