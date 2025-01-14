# Testing common APIS.py
from unittest.mock import patch
from APIS.heavy import HeavyAPI
from APIS.github import GithubAPI


class TestAPI:

    """
        API testing
        Github : https://api.github.com/user/
        
        Heavy : https://api.heavy.com/
    """
    
    def test_github_connection(self)-> None:
        
        #   Testing the connection to the GithubAPI module
        with patch('APIS.github.GithubAPI') as mock:

            mock.get.return_value = '200'
            
            GAPI = GithubAPI()
            assert str(GAPI.ApiStatus(endpoint = f"{GAPI.API_URL}", head = GAPI.head)) == mock.get.return_value 

    def test_heavy_connection(self)-> None:


        #   Testing the connection to the HeavyAPI module
        with patch('APIS.github.GithubAPI') as mock:

            mock.get.return_value = '200'
            
            HAPI = HeavyAPI()
            assert str(HAPI.ApiStatus(endpoint = f"{HAPI.API_URL}", head = HAPI.head)) == mock.get.return_value 

