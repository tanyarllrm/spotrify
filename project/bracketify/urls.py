from django.urls import path

from . import views

app_name = "bracketify"
urlpatterns = [
    path("", views.home, name="home"),
    path("search/", views.artist_search_result, name="search_artist"),
    path("bracket/<album_id>/", views.bracket, name="bracket"),
]
