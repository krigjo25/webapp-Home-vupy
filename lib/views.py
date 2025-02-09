#   Index page

#   Importing libraries
import asyncio, os

from dotenv import load_dotenv
from flask.views import MethodView
from flask import jsonify, request

from lib.APIS.heavy import HeavyAPI
from lib.APIS.github import GithubAPI
from lib.utility.utilitytools import UtilityTools


#   Load environment variables
load_dotenv()

class Index(MethodView):

    #   Initialize methods and database
    methods = ["GET"]

    def __init__(self, *args, **kwargs) -> None:
        super().__init__()

    async def UpdateRepo(self):

        while True:
            
            Index.repo = await GithubAPI().FetchApiJson(f"{os.getenv('GithubRepos')}")
            await asyncio.sleep(386400)
            
    async def get(self): 
        tools = UtilityTools()
        response = {"link":{}}

        if request.method == "GET":

            response['heavy'] = f"{tools.HeavyAPI()}"
            response['github-repo'] = f"{tools.GithubAPI()}"
            
            response['message'] = f"{tools.Announcements()}"

        return jsonify(response)


