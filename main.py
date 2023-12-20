from youtubeDownload import YouTubeDownloader
from spotifyToYT import SpotifyTools
import tkinter as tk

if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    downloader = YouTubeDownloader()
    sptools = SpotifyTools()

    print("Welcome to SYTool")
    print("-----------------")

    #Main Menu
    while True:
        print("\nPlease make a choice: ")
        print("1. Download YouTube video or audio")
        print("2. Spotify playlist to YouTube")
        print("q to quit")
        menuChoice = input("\n")

        if menuChoice == "1":
            downloader.download_menu()
        elif menuChoice == "2":
            sptools.playlist()
        elif menuChoice == "3":
            sptools.ytsearch()
        elif menuChoice.lower() == "q":
            break
        else:
            print("Invalid Choice")