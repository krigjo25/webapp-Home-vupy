#   Importing repositories
import os
import time
import asyncio

import logging
import requests
import datetime

from dotenv import load_dotenv
load_dotenv()

#   errorHandler
from lib.database import SQL

#   Requests repositories
from requests.exceptions import HTTPError, ConnectionError, Timeout, RequestException

#   Configuring the logger
logging.basicConfig(
    level=logging.DEBUG, 
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
    handlers=[logging.FileHandler("app.log"), 
              logging.StreamHandler()])

class APIConfig(object):

    def __init__(self, URL, KEY=None, GET = "GET", POST = "POST", PUT='PUT', PATCH='PATCH', DELETE = 'DELETE'):
        self.GET = GET
        self.POST = POST
        self.PUT = PUT
        self.PATCH = PATCH
        self.DELETE = DELETE
        self.API_KEY = KEY
        self.API_URL = URL

    def ApiCall(self, endpoint: str, head: dict):
        """
            Calling the API
        """
        start = time.strftime('%X', time.localtime())

        try:
            r = requests.get(f"{endpoint}", timeout=30, headers=head)
            if r.status_code in [200, 201]: return r.json()
            elif r.status_code in [401, 403]: raise ConnectionError('Unauthorized Access')
            elif r.status_code in [404]: raise HTTPError('Resource not found')
        
        except (HTTPError, ConnectionError, Timeout, RequestException) as e: 
            logging.error(f"An error occured while attempting to call the api\n request code :{r.status_code}\n, Time elapsed: {time.strftime('%X', time.localtime())-start}")
        
        logging.warning(f"request code :{r.status_code} Time elapsed: {time.time()-start}")

        return

class GithubApi(APIConfig):

    def __init__(self, URL="https://api.github.com/", GET="GET", POST="POST", PUT='PUT', PATCH='PATCH', DELETE='DELETE', KEY=os.getenv('GITHUB_TOKEN')):
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

    async def fetch_repos(self):
        """
            Fetching the repositories
            API : https://api.github.com/
        """
        start = time.time()
        
        

        async def fetch_languages(repo: list, parse: str, start = time.time()):

            #   Request a languages
            response = self.ApiCall(parse, head=self.head)

            for lang, value in response.items():
                if lang:
                    repo[i]['lang'] += [lang]
                else :
                    repo[i]['lang'] += ["None"]

    
                

            logging.info(f"Languages has been fatched {repo[i]['lang']}\nTime elapsed: {time.time()-start}\n")
            return

         #   Intializing a list
        
        #   Initialize an API call
        response = self.ApiCall(f"{self.API_URL}user/repos", head=self.head)
        
        #   Initialize a list
        repo = []

        for i in range(len(response)):

            #   Structure the items from github
            repo += [
                {
                    "name":response[i]['name'], 
                    "description":str(response[i]['description']),
                    "url":response[i]['html_url'],
                    'owner':response[i]['owner']['login'],
                    'lang':[],
                    'date':datetime.datetime.strptime(response[i]['created_at'], '%Y-%m-%dT%H:%M:%SZ').strftime('%d-%M-%y')
                }]
            
            #   Fetch repo languages
            
            await fetch_languages(repo, f"{self.API_URL}/repos/{repo[i]['owner']}/{repo[i]['name']}/languages")
            
        logging.warning(f"Repo has been fatched {repo}\nTime elapsed: {time.time()-start}\n")

        return repo
