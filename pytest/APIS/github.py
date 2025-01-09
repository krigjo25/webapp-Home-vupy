#   Github API
import os

from core import APIConfig
from dotenv import load_dotenv

load_dotenv()

class GithubApi(APIConfig):

    """ Github API Configuration 
        API : https://api.github.com/
    """

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

    def fetch_repos(self):
        """
            Fetching the repositories
            API : https://api.github.com/
        """
        #   Fetch repo languages
        def fetch_languages(repo: list, parse: str):

            #   Request a languages
            response = self.ApiCall(parse, head=self.head)

            for lang, value in response.items():
                if lang: repo[i]['lang'] += f"{lang},"

            #   Sweep data
            del response, repo, parse
            return

         #   Intializing a list
        
        #   Initialize an API call
        response = self.ApiCall(f"{self.API_URL}user/repos", head=self.head)
        
        #   Initialize a list
        repo = []

        for i in range(len(response)):

            #   Structure the items from github
            repo += [{"name":response[i]['name'], "description":str(response[i]['description']), "url":response[i]['html_url'], 'owner':response[i]['owner']['login'], 'lang':"", 'date':response[i]['created_at']}]
            
            #   Fetch repo languages
            fetch_languages(repo, f"{self.API_URL}/repos/{repo[i]['owner']}/{repo[i]['name']}/languages")
