from django.test import TestCase
from django.contrib.auth.models import User
from .models import Review
from django.urls import reverse


# Review Model Test
class ReviewModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', password='12345')
        self.movie_id = 4133  # Movie Blow

    def test_review_creation(self):
        review = Review.objects.create(
            user=self.user, movie_id=4133, text="Great movie!", rating=4.5
        )
        self.assertEqual(review.text, "Great movie!")
        self.assertEqual(review.rating, 4.5)


# Review Form Test
class ReviewFormTest(TestCase):
    def test_review_form_in_movie_overview(self):
        movie_id = 12345
        response = self.client.get(
            reverse('movies:movie_overview', args=[movie_id])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Submit Review')
        self.assertTemplateUsed(response, 'movies/movie_overview.html')


# Review Submission Test
class ReviewSubmissionTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='12345'
        )
        self.client.login(username='testuser', password='12345')
        self.movie_id = 4133  # Movie Blow

    def test_review_submission_and_approval(self):
        review_text = "Amazing movie!"
        review_rating = 4.5  # Add rating valu
        response = self.client.post(
            reverse(
                'movies:movie_overview', args=[self.movie_id]
            ), {'text': review_text, 'rating': review_rating}
        )

        review = Review.objects.get(user=self.user, movie_id=self.movie_id)
        self.assertEqual(review.text, review_text)
        self.assertEqual(review.rating, review_rating)


# Admin Approval Test
class AdminReviewApprovalTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='12345'
        )
        self.admin_user = User.objects.create_superuser(
            username='moviebaseadmin', password='adminpass23'
        )
        self.movie_id = 4133  # Movie Blow
        self.review = Review.objects.create(
            user=self.user,
            movie_id=self.movie_id,
            text="Great movie!",
            rating=4.5
        )

    def test_admin_approves_review(self):
        # Admin user logs in
        self.client.force_login(self.admin_user)

        # Send request to approve the review
        response = self.client.post(
            reverse('movies:approve_review', args=[self.review.id])
        )

        # Refresh the review object from the database
        self.review.refresh_from_db()

        # Check that view is  approved
        self.assertTrue(self.review.approved)

    def test_approved_reviews_displayed(self):
        # Creating a approved review
        review = Review.objects.create(
            user=self.user,
            movie_id=1,
            text='Great Movie!',
            status='approved',
        )
        url = reverse('movies:movie_overview', args=[1])
        response = self.client.get(url)
        self.assertContains(response, "Great Movie!")

    def test_review_pending_in_admin(self):
        # Admin UUser Login
        self.client.force_login(self.admin_user)

        # Check Pending Review in Admin Panel
        response = self.client.get(
            reverse('admin:movies_review_changelist')
        )
        self.assertContains(response, "Great movie!")
        self.assertContains(response, "pending")

    def test_admin_rejects_review(self):
        # Admin user logs in
        self.client.force_login(self.admin_user)
        # Send request to reject review
        response = self.client.post(reverse('movies:reject_review', args=[self.review.id]))
        # Refresh the review object from database
        self.review.refresh_from_db()
        # Check taht review is rejected
        self.assertEqual(self.review.status, "rejected")

