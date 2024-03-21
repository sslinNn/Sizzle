from django.urls import path
from . import views

urlpatterns = [
    path('', views.feed, name='feed'),
    path('genre/<int:pk>/', views.feed_by_genre, name='feed_by_genre'),
    path('film/<int:film_id>/', views.film, name='film'),
]
