from django.db import models


# Movie model
class Movie(models.Model):
    title = models.CharField(max_length=200)  # Movie title
    genre = models.CharField(max_length=100)  # Movie Genre
    release_date = models.DateField()  # Movie Release date
    rating = models.DecimalField(max_digits=5, decimal_places=1)  # Rating
    description = models.TextField()  # Movie Description
