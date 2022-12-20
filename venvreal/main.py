import requests
from bs4 import BeautifulSoup
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
#from spotipy.oauth2 import SpotifyClientCredentials
"""
12-20-2022|holy fuck this project is rough. I've gotten it all to work but now I'm trying to make the searching 
of songs more accurate. I noticed if i search for just the song title I might get the right one and I might not.
I figured searching by the aritist name and title of the song would yield more accurate results but I cant seem to 
extract what I want from the website without getting a bunch of other shit with it. I'm going to still work on it but I
might end up just doing it by the title name. 
I also have an EXCLUDE list that seems to work most of the time... idk. The billboard site though is garbage for its
class and id tags. like you all couldnt give the title of the song id="title of song" and the artist for that song
id="artist of song". if it was like that this would be a cake walk.
"""


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
#li_raw = [li.find(name="h3", class_="c-title") and li.find(name="span", class_="c-label") for li in soup.find_all(name="li", class_="o-chart-results-list__item")]
#h3_element = li_raw.find(name="h3", class_="c-title")
#print(len(li_raw))
#print(li_raw)

# Find the li elements
li_elements = soup.find_all(name="li", class_="o-chart-results-list__item")

# Iterate over the li elements
title_text = []
span_text = []
for li_element in li_elements:
    # Find the h3 elements within the li element
    h3_elements = li_element.find_all(name="h3", id="title-of-a-story")
    span_elements = li_element.find_all(name="span", class_="c-label")

    #Extract the text from the h3 elements
    for h3_element in h3_elements:
        title_text.append(h3_element.getText(strip=True))
        #print(title_text)
    for span_element in span_elements:
        try:
            if span_element.getText(strip=True) in EXCLUDE_LIST:
                pass
            elif int(span_element.getText(strip=True)):
                pass
            else:
                span_text.append(span_element.getText(strip=True))
        except ValueError as error:
            span_text.append(span_element.getText(strip=True))

#print(title_text)
#print(len(title_text))
#print(span_text)
#print(len(span_text))

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
#print(h3_list)
#print(span_list)
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
#print(get_user_playlists)
first_playlist_id = get_user_playlists['items'][0]['id']
#print(first_playlist_id)
title_artist = []

for id, song in enumerate(title_text):
    spotify_song_uri = []
    #print(f"Searching for '{song} {span_text[id]}'")
    title_artist.append(f"{song} {span_text[id]}")
    spotify_song = sp.search(q=song, limit=1, type="track", market="US")
    #print(f"Billboard Song data: {song}")
    #print(f"Spotify Search results: {spotify_song}")
    try:
        spotify_song_uri.append(spotify_song['tracks']['items'][0]['uri'])
    except IndexError as error:
        print(error)
    #print(f"Spotify Song URI: {spotify_song_uri}")
    #print(sp.current_user_top_tracks())
    sp.user_playlist_add_tracks(user=USERNAME, playlist_id=first_playlist_id, tracks=spotify_song_uri, position=id)
    print(f"{id+1} Added song: '{song} by {span_text[id]}' to the {user_date} playlist. I think...")

