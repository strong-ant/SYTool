from spotify_tools import SpotifyTools
from youtube_tools import YouTubeTools



class SpotifyToYoutube:
    
    #create the playlist
    #get the spotify playlist link
    #get the names of videos to search
    #search on youtube and obtain video IDs
    #add the video id's to the playlist
    
    
    def convert_playlist(self,playlist_name, playlist_description, spotify_playlist_url):
        sptools = SpotifyTools()
        yttools = YouTubeTools()
        try:
            #create the playlist
            yt_auth = yttools.yt_authentication()
            yt_playlist_id = yttools.create_youtube_playlist(yt_auth, playlist_name, playlist_description)
            
            #get the song names and artists to search for
            queries = sptools.get_playlist_queries(spotify_playlist_url)
            
            #search youtube for the videos to add to the playlist
            for query in queries:
                video_id = yttools.ytsearch(query)
                yttools.add_to_playlist(yt_auth, yt_playlist_id, video_id)
        except Exception as e:
            print("Unexpected Error:\n", e)