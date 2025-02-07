#   Index page

#   Importing libraries
import asyncio, os, uuid

from dotenv import load_dotenv
from flask.views import MethodView
from flask import jsonify, request

from lib.utility.utilitytools import UtilityTools

class PhotoLibrary(MethodView):

    def __init__(self, *args, **kwargs):
        pass

    async def post(self):

        #   Initialize response object
        response = {}

        #   Get the request data
        
        data = request.get_json()

        #  ensure the request is a GET request and the token is valid
        if request.method == "POST" and data['Authorization'] == os.getenv("Home-Token"):

            
            response['status'] = 200

            
            path = "static/img/carosel/"
            
            #   Ensure the existance of the path
            if os.path.exists(path):

                response['images'] = {}
                
                #   Add the images to the response object
                f = os.listdir(path)
                response['images']['id'] = [uuid.uuid4().hex for i in range(len(f))]
                response['images']['alt'] = [f]
                response['images']['sources'] = [f]
                response['images']['caption'] = ""

                
            else:
                response['status'] = 404
                response['images'] = "No images found"
        else:
            response['status'] = 401
            response['message'] = "Unauthorized"
        
        return jsonify(response)