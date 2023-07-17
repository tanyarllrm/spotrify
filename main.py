import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import argparse
import pprint
import pandas as pd
from lib import get_artist_uri, get_artist_albums, get_album_tracks
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
    print(tracks_df)

    track_names = list(tracks_df['name'])
    print(f'Sorting the tracks on {album_name} by {artist_name} based on your preference')
    sorted_tracks = merge_sort(track_names, user_choice)
    print(f'\nFinal results:')
    pp.pprint(sorted_tracks)

