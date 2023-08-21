from django.contrib import admin
from .models import Movie


class MovieAdmin(admin.ModelAdmin):
    list_filter = ('release_date',)  # Fields you want to filter by


admin.site.register(Movie, MovieAdmin)
