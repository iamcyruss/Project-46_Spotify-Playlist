import requests
from bs4 import BeautifulSoup
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
#from spotipy.oauth2 import SpotifyClientCredentials


EXCLUDE_LIST = ['Songwriter(s):', 'Producer(s):', 'Imprint/Promotion Label:']
SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
SPOTIPY_REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI")
SCOPE = "playlist-modify-private playlist-modify-public"
USERNAME = os.getenv("USERNAME")
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope=SCOPE,
                                               client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               show_dialog=True,
                                               cache_path="token.txt",
                                               username=USERNAME))

#print(f"User info: {sp.user(user=USERNAME)}")

try:
    user_date = input("Choose a date and create a playlist of most popular songs from that date. YYYY-MM-DD\n")
except:
    print("error 1")

site = f"https://www.billboard.com/charts/hot-100/{user_date}/"
#print(site)
website_response = requests.get(site)
website_response_raw = website_response.text
soup = BeautifulSoup(website_response_raw, "html.parser")
song_titles_raw = soup.find_all(name="h3", id="title-of-a-story")
raw = soup.find(name="li", class_="o-chart-results-list__item")
print(raw.get("h3"))
#song_titles_raw = soup.find_all(name="div", class_="o-chart-results-list-row-container")
#print(soup.prettify())
#print(song_titles_raw)
song_titles = []
for title in song_titles_raw:
    single_song_title = title.getText(strip=True)
    if single_song_title in EXCLUDE_LIST:
        pass
    else:
        song_titles.append(single_song_title)

#print(song_titles)
only_song_titles = song_titles[3:(len(song_titles)-20):1]
#print(only_song_titles)
#sp.user_playlist_create(user=USERNAME, name=user_date)
#print(sp.user_playlists(user=USERNAME))
for id, song in enumerate(only_song_titles):
    spotify_song = sp.search(q=song, limit=10, type="track", market="US")
    print(song)
    print(spotify_song)
    spotify_song_uri = spotify_song['tracks']['items'][0]['uri']
    print(spotify_song_uri)
    sp.user_playlist_add_tracks(user=USERNAME, playlist_id="6XxCAe6vsvKObMdh999cn2", tracks=spotify_song_uri, position=id)
    print(f"Added song title: {song} with URI: {spotify_song_uri} to the {user_date} playlist. I think...")
