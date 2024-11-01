#   Importing repositories
import os
import sqlite3
import logging
import requests
from typing import Optional,Tuple

from dotenv import load_dotenv
load_dotenv()

#   errorHandler
from lib.database import SQL

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
        try:
            r = requests.get(f"{endpoint}", timeout=30, headers=head)
            if r.status_code in [200, 201]: return r.json()
            elif r.status_code in [401, 403]: raise ConnectionError('Unauthorized Access')
            elif r.status_code in [404]: raise HTTPError('Resource not found')
        except (HTTPError, ConnectionError, Timeout, RequestException) as e: 
            logging.error(f"An error occured while attempting to call the api{e}")

class GithubApi(APIConfig):

    def __init__(self, URL="https://api.github.com/", GET="GET", POST="POST", PUT='PUT', PATCH='PATCH', DELETE='DELETE', KEY=os.getenv('GITHUB_TOKEN')):
        super().__init__(GET, POST, PUT, PATCH, DELETE)
        self.GET = GET
        self.POST = POST
        self.PUT = PUT
        self.PATCH = PATCH
        self.DELETE = DELETE
        self.API_KEY = KEY
        self.API_URL = URL
        self.head = {'Content-Type': 'application/json','Authorization': f"{self.API_KEY}"}
       
        return

    def fetch_repos(self):
        """
            Fetching the repositories
            API : https://api.github.com/
        """
        #   Fetch repo languages
        def fetch_languages(repo: list, parse: str):

            #   Request a languages
            response = self.ApiCall(parse, head=self.head)

            for lang, value in response.items():
                if lang: repo[i]['lang'] += f"{lang},"

            #   Sweep data
            del response, repo, parse
            return

         #   Intializing a list
        
        #   Initialize an API call
        response = self.ApiCall(f"{self.API_URL}user/repos", head=self.head)
        
        #   Initialize a list
        repo = []

        for i in range(len(response)):

            #   Structure the items from github
            repo += [{"name":response[i]['name'], "description":str(response[i]['description']), "url":response[i]['html_url'], 'owner':response[i]['owner']['login'], 'lang':"", 'date':response[i]['created_at']}]
            
            #   Fetch repo languages
            fetch_languages(repo, f"{self.API_URL}/repos/{repo[i]['owner']}/{repo[i]['name']}/languages")

        logging.info(f"Fetching repositories: {repo}")
        return repo

class InitializeData():

    def __init__(self, db: str):
        self.sql = SQL(db)
        self.tables = self.sql.select_records('sqlite_master', 'SELECT')


    def upsert_data(self, table: str, repo: list):

        """
            Initializing the data by fetching the repositories from the API
            and Ensures the database is up to date
        """
        
        #   Initializing variables
        data = {}
        columns = []
        self.create_table(table, repo)
        self.sql.initialize_records(table, repo)

    def create_table(self, table: str, repo: list):

            """
                Creates a table and insert data into the table
            """
            #   Initializing the data
            data = {}
            columns = []

            #    Initializing columns
            columns = [key for key in repo[0].keys()]

            for column in columns:

                #   Ensure that the id is not in columns
                if "id" not in columns:
                    data["id"] = 'INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT'
                
                #   Ensure that the column is a date
                if 'date' == column:
                    data[column] = "INTEGER NOT NULL DEFAULT (strftime('%s', 'now')"
                
                if column == 'name':
                    data[column] = "TEXT NOT NULL UNIQUE"
            
                else:
                    data[column] = "TEXT NOT NULL DEFAULT 'None'"

            #   Create table
            print(data)
            self.sql.TableConfigurations(table, "CREATE", columns=data)