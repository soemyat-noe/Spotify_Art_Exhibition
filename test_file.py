#Importing necessary tools
# Spotipy: For accessing the Spotify API.
# Pandas: For data handling and manipulation.
# Urllib: For making HTTP requests to APIs.
# IPython.display: For displaying images and media in the Notebook.

import spotipy
import spotipy.util as util
import json
import webbrowser
import pandas as pd
import urllib.request
from IPython.display import display, Image

#Accessing Spotify API 
print('starting')
cred = "spotify_keys.json"
with open(cred,"r") as key_file:
    api_tokens = json.load(key_file)

key_file.close()

client_id = api_tokens['client_id']
client_secret = api_tokens['client_secret']
redirectURI = api_tokens['redirect']
username = api_tokens['username']

scope = 'user-read-private user-read-playback-state user-modify-playback-state playlist-modify-public user-library-read'
token = util.prompt_for_user_token(username, scope, client_id=client_id, client_secret=client_secret, redirect_uri=redirectURI)

sp = spotipy.Spotify(auth=token)
# Available genre seeds from Spotify are fetched, which will later be used to 
# generate music recommendations based on the selected art categories.

print('Here now')
genre_seeds = sp.recommendation_genre_seeds()

print(genre_seeds)
