#   Endpoint for the Carosel images

#   Importing libraries
import os, uuid


from flask.views import MethodView
from flask import jsonify, request

from lib.utils.os_utils import OsUtils
from flask.lib.utils.logger_config import UtilsWatcher


#   Load the environment variables
from dotenv import load_dotenv
load_dotenv()

#   Load the logger
logger = UtilsWatcher('Photo API')
logger.file_handler()

class PhotoLibrary(MethodView):

    def __init__(self, *args, **kwargs):

        #   Initialize the logger
        self.log = logger

    async def get(self):

        #   Initialize response object
        response = {}
        oum = OsUtils()
        #   Get the request data
        #   Ensure the request is a GET request and the Authorization is valid
        if request.method == "GET" and request.headers.get('authorization') == os.getenv("Photo_Authorization"):
            
            response['status'] = 200

            #   Path to the project root
            root = oum.find_project_root()


            path = root + find_directory()
            
            self.log.info(f"Root: {root} + {path}")
            self.log.info(f"Path: {path}")

            #   Ensure the existance of the path
            if os.path.exists(path):

                response['status'] = 200
                response['images'] = []

                #   Add the images to the response object
                caption = []
                
                for i in os.listdir(f'{path}'):

                    #  Fetch description of the images
                    # caption = ReadImage().fetchDescription(i)

                    response['images'].append(
                        {
                            'id': uuid.uuid4().hex,
                            'alt': i, 'src': i,
                            'caption': caption if caption else i
                        })

                response['path'] = path

                self.log.info(f"{response['code']}")

            else:
                response['status'] = 404
                response['images'] = "No images found // Path not found"

                self.log.error(f"Images : {response['images']}\t Path:{path}")
        else:
            response['status'] = 401
            response['message'] = "Unauthorized"

            self.log.warn(f"Request: {request.headers}\n request method : {request.method}\nResponse: {response}")  

        return jsonify(response)