#   Index page

#   Importing libraries
import os, uuid

from dotenv import load_dotenv
from flask.views import MethodView
from flask import jsonify, request

#   Load the environment variables
load_dotenv()
class PhotoLibrary(MethodView):

    def __init__(self, *args, **kwargs):
        pass

    async def get(self):

        #   Initialize response object
        response = {}

        #   Get the request data
        #   Ensure the request is a GET request and the Authorization is valid
        if request.method == "GET" and request.headers.get('Authorization') == os.getenv("Photo_Authorization"):
            
            response['status'] = 200

            #   Path to the images
            path = "/src/assets/img/carosel/"
            print(path)
            #   Ensure the existance of the path
            if os.path.exists('VueClient'+path):

                response['images'] = []
                
                #   Add the images to the response object
                for i in os.listdir(f'VueClient{path}'):

                    response['images'].append({
                    'id': uuid.uuid4().hex,
                    'alt': i, 'src': i,
                    })
                    #if:
                    #    response['images']['caption'] = i.caption
                response['status'] = 200
                response['path'] = path

                
            else:
                response['status'] = 404
                response['images'] = "No images found"
        else:
            response['status'] = 401
            response['message'] = "Unauthorized"

        return jsonify(response)