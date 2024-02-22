from django.shortcuts import render, get_object_or_404
from films.models import Film, Genre


def feed(request):
    all_genres = Genre.objects.all()
    all_films = Film.objects.all()
    return render(request, 'films/feed.html', {'all_films': all_films, 'all_genres': all_genres})


def film(request, film_id):
    _film = get_object_or_404(Film, id=film_id)
    return render(request, 'films/film.html', context={'film': _film})
