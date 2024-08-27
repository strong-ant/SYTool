from spotify_tools import SpotifyTools
from youtube_tools import YouTubeTools
from spotify_to_youtube import SpotifyToYoutube
import tkinter as tk

if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    sptools = SpotifyTools()
    yttools = YouTubeTools()
    spotify_to_yt = SpotifyToYoutube()

    print("Welcome to SYTool")
    print("-----------------")

    #Main Menu
    while True:
        print("\nPlease make a choice: ")
        print("1. Spotify playlist to YouTube")
        print("2. Create Playlist")
        print("q to quit")
        menuChoice = input("\n")

        if menuChoice == "1":
            playlist_name = input("Provide a name for your playlist: ")
            playlist_description = input("Provide a description for your playlist: ")
            spotify_url = input("Provide the spotify playlist URL: \n")
            spotify_to_yt.convert_playlist(playlist_name, playlist_description, spotify_url)
        elif menuChoice == "2":
            playlist_name = input("Provide a name for your playlist: ")
            playlist_description = input("Provide a description for your playlist: ")
            ytauth = yttools.yt_authentication()
            plid = yttools.create_youtube_playlist(ytauth, playlist_name, playlist_description)
            print(yttools.playlist_id_to_url(plid))
        elif menuChoice == "3":
            ytauth = yttools.yt_authentication()
            playlist_id = input("Provide Playlist ID: ")
            video_id = input("Provide video ID")
            yttools.add_to_playlist(ytauth, playlist_id, video_id)
            print("added")
        elif menuChoice.lower() == "q":
            break
        else:
            print("Invalid Choice")