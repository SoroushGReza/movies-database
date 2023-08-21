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


# Movie Genre
class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Search History model
class SearchHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # User Reference
    query = models.CharField(max_length=200)  # Search query
    timestamp = models.DateTimeField(auto_now_add=True)  # Timestamp of search

    def __str__(self):
        return f'{self.user.username}: {self.query}'

    class Meta:
        ordering = ['-timestamp']  # Order by most recent search
