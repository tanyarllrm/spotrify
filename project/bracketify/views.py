from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.views.generic.edit import FormView
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from .models import Record, Players
from .forms import UserChoiceForm
from .lib import *

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
global_context = {}


def home(request):
    return render(request, "bracketify/home.html")


def artist_search_result(request):
    if request.method == "POST":
        input_name = request.POST.get("artist_name", "")
        artist_id = get_artist_uri(input_name)
        artist_name = spotify.artist(artist_id)["name"]
        try:
            top_songs = spotify.artist_top_tracks(artist_id, country="CA")["tracks"][:5]
        except:
            top_songs = []
        all_related_artists = spotify.artist_related_artists(artist_id)["artists"]
        sorted_artists = sorted(all_related_artists, key=lambda x: x["popularity"], reverse=True)[:5]
        related_artists = [a["name"] for a in sorted_artists]
        albums = get_artist_albums(artist_name, artist_id)

        context = {"artist_name": artist_name, "top_songs": top_songs, "related_artists": related_artists, "albums": albums}
        global_context["artist_name"] = artist_name

        return render(request, "bracketify/artist_detail.html", context)
    return render(request, "bracketify/search_artist.html")


def album_sort(request, album_id):
    album = spotify.album(album_id, market="CA")
    global_context["album"] = {"name": album["name"], "id": album_id}
    tracklist = get_album_tracks(album_id)
    global_context["tracklist"] = tracklist

    # context = {"album": {"id": album_id, "name": album_name}, "artist_name": artist_name, "tracklist": tracklist}
    return render(request, "bracketify/album_sorting.html", global_context)


def merge_sort(request, arr, sort_fn):
    print(arr)

    def merge(left, right):
        result = []
        i, j = 0, 0

        while i < len(left) and j < len(right):
            if sort_fn(request,left[i], right[j]):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result += left[i:]
        result += right[j:]

        return result

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(request,left, sort_fn)
    right = merge_sort(request,right, sort_fn)

    return merge(left, right)


def user_choice(request, L, R):
    # process form data from user and render as a page with buttons
    if request.method == "POST":
        form = UserChoiceForm(option1=L, option2=R, data=request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            choice = form.cleaned_data["user_choice"]
            # if choice == "L" return true, else return false
            return choice == "L"
            # return HttpResponseRedirect(reverse("bracketify:bracket_sort", args=(L, R)))  # redirect to the same page

    form = UserChoiceForm(option1=L, option2=R)
    return render(request, "bracketify/sort.html", {'form': form})


def bracket(request, album_id):
    # tracks = [t['name'] for t in global_context["tracklist"]]
    # sorted_tracks = merge_sort(request,tracks, user_choice)
    # return sorted_tracks

    return render(request, "bracketify/sort.html", global_context)
