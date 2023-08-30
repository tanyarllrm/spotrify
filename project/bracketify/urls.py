from django.urls import path

from . import views

app_name = "bracketify"
urlpatterns = [
    path("", views.home, name="home"),
    path("search/", views.artist_top_songs, name="search_artist"),
]
