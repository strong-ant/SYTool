from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.errors import HttpError
import os
import pickle
from config import YOUTUBE_API_KEY

youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

#Scopes needed for creating and managing YouTube playlists
SCOPES = ["https://www.googleapis.com/auth/youtube"]



class YouTubeTools:
    
    def yt_authentication(self):
        #Authenticate the user and return a youtube service object
        credentials = None
        
        # Check if the token.pickle file already exists (this stores the user's credentials)
        if os.path.exists("token.pickle"):
            with open("token.pickle", "rb") as token:
                credentials = pickle.load(token)
                
         # If there are no valid credentials available, prompt the user to log in
        if not credentials or not credentials.valid:
            if credentials and credentials.expired and credentials.refresh_token:
                credentials.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file('client_secret.json', SCOPES)
                credentials = flow.run_local_server(port = 0)
                
        # Save the credentials for the next run
        with open("token.pickle", "wb") as token:
            pickle.dump(credentials, token)
            
        # Build the YouTube service object
        youtube = build('youtube', 'v3', credentials=credentials)
        return youtube
        
        
    def create_youtube_playlist(self, youtube, title, description):
        try:
            request = youtube.playlists().insert(
                part="snippet,status",
                body={
                    "snippet": {
                        "title": title,
                        "description": description
                    },
                    "status": {
                        "privacyStatus": "private"  # Can be "private", "public", or "unlisted"
                    }
                }
            )
            response = request.execute()
            return response['id']
        except HttpError as e:
            print(f"An error occurred: {e}")
        return None
    
    @staticmethod
    def playlist_id_to_url(id) -> str:
        playlist_url = f"https://www.youtube.com/playlist?list={id}"
        return playlist_url
        
    
    
    def ytsearch(self):
        query = input("Enter a video name:\n")
        request = youtube.search().list(
            part = 'snippet',
            q = query,
            type = "video",
            maxResults = 1,
        )
        response = request.execute()
        if 'items' in response and len(response['items']) > 0:
            video_id = response['items'][0]['id']['videoId']
            video_link = f"https://www.youtube.com/watch?v={video_id}"
            print(video_link)
        else:
            print("none")