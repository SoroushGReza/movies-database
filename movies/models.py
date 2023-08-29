from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone


# User Profile
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(
        upload_to='profile_images/', default='default.jpg'
    )

    def __str__(self):
        return self.user.username


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


# User Reviews & User Rating

STATUS_CHOICES = [
    ('pending', 'Pending'),
    ('approved', 'Approved'),
    ('rejected', 'Rejected'),
]


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie_id = models.IntegerField(default=0)
    text = models.TextField()
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    date_created = models.DateTimeField(default=timezone.now)
    approved = models.BooleanField(default=False)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='pending',
    )

    def __str__(self):
        return self.text[:50]

    def rating_as_stars(self):
        rating_int = int(round(self.rating))
        return '★' * rating_int
