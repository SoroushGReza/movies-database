from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


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


# Reviews & User Rating
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie_id = models.IntegerField(default=0)
    text = models.TextField()
    rating = models.FloatField(default=0.0)

    def __str__(self):
        return self.text[:50]
