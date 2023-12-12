import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from config import SPOTIPY_CLIENT_SECRET, SPOTIPY_CLIENT_ID

client_credentials_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID,
                                                      client_secret=SPOTIPY_CLIENT_SECRET)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


class SpotifyTools:

    @staticmethod
    def uri_to_url(url) -> str:  # obtain a playlist URI from a URL
        # playlist_url = input("Enter a Spotify Playlist URL:\n")
        playlist_url = url
        playlist_uri = ''

        if playlist_url.startswith("https://open.spotify.com/playlist/"):
            if '?' in playlist_url:  # link has query
                playlist_id = playlist_url.split("/playlist/")[-1].split('?')[0]
                playlist_uri = f'spotify:playlist:{playlist_id}'
            else:
                playlist_id = playlist_url.split('/playlist/')[-1]
                playlist_uri = f'spotify:playlist:{playlist_id}'

            print(f"Playlist URI is: {playlist_uri}")
        return playlist_uri

    @staticmethod
    def get_playlist_id(uri) -> str:
        return uri.split(':')[-1]

    def playlist(self):
        playlist_url = input("Enter a Spotify Playlist URL:\n")
        playlist_uri = self.uri_to_url(playlist_url)
        if playlist_uri == "":
            print("Invalid URL")
            return
        try:
            pl = spotify.playlist_items(playlist_id=self.get_playlist_id(playlist_uri))
            for track in pl['items']:
                track_name = track['track']['name']
                print(track_name)
        except Exception as e:
            print("Unexpected Error:\n", e)
