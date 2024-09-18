import os
import json
import logging
import requests

from dotenv import load_dotenv
from requests.exceptions import HTTPError, ConnectionError, Timeout, RequestException

load_dotenv()

class APIConfig():
    def __init__(self, URL, KEY=None, GET = "GET", POST = "POST", PUT='PUT', PATCH='PATCH', DELETE = 'DELETE'):
        self.GET = GET
        self.POST = POST
        self.PUT = PUT
        self.PATCH = PATCH
        self.DELETE = DELETE
        self.API_KEY = KEY
        self.API_URL = URL

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

class GithubApi(APIConfig):

    def __init__(self, URL, GET="GET", POST="POST", PUT='PUT', PATCH='PATCH', DELETE='DELETE', KEY=os.getenv('GITHUB_TOKEN')):
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


    
    def fetch_repos(self):
        

        #   Create a connection to github
        response = self.ApiCall(self.API_URL, headers=self.head)
        
        #   Fetch repo languages
        def fetch_languages(repo: list, parse: str):

            #   Request a languages
            response = self.ApiCall(parse, headers= self.head)

            for lang, value in response.items():
                if lang: repo['lang'] += [lang] 
            return

         #   Intializing a list
        repo = []

        for i in range(len(response)):

            #   Structure the items from github
            repo += [{"name":response[i]['name'], "url":response[i]['html_url'], 'owner':response[i]['owner']['login'], 'lang': []}]
            #lambda?
            #   Fetch repo languages
            ##fetch_languages(repo[i], self.API_URL + "{repo[i]['owner']}/{repo[i]['name']}/languages")
