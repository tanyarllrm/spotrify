import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pprint
import pandas as pd
import random
pd.set_option('display.max_colwidth', None)

pp = pprint.PrettyPrinter(indent=4)

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())


def get_artist_uri(name='Taylor Swift'):
    results = spotify.search(q='artist:' + name, type='artist')
    items = results['artists']['items']
    try:
        artist = items[0]
        # pp.pprint(artist)
        uri = artist['uri']
        return uri
    except Exception as e:
        print(e)


def get_artist_albums(name, id):
    print(f'Getting all albums for {name}:')
    response = spotify.artist_albums(id)

    albums = []
    try:
        # item specify a collection of information related to each artist's album
        for item in response['items']:
            a = {'name': item['name'], 'id': item['id'], 'release_date': item['release_date']}
            albums.append(a)
    except Exception as e:
        print(e)

    df = pd.DataFrame.from_dict(albums)
    return df


def get_album_tracks(name, id):
    print(f'Getting all tracks on album {name}:')
    response = spotify.album_tracks(id)

    tracks = []
    try:
        for item in response['items']:
            t = {'name': item['name'], 'id': item['id'], 'uri': item['uri'],
                 'spotify_url': item['external_urls']['spotify'], 'preview_url': item['preview_url']}
            tracks.append(t)
    except Exception as e:
        print(e)

    df = pd.DataFrame.from_dict(tracks)
    return df


def bubble_sort_by_preference(values):
    n = len(values)

    # Choose the inputs to select the left or right option
    L, R = '1', '2'
    print(f'Rules: Enter {L} for the choice on the left or {R} for the choice on the right.')

    # Keep track of which pairs have already been compared
    compared_pairs = set()

    # Perform bubble sort based on user preference
    for i in range(n - 1):
        for j in range(n - i - 1):
            k = j + 1
            print(i, j, k)

            # Generate a pair and shuffle the list if it has already been compared
            pair = frozenset([values[j], values[k]])
            while pair in compared_pairs:
                random.shuffle(values)
                pair = frozenset([values[j], values[k]])
            compared_pairs.add(pair)
            # print(compared_pairs)

            # Display the two values for comparison
            print(f"\nComparison {j + 1}:")
            print(f"{values[j]} vs. {values[k]}")

            # Get user input for their preference
            choice = ''
            while choice not in [L, R]:
                choice = input("Enter your preference (1 or 2): ")

            # Swap the values if necessary based on user preference
            if choice == L:
                values[j], values[k] = values[k], values[j]

            print('current list:',values)

            # # Prompt to continue with the next comparison
            # if i < n - 2:
            #     next_comparison = input("Continue to the next comparison? (yes or no): ")
            #     if next_comparison.lower() != 'yes':
            #         return values

    return values


if __name__ == '__main__':

    list = [1,2,3,4,5,6,7,8]
    sorted_movies = bubble_sort_by_preference(list)
    print("Sorted movies based on your preference:")
    print(sorted_movies)


