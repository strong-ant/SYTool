from youtubeDownload import YouTubeDownloader
import tkinter as tk

if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    downloader = YouTubeDownloader()

    print("Welcome to SYTool")
    print("-----------------")

    #Main Menu
    while True:
        print("\nPlease make a choice: ")
        print("1. Download YouTube video or audio")
        print("q to quit")
        menuChoice = input("\n")

        if menuChoice == "1":
            downloader.downloadMenu()
        elif menuChoice.lower() == "q":
            break
        else:
            print("Invalid Choice")