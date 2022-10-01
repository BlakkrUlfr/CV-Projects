import os

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

import requests
from bs4 import BeautifulSoup
from pprint import pprint

date_of_choice = input('Which year do you want to travel to? Type the date in this format YYYY-MM-DD:')

URL = f'https://www.billboard.com/charts/hot-100/{date_of_choice}'

SPOTIPY_CLIENT_ID = 'd336b16de3c3462fad6270adaf5c5400'
SPOTIPY_CLIENT_SECRET = '889beef0b5744f6fa20dd92c9b4bd4cc'
SPOTIPY_REDIRECT_URI = 'http://localhost'

# response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
response = requests.get(url=URL)
website_html = response.text

# soup = BeautifulSoup(response.text, 'html.parser')
soup = BeautifulSoup(markup=website_html, features='html.parser')
# print(soup.prettify())

# songs_h3 = soup.select(selector="li #title-of-a-story")
# songs_h3 = soup.find_all("h3", class_="a-no-trucate")
all_songs_h3 = soup.select(selector='li ul li h3')
song_titles = [song_h3.getText().strip() for song_h3 in all_songs_h3]
# song_titles = [song_h3.getText().strip('\n\t') for song_h3 in all_songs_h3 ]
# pprint(song_titles)

scope = 'playlist-modify-private'

# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

auth_code_flow = SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET,
                              redirect_uri=SPOTIPY_REDIRECT_URI, cache_path='token.txt', show_dialog=True,
                              open_browser=True, scope=scope)

# token = auth_code_flow.get_access_token(as_dict=False)

sp = spotipy.Spotify(oauth_manager=auth_code_flow)

# user_id = sp.current_user()["id"]
my_user_id = sp.current_user()
print(my_user_id['id'])

year = date_of_choice.split('-')[0]
# year = date_of_choice[:4]

track_uris = []
for song_title in song_titles:
    results = sp.search(q=f'track:{song_title}+year:{year}', type='track', market='GB')
    # pprint(object=results)
    try:
        track_uri = results['tracks']['items'][0]['uri']
        track_uris.append(track_uri)
    except IndexError:
        print(f"{song_title} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=my_user_id['id'], name=f'{year} Billboard 100', public=False)
playlist_id = playlist['id']
sp.playlist_add_items(playlist_id=playlist_id, items=track_uris)

