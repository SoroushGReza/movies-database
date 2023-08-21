from django.test import TestCase
from .models import Movie


class MovieModelTest(TestCase):
    def test_create_movie(self):
        movie = Movie.objects.create(
            title="Waist Deep",
            genre="Action, Drama",
            release_date="2006-06-23",
            rating=5.9,
            description="An ex-convict (Tyrese Gibson) gets tangled up with a gang after his car is hijacked with his son inside."
        )
        self.assertEqual(movie.title, "Waist Deep")
        self.assertEqual(movie.genre, "Action, Drama")
