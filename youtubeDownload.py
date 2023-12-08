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
            audio_streams = video.streams.filter(only_audio=True)  #select all audio streams

            #download highest bitrate
            highest_bitrate = None
            for stream in audio_streams:
                if stream.abr: #if a bitrate is found
                    if highest_bitrate:
                        bitrate = int(''.join(filter(str.isdigit, stream.abr))) #extract bitrate int
                        if bitrate > int(''.join(filter(str.isdigit,highest_bitrate.abr))): #check if bitrate is higher than highest_bitrate's
                            highest_bitrate = stream
                    else:
                        highest_bitrate = stream

            highest_bitrate.download(output_path=path)
            print(f"Downloaded Successfully highest bitrate audio of {highest_bitrate.abr}")
        except Exception as e:
            print(e)

    def open_save_location(self):
        folder = filedialog.askdirectory()
        if folder:
            print(f"Saving to: {folder}")
        return folder
    def downloadMenu(self):
        while True:
            userInput = input("Enter a URL or q for Main Menu\n")

            if userInput.lower() == 'q':
                break
            else:
                video_url = userInput
                fileChoice = input("Enter 1 for video, 2 for audio\n")
                if fileChoice != "1" and fileChoice != "2":
                    print("Invalid Choice")
                    break
                else:
                    save_path = self.open_save_location()
                    if save_path:
                        print("Downloading...")
                        if fileChoice == "1":
                            self.download_video_mp4(video_url, save_path)
                        else:
                            self.download_audio(video_url, save_path)
                    else:
                        print("Invalid Directory")




