import os
import json
import logging
import requests
import sqlite3

from dotenv import load_dotenv
from requests.exceptions import HTTPError, ConnectionError, Timeout, RequestException

load_dotenv()

class Databases():
    def __init__(self, database:str, port:int | int=None, host:str | str=None, statement:str | str = None):

        #   Ensure there is one value
        self.host = host
        self.port = port
        self.db = database
        self.method = statement
        self.connected = False

        del host, database, port, statement
        return
    
    def configure_query(self,  table:str, statement:str, columns: tuple | tuple=None):

        column = ""
        
        if bool(columns):
            for i in range(len(columns)):
                column += f"{columns[i]}"

                #   Ensure that the tuple does not exceed its limits
                if i < len(columns): column += ", "

                else: columns = '*'

        if statement.upper() == "SELECT":
            
            query = f"{statement}{columns} FROM {table}"

        return query

class SQL(Databases):
        def __init__(self, database:str, port:int | int=None, host:str | str=None, method:str | str = None):
            super().__init__(database, port, host, method)
        
            #   Establish the connection to the database
            try:

                self.conn = sqlite3.connect(self.db)
                if not self.conn: raise Exception('Could not establish a connection to the database')

            except Exception as e: return e

            self.connected = True

            #   Initializing the sqlite cursor
            self.cur = self.conn.cursor()
            

            return print('Established connection to the Database')
        
        def selectRecords(self, table:str, statement:str, columns:tuple):
            return self.cur.execute(self.configure_query(self, table, statement, columns))

class APIConfig():
    def __init__(self, URL, KEY=None, GET = "GET", POST = "POST", PUT='PUT', PATCH='PATCH', DELETE = 'DELETE'):
        self.GET = GET
        self.POST = POST
        self.PUT = PUT
        self.PATCH = PATCH
        self.DELETE = DELETE
        self.API_KEY = KEY
        self.API_URL = URL

    def ApiCall(self, endpoint: str, header: dict | str = None) -> str:
        """
            Calling the API
        """
        try:
            r = requests.get(f"{endpoint}", timeout=30, headers=header)

            if r.status_code in [200, 201]: return r.json()
            elif r.status_code in [401, 403]: return json.dumps({"Error": "Encountered an AUTHORIZATION Error"})
            
        except (HTTPError, ConnectionError, Timeout, RequestException) as e: 
            logging.error(e)
        return

class GithubApi(APIConfig):

    def __init__(self, URL, GET="GET", POST="POST", PUT='PUT', PATCH='PATCH', DELETE='DELETE', KEY=os.getenv('GITHUB_TOKEN')):
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
        

        #   Create a connection to github
        response = self.ApiCall(self.API_URL, headers=self.head)
        
        #   Fetch repo languages
        def fetch_languages(repo: list, parse: str):

            #   Request a languages
            response = self.ApiCall(parse, headers= self.head)

            for lang, value in response.items():
                if lang: repo['lang'] += [lang] 
            return

         #   Intializing a list
        repo = []

        for i in range(len(response)):

            #   Structure the items from github
            repo += [{"name":response[i]['name'], "url":response[i]['html_url'], 'owner':response[i]['owner']['login'], 'lang': []}]
            #lambda?
            #   Fetch repo languages

