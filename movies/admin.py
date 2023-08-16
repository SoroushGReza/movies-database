from django.contrib import admin
from .models import Movie, Review, Rating, UserList
from .forms import MovieForm


class MovieAdmin(admin.ModelAdmin):
    form = MovieForm
    list_display = ('title', 'genre', 'release_date', 'rating')
    list_filter = ('release_date',)  # Fields you want to filter by


admin.site.register(Movie, MovieAdmin)
admin.site.register(Review)
admin.site.register(Rating)
admin.site.register(UserList)
