#   Index page

#   Importing libraries
import asyncio, os, json as j

from datetime import datetime
from dotenv import load_dotenv
from flask.views import MethodView
from flask import jsonify, request


from lib.APIS.heavy import HeavyAPI
from lib.APIS.github import GithubAPI
from lib.utility.utilitytools import UtilityTools


#   Load environment variables
load_dotenv()

class Github(MethodView):
    def __init__(self, *args, **kwargs):
        pass
    async def get(self):
        response = {}

        if request.method == "GET":
            count = 0
            response['github'] = await GithubAPI().FetchAPI(os.getenv('GithubRepos'))
            response['status'] = 200

            for i in range(len(response['github'])):
                if i % 3 == 0:
                    count += 1
                    response['page'] = count

        return jsonify(response)

