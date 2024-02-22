from django.urls import path
from . import views

urlpatterns = [
    path('', views.feed, name='feed'),
    path('film/<film_id>/', views.film, name='film'),
]
