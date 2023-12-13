import spotipy
import requests
from spotipy.oauth2 import SpotifyClientCredentials
from config import SPOTIPY_CLIENT_SECRET, SPOTIPY_CLIENT_ID

client_credentials_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID,
                                                      client_secret=SPOTIPY_CLIENT_SECRET)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


class SpotifyTools:


    def validate_spotify_url(self, url) -> bool: #check if repsonse code is 200
        try:
            response = requests.get(url)
            return response.status_code == 200
        except requests.exceptions.RequestException as e:
            print(f"Error validating URL: {e}")
            return False

    def uri_to_url(self, playlist_url) -> str:  # obtain a playlist URI from a URL
        playlist_uri = ''
        try:
            if playlist_url.startswith("https://open.spotify.com/playlist/"): #check url format
                if self.validate_spotify_url(playlist_url): #check if spotify link works
                    if '?' in playlist_url:  # link has query
                        playlist_id = playlist_url.split("/playlist/")[-1].split('?')[0]
                        playlist_uri = f'spotify:playlist:{playlist_id}'
                    else:
                        playlist_id = playlist_url.split('/playlist/')[-1]
                        playlist_uri = f'spotify:playlist:{playlist_id}'
                else:
                    raise ValueError("Invalid Spotify link, or playlist is private")
                #print(f"Playlist URI is: {playlist_uri}")
            else:
                raise ValueError("Invalid Spotify link format (https://open.spotify.com/playlist/)")
        except ValueError as e:
            print(f"Error: {e}")
        return playlist_uri

    @staticmethod
    def get_playlist_id(uri) -> str:
        return uri.split(':')[-1]

    def playlist(self):
        playlist_url = input("Enter a Spotify Playlist URL:\n")
        playlist_uri = self.uri_to_url(playlist_url)
        if playlist_uri == "":
            return
        try:
            pl = spotify.playlist_items(playlist_id=self.get_playlist_id(playlist_uri))
            for track in pl['items']:
                track_name = track['track']['name']
                print(track_name)
        except Exception as e:
            print("Unexpected Error:\n", e)
