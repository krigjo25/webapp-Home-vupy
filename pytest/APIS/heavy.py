import os, json
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
        self.APIV = os.getenv("HeaVy")
        self.head = {"accept": "application/json", "api-key": f"{self.API_KEY}"}
    
    def FetchPages(self, endpoint: str):
        """
            Fetching the workouts
        """

        response = ""
        workout = {}

        for key, value in self.ApiCall(endpoint = f"{self.API_URL}{self.APIV}{endpoint}{i}", head = self.head).items():
                
            if key != "workout":
                workout[key] = value
    
        #return response

    def FetchN(self, endpoint: str):

        return self.ApiCall(endpoint = f"{self.API_URL}{self.APIV}{endpoint}", head = self.head)["workout_count"]

    