import os
import json
import logging
import requests

from dotenv import load_dotenv
from requests.exceptions import HTTPError, ConnectionError, Timeout, RequestException

load_dotenv()

class Config():
    def __init__(self, GET = "GET", POST = "POST", PUT='PUT', PATCH='PATCH', DELETE = 'DELETE', KEY = None, URL = None):
        self.GET = GET
        self.POST = POST
        self.PUT = PUT
        self.PATCH = PATCH
        self.DELETE = DELETE
        self.API_KEY = KEY
        self.API_URL = URL

class GithubApi(Config):

    def __init__(self, GET="GET", POST="POST", PUT='PUT', PATCH='PATCH', DELETE='DELETE', KEY=os.getenv('GITHUB_TOKEN'), URL="https://api.github.com/user"):
        super().__init__(GET, POST, PUT, PATCH, DELETE)
        self.GET = GET
        self.POST = POST
        self.PUT = PUT
        self.PATCH = PATCH
        self.DELETE = DELETE
        self.API_KEY = KEY
        self.API_URL = URL
        self.head = {'Content-Type': 'application/json','Authorization': f"{self.API_KEY}"}

        return

    def ApiCall(self, endpoint: str, header: dict | str = None) -> str:
        """
         Calling the API
        """
        try:
            r = requests.get(f"{endpoint}", timeout=30, headers=header)

            if r.status_code in [200, 201]: return r.json()
            elif r.status_code in [401, 403]: return json.dumps({"Error": "Encountered an AUTHORIZATION Error"})
            
        except (HTTPError, ConnectionError, Timeout, RequestException) as e: 
            logging.error(e)
        return
    

    def mock_requests():

        #   Ensure that The data which is requested 

        pass
