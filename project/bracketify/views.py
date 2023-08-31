from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from .models import Record
from .lib import *

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())


def home(request):
    return render(request, "bracketify/home.html")


def artist_top_songs(request):
    if request.method == "POST":
        artist_name = request.POST.get("artist_name", "")
        artist_id = get_artist_uri(artist_name)
        try:
            top_songs = spotify.artist_top_tracks(artist_id, country="CA")["tracks"][:5]
        except:
            top_songs = []
        all_related_artists = spotify.artist_related_artists(artist_id)["artists"]
        sorted_artists = sorted(all_related_artists, key=lambda x: x["popularity"], reverse=True)[:5]
        related_artists = [a["name"] for a in sorted_artists]
        albums = get_artist_albums(artist_name, artist_id)

        response = {"artist_name": artist_name, "top_songs": top_songs, "related_artists": related_artists, "albums": albums}

        return render(request, "bracketify/artist_result.html", response)
    return render(request, "bracketify/search_artist.html")
