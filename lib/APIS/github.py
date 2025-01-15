#   Github API
#   Fetching the repositories
import os, logging,requests,datetime

from lib.model import APIConfig
from time import perf_counter
from dotenv import load_dotenv
load_dotenv()

#   Configuring the logger
logging.basicConfig(
    level=logging.DEBUG, 
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
    handlers=[logging.FileHandler("app.log"), 
              logging.StreamHandler()])

class GithubAPI(APIConfig):

    """ Github API Configuration 
        API : https://api.github.com/
    """

    def __init__(self, URL=os.getenv("GithubBase"), GET="GET", POST="POST", PUT='PUT', PATCH='PATCH', DELETE='DELETE', KEY=os.getenv('GithubToken')):
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

    async def FetchApiJson(self, endpoint):
        """
            Fetching the repositories
            API : https://api.github.com/users/repos
        """
        #   Initialize an API call
        response = self.ApiCall(f"{self.API_URL}{endpoint}", head=self.head)
        
        #   Initialize a list
        repo = []

        #   fetch the response
        for i in range(len(response)):

            #   Structure the items from github
            repo += [
                {
                "lang":[],
                "name":response[i]['name'], 
                "description":str(response[i]['description']), 
                "url":response[i]['html_url'],                
                "owner":response[i]['owner']['login'],
                "date":datetime.datetime.strptime(response[i]['created_at'], '%Y-%m-%dT%H:%M:%SZ').strftime('%d-%m-%y')
                }]
            
            #   Fetch repo languages
            repo['lang'] = await self.fetch_languages(repo, f"{self.API_URL}/repos/{repo[i]['owner']}/{repo[i]['name']}/languages")

        return repo

    async def fetch_languages(self, repo: list, endpoint: str):

        #   Request a languages
        response = self.ApiCall(endpoint, head=self.head)

        for lang, value in response.items():
            
            if lang: 
                repo['lang'] += f"{lang},"

        return repo['lang']