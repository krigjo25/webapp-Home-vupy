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
        announcement = tools.Announcements(datetime.now())

        if request.method == "GET" and announcement:

            response['announcement'] = f"{announcement}"

        return jsonify(response)


