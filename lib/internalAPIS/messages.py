#   Index page

#   Importing libraries
from datetime import datetime
from dotenv import load_dotenv
from flask.views import MethodView
from flask import jsonify, request

#   Custom dependencies
from lib.utility.utilitytools import UtilityTools


#   Load environment variables
load_dotenv()

class Announcements(MethodView):

    #   Initialize methods and database
    methods = ["GET"]

    def __init__(self, *args, **kwargs) -> None:
        super().__init__()

            
    async def get(self): 
        tools = UtilityTools()
        response = {}

        if request.method == "GET":
            response['announcement'] = f"{tools.Announcements(datetime.now())}"

        return jsonify(response)


