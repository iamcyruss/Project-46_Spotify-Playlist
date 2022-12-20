response = {
  'tracks': {
    'href': 'https://api.spotify.com/v1/search?query=He+Loves+U+Not&type=track&market=US&offset=0&limit=1',
    'items': [
      {
        'album': {
          'album_type': 'album',
          'artists': [
            {
              'external_urls': {
                'spotify': 'https://open.spotify.com/artist/6gbGGM0E8Q1hE511psqxL0'
              },
              'href': 'https://api.spotify.com/v1/artists/6gbGGM0E8Q1hE511psqxL0',
              'id': '6gbGGM0E8Q1hE511psqxL0',
              'name': 'Ray J',
              'type': 'artist',
              'uri': 'spotify:artist:6gbGGM0E8Q1hE511psqxL0'
            }
          ],
          'external_urls': {
            'spotify': 'https://open.spotify.com/album/4cmmca5HU2WP9yIvErhnf6'
          },
          'href': 'https://api.spotify.com/v1/albums/4cmmca5HU2WP9yIvErhnf6',
          'id': '4cmmca5HU2WP9yIvErhnf6',
          'images': [
            {
              'height': 640,
              'url': 'https://i.scdn.co/image/ab67616d0000b27370a53ec0d4c839795025856f',
              'width': 640
            },
            {
              'height': 300,
              'url': 'https://i.scdn.co/image/ab67616d00001e0270a53ec0d4c839795025856f',
              'width': 300
            },
            {
              'height': 64,
              'url': 'https://i.scdn.co/image/ab67616d0000485170a53ec0d4c839795025856f',
              'width': 64
            }
          ],
          'name': "This Ain't A Game",
          'release_date': '2001-06-19',
          'release_date_precision': 'day',
          'total_tracks': 16,
          'type': 'album',
          'uri': 'spotify:album:4cmmca5HU2WP9yIvErhnf6'
        },
        'artists': [
          {
            'external_urls': {
              'spotify': 'https://open.spotify.com/artist/6gbGGM0E8Q1hE511psqxL0'
            },
            'href': 'https://api.spotify.com/v1/artists/6gbGGM0E8Q1hE511psqxL0',
            'id': '6gbGGM0E8Q1hE511psqxL0',
            'name': 'Ray J',
            'type': 'artist',
            'uri': 'spotify:artist:6gbGGM0E8Q1hE511psqxL0'
          },
          {
            'external_urls': {
              'spotify': 'https://open.spotify.com/artist/2RdwBSPQiwcmiDo9kixcl8'
            },
            'href': 'https://api.spotify.com/v1/artists/2RdwBSPQiwcmiDo9kixcl8',
            'id': '2RdwBSPQiwcmiDo9kixcl8',
            'name': 'Pharrell Williams',
            'type': 'artist',
            'uri': 'spotify:artist:2RdwBSPQiwcmiDo9kixcl8'
          }
        ],
        'disc_number': 1,
        'duration_ms': 305933,
        'explicit': True,
        'external_ids': {
          'isrc': 'USAT20102141'
        },
        'external_urls': {
          'spotify': 'https://open.spotify.com/track/7qysG3xmCneKZuVjnDCif2'
        },
        'href': 'https://api.spotify.com/v1/tracks/7qysG3xmCneKZuVjnDCif2',
        'id': '7qysG3xmCneKZuVjnDCif2',
        'is_local': False,
        'is_playable': True,
        'name': 'Formal Invite (feat. Pharrell Williams)',
        'popularity': 18,
        'preview_url': 'https://p.scdn.co/mp3-preview/5b78b630fa8f15b0c9b3b7750efe71a1e27ff4ae?cid=ac9c3de96c014157b1a9043dab32aa3a',
        'track_number': 4,
        'type': 'track',
        'uri': 'spotify:track:7qysG3xmCneKZuVjnDCif2'
      }
    ],
    'limit': 1,
    'next': 'https://api.spotify.com/v1/search?query=He+Loves+U+Not&type=track&market=US&offset=1&limit=1',
    'offset': 0,
    'previous': None,
    'total': 1241
  }
}

# Get the list of tracks from the response
tracks = response['tracks']['items']

# Check if there are any tracks in the list
if tracks:
    # Get the first track from the list
    track = tracks[0]

    # Get the track URI from the track object
    track_uri = track['uri']

    # Print the track URI
    print(track_uri)
else:
    print("No tracks found in the response")
