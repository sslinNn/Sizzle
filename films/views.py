from django.http import StreamingHttpResponse
import ffmpeg_streaming

from django.shortcuts import render, get_object_or_404
from films.models import Film
from .services import open_file


def feed(request):
    all_films = Film.objects.all()
    return render(request, 'films/feed.html', {'all_films': all_films})


def film(request, film_id):
    _film = get_object_or_404(Film, id=film_id)
    return render(request, 'films/film.html', context={'film': _film})


def get_streaming_film(request, film_id):
    file, status_code, content_length, content_range = open_file(request, film_id)
    response = StreamingHttpResponse(file, content_type='video/mp4', status=status_code)
    response['Content-Range'] = content_range
    # response['Content-Length'] = content_length
    # print(f'CR: {content_range}\n Size: {content_length} \n File: {file}\n Status: {status_code}')
    return response


# def get_streaming_film(request, film_id):
#     _film = get_object_or_404(Film, id=film_id)
#     response = StreamingHttpResponse(open(str(_film.video), 'rb'), content_type='video/mp4', status='200')
#     return response

