import json
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from flask import Flask, request, redirect

# Load credentials from the spotify_credentials.json file
with open("config/spotify_credentials.json") as cred_file:
    creds = json.load(cred_file)

# Setup Flask app
app = Flask(__name__)

# Spotify OAuth setup
sp_oauth = SpotifyOAuth(
    client_id=creds["client_id"],
    client_secret=creds["client_secret"],
    redirect_uri=creds["redirect_uri"],
    scope="user-library-read user-top-read playlist-read-private"
)

@app.route("/")
def login():
    # Redirect user to Spotify's authentication page
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)

@app.route("/callback")
def callback():
    # Spotify redirects here with authorization code
    token_info = sp_oauth.get_access_token(request.args["code"])
    access_token = token_info["access_token"]
    sp = spotipy.Spotify(auth=access_token)

    # Test: Get the current user's top tracks (as an example)
    results = sp.current_user_top_tracks(limit=10, offset=0, time_range="short_term")
    return json.dumps(results)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888)
