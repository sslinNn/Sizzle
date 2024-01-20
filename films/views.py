from django.db.models import Count

from django.shortcuts import render
from films.models import Film


def feed(request):
    all_films = Film.objects.all()
    return render(request, 'films/feed.html', {'all_films': all_films})


def film(request, film_id):
    film = Film.objects.get(id=film_id)
    return render(request, 'films/film.html', context={'film': film})