import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Load credentials from JSON file
with open('spotify_credentials.json') as cred_file:
    credentials = json.load(cred_file)

# Authenticate with Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=credentials['client_id'],
    client_secret=credentials['client_secret'],
    redirect_uri=credentials['redirect_uri'],
    scope="user-library-read"
))

# Fetch liked songs
def fetch_liked_songs():
    results = sp.current_user_saved_tracks(limit=50)
    songs = []
    for item in results['items']:
        track = item['track']
        song_info = {
            'name': track['name'],
            'artist': track['artists'][0]['name'],
            'album': track['album']['name']
        }
        songs.append(song_info)
        print(f"{song_info['name']} by {song_info['artist']} from {song_info['album']}")
    return songs

if __name__ == "__main__":
    print("Fetching your Spotify liked songs...")
    liked_songs = fetch_liked_songs()
    print(f"\nFetched {len(liked_songs)} songs!")
