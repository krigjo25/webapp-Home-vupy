#   Google API class
import os
from dotenv import load_dotenv

import google.oauth2.credentials
import google_auth_oauthlib.flow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

load_dotenv()

from core import APIConfig

class GoogleLibraryAPI(APIConfig):

    """ Google Library API Configuration 

        API : https://www.googleapis.com/auth/
    """

    def __init__(self, URL=os.getenv("GoogleLibAPI"), GET="GET", POST="POST", PUT='PUT', PATCH='PATCH', DELETE='DELETE', KEY=os.getenv('ClientSecret')):
        super().__init__(GET, POST, PUT, PATCH, DELETE)
        self.GET = GET
        self.PUT = PUT
        self.POST = POST
        self.API_KEY = KEY
        self.API_URL = URL
        self.PATCH = PATCH
        self.DELETE = DELETE
        self.Scopes = ['https://www.googleapis.com/auth/photoslibrary.readonly']
        self.head = {'Content-Type': 'application/json','Authorization': f"{self.API_KEY}"}
        return
    
    def get_credentials(self):
        """
            Get the credentials
        """
        return google_auth_oauthlib.flow.Flow.from_client_secrets_file("google_auth_credentials.json",
        self.Scopes)
    def  fetch_photos(self):
        service = build('photoslibrary', 'v1', credentials=self.get_credentials())
        results = service.mediaItems().list(pageSize=10).execute()
        items = results.get('mediaItems', [])

        if not items:
            print('No photos found.')
            return
        
        else:
            print('Photos:')
            for item in items:
                print(u'{0} ({1})'.format(item['filename'], item['id']))
        
        return
        """
            Fetching the photos
            API : https://www.googleapis.com/auth/
        """
