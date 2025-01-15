#   Importing repositories
import os
import logging
import requests
import datetime

from time import perf_counter
from dotenv import load_dotenv
load_dotenv()

#   errorHandler
#from lib.database import SQL

#   Requests repositories
from requests.exceptions import HTTPError, ConnectionError, Timeout, RequestException

#   Configuring the logger
logging.basicConfig(
    level=logging.DEBUG, 
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
    handlers=[logging.FileHandler("app.log"), 
              logging.StreamHandler()])

class APIConfig(object):

    def __init__(self, URL, KEY=None, GET = "GET", POST = "POST", PUT='PUT', PATCH='PATCH', DELETE = 'DELETE'):
        self.GET = GET
        self.POST = POST
        self.PUT = PUT
        self.PATCH = PATCH
        self.DELETE = DELETE
        self.API_KEY = KEY
        self.API_URL = URL

    def ApiCall(self, endpoint: str, head: dict):
        """
            Calling the API
        """
        start = perf_counter()

        try:
            r = requests.get(f"{endpoint}", timeout=30, headers=head)

            if r.status_code in [200, 201]:
                
                logging.warning(f"request code :{r.status_code} Time elapsed: {perf_counter()-start}")
                return r.json()
            if r.status_code in [401, 403]: raise ConnectionError('Unauthorized Access')
            elif r.status_code in [404]: raise HTTPError('Resource not found')     
        except (HTTPError, ConnectionError, Timeout, RequestException) as e: 
            logging.error(f"An error occured while attempting to call the api\n request code :{r.status_code}\n, Time elapsed: {perf_counter()-start}")

        return r.status_code