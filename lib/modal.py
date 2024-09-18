#   Import the responsories
import sqlite3
import os
import json
import logging

import requests
from requests.exceptions import HTTPError, ConnectionError, Timeout, RequestException

    
class APIConfig():
    def __init__(self, URL: str, KEY :dict = None, GET ="GET", POST = "POST", PUT='PUT', PATCH='PATCH', DELETE = 'DELETE'):
        self.GET = GET
        self.POST = POST
        self.PUT = PUT
        self.PATCH = PATCH
        self.DELETE = DELETE
        self.API_KEY = KEY
        self.API_URL = URL
    
    def ApiCall(self, endpoint: str, head: dict = None) -> str:
        """
         Calling the API
        """
        try:
            #   Request something from endpoint
            r = requests.get(f"{endpoint}", timeout=30, headers=head)

            #   Ensure that the r.status_code has a specified code
            if r.status_code in [200, 201]: return r.json()
            elif r.status_code in [401, 403]: return json.dumps({"Error": "Encountered an AUTHORIZATION Error. You do not have the Autorized permission to process"})
            elif r.status_code == 400: return json.dumps({"Client Error": "The server would not process the request due to the request is considered to be a client error. It could be one of the following : Malformed request syntax, invalid request message framing, or deceptive request routing"})
            
        except (HTTPError, ConnectionError, Timeout, RequestException) as e: 
            logging.error(e)

        return


class Github(APIConfig):

    """Configure the API to fetch apis from Github"""
    def __init__(self, URL: str, KEY: dict = None, GET="GET", POST="POST", PUT='PUT', PATCH='PATCH', DELETE='DELETE'):
        super().__init__(URL, KEY, GET, POST, PUT, PATCH, DELETE)
        self.API_KEY = KEY
        self.API_URL = URL
        self.head = {'Content-Type': 'application/json','Authorization': f"{self.API_KEY}"}

        return
    
    def fetch_repos(self):

        """ Fetches repositories data"""
        #   Initialize a list
        repo = []

        #   Create a connection to github
        response = self.ApiCall(self.API_URL, headers=self.head)
        
        #   Fetch repo languages
        def fetch_languages(repo: list, parse: str):

            #   Request a languages
            response = self.ApiCall(parse, headers= self.head)

            for lang, value in response.items():
                if lang: repo['lang'] += [lang] 
            return

        for i in range(len(response)):

            #   Structure the items from github
            repo += [{"name":response[i]['name'], "url":response[i]['html_url'], 'owner':response[i]['owner']['login'], 'lang': []}]
            #lambda?
            #   Fetch repo languages
            fetch_languages(repo[i], f"https://api.github.com/repos/{repo[i]['owner']}/{repo[i]['name']}/languages")

        return repo
        
    def updateDatabase(self, db, table):

        columns = []

        repo = self.fetch_repos()
        
        for i in range(len(repo)):
            for j in range(len(repo[i]['lang'])):

                if repo[i]['lang'][j] not in columns:
                    columns.append(repo[i]['lang'][j])


        columns.sort()

        SQL(db).updateTable(table, "ADD", columns)
        
        del columns, repo

        return 

class Databases():

    def __init__(self, database=None, **args):


        #   Ensure the arguments has value
        if bool(args):

            #   Ensure there is one value
            for host, port in args.items():
                self.host = host
                self.port = port
            
            self.db = database
    
        del args, database
        return

class SQL(Databases):
    def __init__(self, database, **args):
        super().__init__(database, **args)
        
        #   Establish the connection to the database
        try:

            self.conn = sqlite3.connect(self.db)
            if not self.conn: raise Exception('Could not establish a connection to the database')

        except Exception as e: return e

        print('Established connection to the Database')
        self.cur = self.conn.cursor()
        #self.conn.close()

        
        return
    
    def createTable(self, table, **args):

        try:
            if len(args['args']['columns']) != len(args['args']['datatype']):
                raise Exception('Columns and Datatypes has to have equal value :( ')
        except Exception as e:
            return e
        

        #   Initialize a query
        query = f"CREATE TABLE IF NOT EXITS {table} ("


        for i in range(len(args['args']['columns'])):

            for col in args['args']['columns']:

                for dt in args['args']['datatype']:

                    query += f"{col} {dt}"
                
                    if i+1 != len(args['args']['columns']): query +=','
                    else : query += ");"

        #   Execute the statement
        self.conn.execute(query)

        return query

    def updateTable(self, table, keyword="add", *arg):

        keyword = keyword.upper()
        keywords = ['DROP', 'RENAME', 'ADD']

        #   fetch columns
        sql = self.selectRecord(table)
    
        query = f"ALTER TABLE {table} {keyword} COLUMN "

        try:
            
            if keyword not in keywords: raise Exception(f'{keyword} not one of {keywords}')
            if len(arg) != 2: raise Exception('Can only update one column at the time')

            
        except Exception as e: return e
        
        #   Ensure the keyword is equal and ensure there is no duplicates
        if keyword in keywords and str(arg[0]) not in list(map(lambda x: x[0], self.cur.description)):

            for i in range(len(arg)):
                print(arg)
                query += f"{arg[i]} "

        elif keyword in keywords and str(arg[0]) in list(map(lambda x: x[0], self.cur.description)): 
            print(list(map(lambda x: x[0], self.cur.description)))
            
        else: pass

        
        del table, keyword, arg, sql
        query += ";"
        #   Execute the query
        self.cur.execute(query)

        return

    def selectRecord(self, table, *columns):


        query = f"SELECT "
        # Ensure the columns is false
        if not bool(columns):
            query += "*"
        else:
            for i in range(len(columns)):
                query += f"{columns[i]}"
                if columns[i] != len(columns):
                    query += ","

        #   Initialize the statement to execute
        
        query +=f" FROM {table};"

        #   Execute the SQL statement
        self.cur.execute(query)

        return


        query = f"ALTER TABLE {table} ADD COLUMN "
        #   fetch table from database
        sql = self.selectRecord(table)
        names = list(map(lambda x: x[0], self.cur.description))
        

        #   Check for duplicates not working
        for i in range(len(arg)):
            if arg[i] not in names:
                query = f"ALTER TABLE {table} ADD COLUMN '{arg[i]}' BOOLEAN NOT NULL DEFAULT False;"
                self.cur.execute(query)

        return