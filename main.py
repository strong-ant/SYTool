from youtubeDownload import YouTubeDownloader
import tkinter as tk

if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    downloader = YouTubeDownloader()

    video_url = input("Enter URL:")
    save_path = "D:\Programs\pythonProjects\SYTool"
    downloader.download_video_mp4(video_url, save_path)

