from django.contrib import admin
from films.models import Film, Genre

admin.site.register(Genre)
admin.site.register(Film)
