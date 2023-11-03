from django.urls import path

from . import views

app_name = "bracketify"
urlpatterns = [
    path("", views.home, name="home"),
    path("search/", views.artist_search_result, name="search_artist"),
    path("album/<album_id>/sort/", views.album_sort, name="album_sort"),
    path("album/<album_id>/result/", views.bracket, name="bracket_sort"),
]
