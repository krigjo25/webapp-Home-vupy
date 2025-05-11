#   Endpoint for the Carosel images

#   Importing libraries
import os, uuid


from flask.views import MethodView
from flask import jsonify, request

from lib.utils.os_utils import OsUtils
from lib.utils.logger_config import APIWatcher
from lib.utils.exception_handler import NotFoundError
from flask.app import HTTPException

#   Load the environment variables
from dotenv import load_dotenv
load_dotenv()

#   Load the logger
logger = APIWatcher(dir="logs", name='Photo-API')
logger.file_handler()

class PhotoLibrary(MethodView):

    async def get(self):

        #   Initialize response object
        response = {}
        oum = OsUtils()
        logger.warn(f"Request: {request.headers}\n request method : {request.method}\n")

        try:
            if request.method == "GET" and request.headers.get('authorization') == os.getenv("Photo_Authorization"):
                
                response['status'] = 200

                #   Path to the project root
                root = oum.find_project_root()
                path = root + oum.find_directory(request.headers.get('path'))
                
                logger.info(f"Root: {root}\n{path}")

                #   Ensure the existance of the path
                try:

                    if os.path.exists(path):

                        response['status'] = 200
                        response['images'] = []

                        caption = [] # remove this line if you want to fetch the description of the images
                        for i in os.listdir(path):

                            #  Fetch description of the images
                            
                            # caption = ReadImage().fetchDescription(i)

                            response['images'].append(
                                {
                                    'id': uuid.uuid4().hex,
                                    'alt': i, 'src': i,
                                    'caption': caption if caption else i
                                })

                        response['path'] = path

                        logger.info(response)

                    else:
                        raise NotFoundError(404, "Path not found", path)
                        
                except NotFoundError as e:
                    response['error'] = e.message
                    response['status'] = e.status_code
                    
                    logger.error(f"Images : {response['error']}\t Path:{path}")


        except Exception as e:
            response['status'] = e.status_code
            response['message'] = e.message

            logger.error(f"Error code: {e.status_code}\nError message: {e.message}\nRequest: {request.headers}\nRequest method : {request.method}\n")
        
        return jsonify(response)