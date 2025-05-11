#   Github API
#   Fetching the repositories
import os, uuid, datetime

from dotenv import load_dotenv
from lib.core.base import APIConfig


from lib.utils.log_config import UtilsWatcher

#  Loading the environment variables
load_dotenv()

logger = UtilsWatcher('Github API')
logger.file_handler()

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
        self.logging = logger

        self.head = {'Content-Type': 'application/json','Authorization': f"{self.API_KEY}"}
        return

    async def FetchAPI(self, endpoint):
        """
            Fetching the repositories
            API : https://api.github.com/users/repos
        """

        #   Initialize an API call
        response = self.ApiCall(f"{self.API_URL}{endpoint}", head=self.head)
        
        #   Initialize a list
        repo = []
        
        counter = 0
        #   fetch the response
        for i in range(len(response)):

            #   Initialize a dictionary
            repoObject = {}
            repoObject['id'] = uuid.uuid4().hex
            repoObject['name'] = response[i]['name']

            repoObject['owner'] = response[i]['owner']['login']
            repoObject['description'] = response[i]['description']
            repoObject['date'] = datetime.datetime.strptime(response[i]['updated_at'], '%Y-%m-%dT%H:%M:%SZ').strftime('%d-%m-%y')
            repoObject['lang'] = [await self.fetch_languages(repoObject, f"{self.API_URL}/repos/{repoObject['owner']}/{repoObject['name']}/languages")]
            repoObject['links'] = [
                {
                    'icon': 'bi bi-code',
                    'url': response[i]['html_url'],
                }]
            if response[i]['homepage'] or response[i]['homepage'] == "None":

                repoObject['links'].append(
                    {
                        'icon':"bi bi-globe", 
                        'url':response[i]['homepage']
                    })

            repo.append(repoObject)
        self.logging.info(f"Repositories fetched successfully. {repo}")
        return repo

    async def fetch_languages(self, repo: object, endpoint: str):

        #   Request a languages les problemos
        response = self.ApiCall(endpoint, head=self.head)

        language = {}
        language['lang'] = []

        for lang, value in response.items():
        
            match(str(lang).lower()):
                case "c#":
                    lang = "CS"

                case "c++":
                    lang = "CP"
                
                case "jupyter notebook":
                    lang = "jp-nb"
                case None:
                    lang = "Unkown"

        language['lang'].append(lang)
        language['id'] = uuid.uuid4().hex

        self.logging.info(f"Languages fetched successfully. {language}")
        return language