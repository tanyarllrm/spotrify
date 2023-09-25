import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pprint
import pandas as pd
import random

pd.set_option("display.max_colwidth", None)
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", 4)

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
    results = spotify.search(q="artist:" + name, type="artist")
    items = results["artists"]["items"]

    try:
        top_items = sorted(items, key=lambda x: x["followers"]["total"], reverse=True)[:5]
        artist = top_items[0]
        # pp.pprint(artist)
        uri = artist["uri"]
        return uri
    except Exception as e:
        print(e)


def get_artist_albums(name, id):
    print(f"Getting all albums for {name}:")
    response = spotify.artist_albums(id, album_type="album")

    albums = []
    try:
        # item specify a collection of information related to each artist's album
        for item in response["items"]:
            a = {"name": item["name"], "id": item["id"], "release_year": str(item["release_date"][:4])}
            albums.append(a)
    except Exception as e:
        print(e)

    df = pd.DataFrame.from_dict(albums)
    return df


def get_album_tracks(name, id):
    print(f"Getting all tracks on album {name}:")
    response = spotify.album_tracks(id)

    tracks = []
    try:
        pp.pprint(response["items"][0])
        for item in response["items"]:
            t = {
                "name": item["name"],
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
        pp.pprint(response["tracks"][0])
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

    df = pd.DataFrame.from_dict(recs)
    return df.iloc[:, :4]


if __name__ == "__main__":
    tracks = get_album_tracks("Saves the World", "5ZpSRd3GwvEGrD7kWn0fHz")
    pp.pprint(tracks)
    album = spotify.album("5ZpSRd3GwvEGrD7kWn0fHz", market="CA")
    album_name = album["name"]
    artist_name = album["artists"][0]["name"]
    print(album_name)
    print(artist_name)
