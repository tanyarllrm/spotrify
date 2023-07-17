import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import argparse
import pprint
import pandas as pd
from pandas.api.types import CategoricalDtype
from lib import get_artist_uri, get_artist_albums, get_album_tracks, get_recommendations
from sort import merge_sort, user_choice
pd.set_option('display.max_colwidth', None)

pp = pprint.PrettyPrinter(indent=4)

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())


if __name__ == '__main__':
    # Get parameters from command line input
    parser = argparse.ArgumentParser(description='Enter an artist name')
    parser.add_argument('-a', '--artist')
    args = parser.parse_args()
    artist_name = args.artist
    print(f'Entered artist {artist_name}')

    artist_uri = get_artist_uri(artist_name)
    artist = spotify.artist(artist_uri)

    albums_df = get_artist_albums(artist_name, artist_uri)
    print(albums_df)

    index = int(input('Choose an album from the list by entering its row index: '))
    album_name = albums_df._get_value(index, 'name')
    album_id = albums_df._get_value(index, 'id')

    tracks_df = get_album_tracks(album_name, album_id)

    track_names = list(tracks_df['name'])
    print(f'Sorting the tracks on {album_name} by {artist_name} based on your preference')
    sorted_tracks = merge_sort(track_names, user_choice)
    track_order = CategoricalDtype(sorted_tracks,ordered=True)
    tracks_df['name'] = tracks_df['name'].astype(track_order)
    tracks_df.sort_values('name', ignore_index=True, inplace=True)

    print(f'\nYour ranking:')
    print(tracks_df.head(10))



    recs = get_recommendations(tracks_df.head(5), 5)
    print(recs)

