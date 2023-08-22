from django.contrib.auth.models import User
from django.test import TestCase
from .models import Review
from django.urls import reverse


# Review Model Test
class ReviewModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', password='12345')

    def test_review_creation(self):
        review = Review.objects.create(
            user=self.user, movie_id=12345, text="Great movie!", rating=4.5
        )
        self.assertEqual(review.text, "Great movie!")
        self.assertEqual(review.rating, 4.5)


# Review Form Test
class ReviewFormTest(TestCase):
    def test_review_form_in_movie_overview(self):
        movie_id = 12345
        response = self.client.get(reverse('movie_overview', args=[movie_id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Submit Review')
        self.assertTemplateUsed(response, 'movies/movie_overview.html')
