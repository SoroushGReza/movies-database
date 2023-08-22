from django.contrib.auth.models import User
from django.test import TestCase
from .models import Review


class ReviewModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', password='12345')

    def test_review_creation(self):
        review = Review.objects.create(user=self.user, movie_id=12345, text="Great movie!", rating=4.5)
        self.assertEqual(review.text, "Great movie!")
        self.assertEqual(review.rating, 4.5)
