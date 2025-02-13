#   Github API
#   Fetching the repositories
import os, logging,datetime

from lib.model import APIConfig
from dotenv import load_dotenv

from lib.utility.logger import ApiWatcher
#  Loading the environment variables
load_dotenv()

class GithubAPI(APIConfig):

    """ Github API Configuration
        API : https://api.github.com/
    """

    def __init__(self, URL=os.getenv("GithubBase"), GET="GET", POST="POST", PUT='PUT', PATCH='PATCH', DELETE='DELETE', KEY=os.getenv('GithubToken')):
        super().__init__(GET, POST, PUT, PATCH, DELETE)
        self.GET = GET
        self.PUT = PUT
        self.POST = POST
        self.API_URL = URL
        self.PATCH = PATCH
        self.API_KEY = KEY
        self.DELETE = DELETE

        self.log = ApiWatcher()
        self.log.FileHandler()

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
        repoObject = {}

        #   fetch the response
        for i in range(len(response)):

            #   Structure the items from github
            repoObject['lang'] = []
            repoObject['name'] = response[i]['name']
            repoObject['url'] = response[i]['html_url']
            repoObject['owner'] = response[i]['owner']['login']
            repoObject['description'] = response[i]['description']
            repoObject['date'] = datetime.datetime.strptime(response[i]['created_at'], '%Y-%m-%dT%H:%M:%SZ').strftime('%d-%m-%y')

            
            if response[i]['homepage'] != '':
                repoObject['web_link'] = response[i]['homepage']

            #   Fetch repo languages
            repoObject['lang'] = await self.fetch_languages(repoObject, f"{self.API_URL}/repos/{repo[i]['owner']}/{repo[i]['name']}/languages")

            repo.append(repoObject)

        self.log.info(f"Repositories fetched successfully.")
        return repo

    async def fetch_languages(self, repo: list, endpoint: str):

        #   Request a languages les problemos
        response = self.ApiCall(endpoint, head=self.head)

        for lang, value in response.items():
        
            match(str(lang).lower()):
                case "c#":
                    lang = "CS"
                
                case None:
                    lang = "Uknown"

            repo['lang'] += [lang]


        return repo['lang']