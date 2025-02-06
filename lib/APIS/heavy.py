#   Heavy workout app API
import os, datetime
from dotenv import load_dotenv

#  Loading the environment variables
load_dotenv()

#   Custom libraries
from lib.model import APIConfig
from lib.mathlibrary import MathInterPreter 

class HeavyAPI(APIConfig):

    def __init__(self, URL = f"{os.getenv("HeavyBase")}", KEY=os.getenv("HeavyToken"), GET = "GET", POST = "POST", PUT='PUT', PATCH='PATCH', DELETE = 'DELETE'):
        self.GET = GET
        self.PUT = PUT
        self.POST = POST
        self.API_KEY = KEY
        self.API_URL = URL
        self.PATCH = PATCH
        self.DELETE = DELETE
        self.APIV = os.getenv("HeaVy")
        self.head = {"accept": "application/json", "api-key": f"{self.API_KEY}"}
    
    def FetchWorkouts(self, endpoint: str):
        """
            Fetching the workouts
        """
        
        response = ""
        session = [{"pages": self.FetchN(endpoint),}]

        # Fetch one page of workouts
        response = self.ApiCall(endpoint = f"{self.API_URL}{self.APIV}{endpoint}", head = self.head)
        
        #   Fetching the workouts
        for i in range(len(response["workouts"])):
            kake = response["workouts"][i]
            
            workout = {
                
                "title": kake['title'],
                "description": kake['description'],
                "time": datetime.datetime.strptime(kake['end_time'], '%Y-%m-%dT%H:%M:%S%z') - datetime.datetime.strptime(kake['start_time'], '%Y-%m-%dT%H:%M:%S%z'),
                "exercises": []
            }
            #  Fetching the exercises
            for j in range(len(kake['exercises'])):
                exercise = kake['exercises'][j]

                workout['exercises'] += [{
                    "title": exercise['title'],
                    "sets": []
                }]

                #   Fetching the sets
                for k in range(len(exercise['sets'])):

                    #   Fetching the sets
                    sets = exercise['sets'][k]
                    cookie = workout['exercises'][j]['sets']


                    #   Appending the sets to the exercises
                    cookie = [{
                        'reps': sets['reps'],
                        'weight_kg': sets['weight_kg'],
                        'rpe': sets['rpe']}]
                    
                    if sets['distance_meters'] != None:
                        cookie[k]['distance'] = sets['distance_meters']
                        cookie[k]['duration'] = (int(sets['duration_seconds']) / 60 ) / 60
                        cookie[k]['pace'] = MathInterPreter().SpeedCalculation(float(cookie[k]['distance']),float(cookie[k]['duration']))
            
            session.append(workout)
            
        return session

    def FetchN(self, endpoint: str):

        return self.ApiCall(endpoint = f"{self.API_URL}{self.APIV}{endpoint}", head = self.head)
