from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.feed, name='feed'),
    path('film/<film_id>/', views.film, name='film'),
]
