from django.db import models
from django.contrib.auth.models import User


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
