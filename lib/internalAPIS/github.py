#   Endpoint for the Github repositories

#   Importing libraries
import os
from dotenv import load_dotenv
from flask.views import MethodView
from flask import jsonify, request


from lib.APIS.github import GithubAPI


#   Load environment variables
load_dotenv()

class Github(MethodView):
    def __init__(self, *args, **kwargs):
        pass
    async def get(self):
        response = {}

        if request.method == "GET":
            count = 0
            response['data'] = await GithubAPI().FetchAPI(os.getenv('GithubRepos'))
            response['status'] = 200

            for i in range(len(response['data'])):
                if i % 9 == 0:
                    count += 1
                    response['page'] = count

        return jsonify(response)

