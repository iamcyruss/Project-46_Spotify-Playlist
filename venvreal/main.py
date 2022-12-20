import requests
from bs4 import BeautifulSoup
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
#from spotipy.oauth2 import SpotifyClientCredentials


EXCLUDE_LIST = ['Songwriter(s):', 'Producer(s):', 'Imprint/Promotion Label:', '-', 'NEW', 'RE-\\nENTRY']
SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
SPOTIPY_REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI")
SCOPE = "playlist-modify-public user-top-read"
USERNAME = os.getenv("USERNAME")
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope=SCOPE,
                                               client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               show_dialog=False,
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
li_raw = [li.find(name="h3", class_="c-title") for li in soup.find_all(name="li", class_="o-chart-results-list__item")]
#h3_element = li_raw.find(name="h3", class_="c-title")
print(li_raw)
#print(li_raw)
h3_list = []
for h3_title in soup.select("h3#title-of-a-story.c-title"):
    if h3_title.getText(strip=True) in EXCLUDE_LIST:
        pass
    else:
        h3_list.append(h3_title.getText(strip=True))
span_list = []
for span_artist in soup.select("span.c-label"):
    strip_span_artist = span_artist.getText(strip=True)
    try:
        if span_artist.getText(strip=True) in EXCLUDE_LIST:
            pass
        elif int(strip_span_artist) > 0:
            pass
        else:
            span_list.append(span_artist.getText(strip=True))
    except ValueError as error:
        span_list.append(span_artist.getText(strip=True))
h3_list_trim = h3_list[2:(len(h3_list)-20):1]
print(h3_list)
print(span_list)
#song_titles_raw = soup.find_all(name="div", class_="o-chart-results-list-row-container")
#print(song_titles_raw)
"""
song_titles = []
for title in song_titles_raw:
    single_song_title = title.getText(strip=True)
    if single_song_title in EXCLUDE_LIST:
        pass
    else:
        song_titles.append(single_song_title)
"""
#print(song_titles)
only_song_titles = h3_list[4:(len(h3_list)-20):1]
#print(only_song_titles)
sp.user_playlist_create(user=USERNAME, name=user_date)
get_user_playlists = sp.user_playlists(user=USERNAME)
print(get_user_playlists)
first_playlist_id = get_user_playlists['items'][0]['id']
print(first_playlist_id)

for id, song in enumerate(only_song_titles):
    spotify_song_uri = []
    spotify_song = sp.search(q=song, limit=1, type="track", market="US")
    #print(f"Billboard Song data: {song}")
    #print(f"Spotify Search results: {spotify_song}")
    try:
        spotify_song_uri.append(spotify_song['tracks']['items'][0]['uri'])
    except IndexError as error:
        print(error)
    #print(f"Spotify Song URI: {spotify_song_uri}")
    #print(sp.current_user_top_tracks())
    #sp.user_playlist_add_tracks(user=USERNAME, playlist_id=first_playlist_id, tracks=spotify_song_uri, position=id)
    print(f"Added song title: {song} to the {user_date} playlist. I think...")
