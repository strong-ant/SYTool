from pytube import YouTube
from tkinter import filedialog

class YouTubeDownloader:
    def download_video_mp4(self, url, path):
        try:
            video = YouTube(url)
            #retrieve all video streams for a video
            streams = video.streams.filter(progressive=True, file_extension="mp4")
            #select highest resolution
            highest_res = streams.get_highest_resolution()
            highest_res.download(output_path=path)
            print("Downloaded Successfully")
        except Exception as e:
            print(e)
    def download_audio(self, url, path):
        try:
            video = YouTube(url)
            #select all audio streams
            audio_streams = video.streams.filter(only_audio=True)
            #download highest bitrate
            #highest_bitrate = audio_streams.get_audio_only().order_by('bitrate').desc().first()
            #highest_bitrate.download(output_path=path)
        except Exception as e:
            print(e)

    def open_save_location(self):
        folder = filedialog.askdirectory()
        if folder:
            print(f"Saving to: {folder}")
        return folder

