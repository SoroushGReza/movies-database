from django.contrib import admin
from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'movie_id', 'text', 'status']
    list_filter = ('status', 'approved')
    actions = ['approve_reviews', 'reject_reviews']

    # Approving Reviews
    def approve_reviews(self, request, queryset):
        queryset.update(status='approved', approved=True)

    # Rejecting reviews
    def reject_reviews(self, request, queryset):
        queryset.update(status='approved', approved=False)

    approve_reviews.short_description = "Approve selected reviews"
    reject_reviews.short_description = "Reject selected reviews"
