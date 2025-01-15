#  Performace Testing for the API's
import pytest, os, time
from unittest.mock import patch

from APIS.heavy import HeavyAPI
from APIS.github import GithubAPI

class TestResponsesAPI:

    def test_FetchReposPerformance(self)-> None:
        """
            #   Testing  the Performance of fetch_repos
            #   The time complexity for this test is O(1*repositories) which equals
            #   Which equals 
        """
        
        start = time.perf_counter()

        #   Initializing Requests module
        api = GithubAPI()

        for i in range(1000):
            
            #   Actual response from the Api Call
            response = api.ApiCall(endpoint = f"{api.API_URL}user/repos", head = api.head)
        
        print(f"Time taken to fetch 100 * x repos: {time.perf_counter() - start}")

        

    def test_fetchWorkoutPerformance(self)-> None:
       
        """
        
            #    Testing  the performance of fetch_workouts
            #    The time complexity for this test is O(3*workout log) which equals
            #    Which equals 
        """

        #   Initializing Requests module
        HAPI = HeavyAPI()

        #   Actual response from the Api Call
        start = time.perf_counter()
        
        for i in range(1000):
            response = HAPI.FetchWorkouts(os.getenv("Workouts"))

        print(f"Time taken to fetch 100 * x workouts: {time.perf_counter() - start}")