import requests

# Set the base URL for the Spotify Web API
base_url = "https://api.spotify.com/v1/tracks/"

# Set the track URI to check
track_uri = "7qysG3xmCneKZuVjnDCif2"

# Send a request to the Spotify Web API using the track URI
response = requests.get(base_url + track_uri)

# Check the status code of the response
if response.status_code == 200:
    # The track URI is valid
    print("The track URI is valid!")
else:
    # The track URI is invalid or the track is not available on Spotify
    print("The track URI is invalid or the track is not available on Spotify.")
