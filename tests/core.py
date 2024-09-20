#   Importing repositories
import os, json, sqlite3
import logging, requests

from dotenv import load_dotenv
from requests.exceptions import HTTPError, ConnectionError, Timeout, RequestException

load_dotenv()

class Base():

    """ Base: What would includes in several databases"""
    def __init__(self, database:str, port:int | int=None, host:str | str=None):

        self.host = host
        self.port = port
        self.db = database
        self.statements = ['CREATE', "ALTER", 'DROP', 'INSERT', 'SELECT']

        del host, database, port
        return
    
    def configure_columns(self,  table:str, statement:str, columns:list | list=None, datas: dict | dict = None):
        
        #   Initialize variables
        data = ""
        column = ""

        if statement.upper() in self.statements and bool(datas):

            for i in range(len(columns)):
                column += f'{columns[i]}, ' if i +1 < len(columns) else f"{columns[i]}"


            for key, value in datas.items():
                data += f'\'{value}\',' if list(columns)[-1] != key else f'\'{value}\''

            query = f"{statement} INTO {table} ({column}) VALUES ({data});"

        #   Ensure the select statement
        elif statement.upper() in self.statements and bool(columns):

            for i in range(len(columns)):
                column += f'{columns[i]}, ' if i +1 < len(columns) else f"{columns[i]}"

            query = f"{statement} {column} FROM {table};"

        #   Sweep memory
        del column, data, table
        del statement, columns

        return query
    
    def configure_table(self, table:str, statement:str, columns: dict | dict=None):

        print(columns)
        #   Ensure that statement is equal to the listed  statement

        if statement in self.statements and bool(columns):
            query = f"{statement} TABLE IF NOT EXISTS {table}("

            #   Ensure that there is values in columns
            for key, value in columns.items():

                #   Append data
                query += f"{key} {value}"

                #   Ensure the list is not at end
                query += ',' if list(columns)[-1] != key else ');'

        #   Sweep data
        del table, statement, columns
        print(query)
        return query

class SQL(Base):

        def __init__(self, database:str, port:int | int=None, host:str | str=None):
            super().__init__(database, port, host)
        
            #   Establish the connection to the database
            try:

                self.conn = sqlite3.connect(self.db)
                if not self.conn: raise Exception('Could not establish a connection to the database')

            except Exception as e: return e

            #   Initializing the sqlite cursor
            self.cur = self.conn.cursor()

            return print('Established connection to the Database')

        #   Creating a table
        def TableConfigurations(self, table:str, statement:str, columns:dict): 
            

            self.cur.execute(self.configure_table(table, statement, columns))
        
        #   Inserting values into a table
        def insert_into_table(self, table:str, statement:str, column:list, data:dict):
            try:

                if statement not in self.statements:
                    raise SyntaxError('400 : Given statement does not exists in SQLlite3')
                
                if table not in self.cur.execute('SELECT name FROM sqlite_master').fetchall():
                    raise SyntaxError('404 : Table Does not exists')
                
                if not isinstance(column, list):
                    raise Exception('400: Bad Request, accepts only list as a argument')
                
                if not isinstance(data, dict): raise Exception('400, accepts only dictionary as argument')
    
            except (SyntaxError, Exception) as e: print(e)

            self.cur.execute(self.configure_columns(table, statement, column, data))
            self.conn.commit()
            return
        
        def select_records(self, table:str, statement:str, columns:tuple | tuple = "*"):
            return self.cur.execute(self.configure_columns(table, statement, columns)).fetchall()
            

        #   delete a row
        def delete_row(self, table:str, column:str, value:str): return self.cur.execute(f"DELETE FROM {table} WHERE {column} = {value};")
        def drop_table(self, table:str): return self.conn.execute(f'DROP table IF EXISTS {table}')
        def drop_database(self, db:str): return self.cur.execute(f'DROP DATABASE IF EXISTS {self.db}')  



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

