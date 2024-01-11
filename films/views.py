from django.shortcuts import render
from films.models import Film


def feed(request):
    all_films = Film.objects.all()
    return render(request, 'films/feed.html', {'all_films': all_films})
