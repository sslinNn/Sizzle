from django.db.models import Count
from django.http import StreamingHttpResponse

from django.shortcuts import render, get_object_or_404
from films.models import Film
from .services import open_file


def feed(request):
    all_films = Film.objects.all()
    return render(request, 'films/feed.html', {'all_films': all_films})


def film(request, film_id):
    # film = Film.objects.get(id=film_id)
    _film = get_object_or_404(Film, id=film_id)
    return render(request, 'films/film.html', context={'film': _film})


def get_streaming_film(request, film_id):
    file, status_code, content_length, content_range = open_file(request, film_id)
    response = StreamingHttpResponse(file, status=status_code, content_type='video/mp4')
    response['Accept-Ranges'] = 'bytes'
    response['Content-Length'] = str(content_length)
    response['Cache-Control'] = 'no-cache'
    response['Control-Range'] = content_range
    print(f'--------------------{response}----------------------')
    return response
