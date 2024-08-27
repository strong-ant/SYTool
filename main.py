from spotifyToYT import SpotifyTools
from youtubeTools import YouTubeTools
import tkinter as tk

if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    sptools = SpotifyTools()
    yttools = YouTubeTools()

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
            sptools.playlist()
        elif menuChoice == "2":
            playlist_name = input("Provide a name for your playlist: ")
            playlist_description = input("Provide a description for your playlist: ")
            ytauth = yttools.yt_authentication()
            plid = yttools.create_youtube_playlist(ytauth, playlist_name, playlist_description)
            print(yttools.playlist_id_to_url(plid))
        elif menuChoice.lower() == "q":
            break
        else:
            print("Invalid Choice")