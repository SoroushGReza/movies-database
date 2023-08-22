from django.contrib.auth.models import User
from django.test import TestCase
from .models import Movie, Review


# Movie model test
class MovieModelTest(TestCase):
    def test_create_movie(self):
        movie = Movie.objects.create(
            title="Waist Deep",
            genre="Action, Drama",
            release_date="2006-06-23",
            rating=5.9,
            description=(
                "An ex-convict (Tyrese Gibson) gets tangled up with a "
                "gang after his car is hijacked with his son inside."
            )
        )
        self.assertEqual(movie.title, "Waist Deep")
        self.assertEqual(movie.genre, "Action, Drama")


# Review Model test
class ReviewModelTest(TestCase):
    def setUp(self):
        # Create a user and a movie for testing
        self.user = User.objects.create(username='testuser')
        self.movie = Movie.objects.create(title='Inception', genre='Sci-Fi')

    def test_review_creation(self):
        # Write a review and verify
        review = Review.objects.create(
            movie=self.movie, user=self.user, review_text='Great movie!'
        )
        self.assertEqual(review.movie, self.movie)
        self.assertEqual(review.user, self.user)
        self.assertEqual(review.review_text, 'Great movie!')
        self.assertEqual(review.approved, False)
