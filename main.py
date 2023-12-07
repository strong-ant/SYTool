from youtubeDownload import YouTubeDownloader
import tkinter as tk
from tkinter import filedialog

def open_save_location():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Saving to: {folder}")
    return folder

if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    downloader = YouTubeDownloader()

    video_url = input("Enter URL:")
    save_path = open_save_location()

    if save_path:
        print("Downloading...")
        downloader.download_video_mp4(video_url, save_path)
    else:
        print("Invalid Directory")