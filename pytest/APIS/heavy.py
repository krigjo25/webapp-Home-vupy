import os
from dotenv import load_dotenv

load_dotenv()

from core import APIConfig

class HeavyAPI(APIConfig):

    def __init__(self, URL = f"{os.getenv("HeavyBase")}", KEY=os.getenv("HeavyToken"), GET = "GET", POST = "POST", PUT='PUT', PATCH='PATCH', DELETE = 'DELETE'):
        self.GET = GET
        self.POST = POST
        self.PUT = PUT
        self.PATCH = PATCH
        self.DELETE = DELETE
        self.API_KEY = KEY
        self.API_URL = URL
        self.head = {"accept": "application/json", "api-key": f"{self.API_KEY}"}


    