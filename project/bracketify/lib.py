import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pprint

# import pandas as pd
import random

# pd.set_option("display.max_colwidth", None)
# pd.set_option("display.max_rows", None)
# pd.set_option("display.max_columns", 4)

pp = pprint.PrettyPrinter(indent=4)

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

# genre_options = spotify.recommendation_genre_seeds()['genres']
genres = [
    "acoustic",
    "afrobeat",
    "alt-rock",
    "alternative",
    "ambient",
    "bluegrass",
    "blues",
    "bossanova",
    "brazil",
    "breakbeat",
    "british",
    "chicago-house",
    "children",
    "chill",
    "classical",
    "country",
    "dance",
    "dancehall",
    "disco",
    "disney",
    "drum-and-bass",
    "emo",
    "folk",
    "french",
    "funk",
    "garage",
    "goth",
    "grindcore",
    "groove",
    "grunge",
    "guitar",
    "happy",
    "hard-rock",
    "hip-hop",
    "honky-tonk",
    "house",
    "idm",
    "indian",
    "indie",
    "indie-pop",
    "industrial",
    "iranian",
    "jazz",
    "latin",
    "latino",
    "movies",
    "new-age",
    "new-release",
    "opera",
    "party",
    "piano",
    "pop",
    "pop-film",
    "power-pop",
    "psych-rock",
    "punk",
    "punk-rock",
    "r-n-b",
    "rainy-day",
    "reggae",
    "reggaeton",
    "road-trip",
    "rock",
    "rock-n-roll",
    "rockabilly",
    "romance",
    "sad",
    "salsa",
    "samba",
    "sertanejo",
    "show-tunes",
    "singer-songwriter",
    "ska",
    "sleep",
    "songwriter",
    "soul",
    "soundtracks",
    "spanish",
    "study",
    "summer",
    "swedish",
    "synth-pop",
    "tango",
    "trip-hop",
    "turkish",
    "work-out",
    "world-music",
]
genres = ["indie-pop"]


def get_artist_uri(name="Taylor Swift"):
    results = spotify.search(q="artist:" + name, type="artist", market="CA")
    items = results["artists"]["items"]
    try:
        top_items = sorted(items, key=lambda x: x["popularity"], reverse=True)[:5]
        print(top_items)
        artist = top_items[0]
        # pp.pprint(artist)
        uri = artist["uri"]
        return uri
    except Exception as e:
        print(e)


def get_artist_albums(name, id):
    print(f"Getting all albums for {name}:")
    response = spotify.artist_albums(id, album_type="album", limit=25)

    albums = []
    try:
        # item specify a collection of information related to each artist's album
        for item in response["items"]:
            a = {"name": item["name"], "id": item["id"], "release_year": int(item["release_date"][:4])}
            albums.append(a)
        albums = sorted(albums, key=lambda x: x["release_year"], reverse=True)
    except Exception as e:
        print(e)

    return albums
    # df = pd.DataFrame.from_dict(albums)
    # return df


def get_album_tracks(id):
    response = spotify.album_tracks(id)

    tracks = []
    try:
        for item in response["items"]:
            t = {
                "name": item["name"],
                "track_number": item["track_number"],
                "id": item["id"],
                "uri": item["uri"],
                "spotify_url": item["external_urls"]["spotify"],
                "preview_url": item["preview_url"],
            }
            tracks.append(t)
    except Exception as e:
        print(e)

    return tracks
    # df = pd.DataFrame.from_dict(tracks)
    # return df


def get_recommendations(tracks, n):
    seed_tracks = list(tracks["id"])
    print("Track recommendations based on your top 5 songs:")
    response = spotify.recommendations(
        seed_tracks=seed_tracks,
        # seed_genres=genres,
        country="CA",
        min_danceability=0.5,
    )
    recs = []
    try:
        for item in response["tracks"][:n]:
            t = {
                "track_name": item["name"],
                "album_name": item["album"]["name"],
                "artist_name": item["artists"][0]["name"],
                "spotify_url": item["external_urls"]["spotify"],
                "preview_url": item["preview_url"],
                "track_uri": item["uri"],
                "album_uri": item["album"]["uri"],
                "artist_uri": item["artists"][0]["uri"],
            }
            recs.append(t)
    except Exception as e:
        print(e)

    return recs
    # df = pd.DataFrame.from_dict(recs)
    # return df.iloc[:, :4]


def merge_sort(arr, sort_fn):
    print(arr)
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left, sort_fn)
    right = merge_sort(right, sort_fn)

    return merge(left, right, sort_fn)


def merge(left, right, sort_fn):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if sort_fn(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]

    return result


if __name__ == "__main__":
    # print(get_artist_uri("Muna"))

    tracks = get_album_tracks("3lS1y25WAhcqJDATJK70Mq")
    pp.pprint(tracks)
