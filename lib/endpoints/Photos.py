#   Endpoint for the Carosel images

#   Importing libraries
import os, uuid

from dotenv import load_dotenv
from flask.views import MethodView
from flask import jsonify, request

from lib.utility.logger import ApiWatcher

#   Load the environment variables
load_dotenv()

class PhotoLibrary(MethodView):

    def __init__(self, *args, **kwargs):

        #   Initialize the logger
        self.log = ApiWatcher()
        self.log.FileHandler()

    async def get(self):

        #   Initialize response object
        response = {}

        #   Get the request data
        #   Ensure the request is a GET request and the Authorization is valid
        if request.method == "GET" and request.headers.get('Authorization') == os.getenv("Photo_Authorization"):
            
            response['status'] = 200

            #   Path to the images
            path = "/src/assets/img/carosel/"


            #   Ensure the existance of the path
            if os.path.exists('VueClient' + path):

                response['code'] = 200
                response['images'] = []

                
                #   Add the images to the response object
                caption = []
                
                for i in os.listdir(f'VueClient{path}'):

                    #  Fetch description of the images
                    #caption = ReadImage().fetchDescription(i)
                    #   Add the image to the response object
                    response['images'].append({
                    'id': uuid.uuid4().hex,
                    'alt': i, 'src': i,
                    'caption': caption if caption else i
                    
                    })
                response['status'] = 200
                response['path'] = path

                self.log.info(f"{response['code']}")
            else:
                response['status'] = 404
                response['images'] = "No images found"

                self.log.error(f"Images : {response['images']}\t Path:{path}")
        else:
            response['status'] = 401
            response['message'] = "Unauthorized"

            self.log.error(f"Request: {request.headers}")  

        return jsonify(response)