#   Importing repositories
import os, json, sqlite3
import logging, requests

from dotenv import load_dotenv
from requests.exceptions import HTTPError, ConnectionError, Timeout, RequestException

from algorithms import SearchAlgorithm
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
    
    def configure_columns(self,  table:str, statement:str, columns: tuple| tuple=None, datas: dict | dict = None):

        #   Initialize variables
        data = "("
        column = "("
        search = SearchAlgorithm()

        #   Initialize the array
        statements = ['SELECT', 'INSERT']

        if statement.upper() == search.linearSearch(statements, len(statements), statement) and bool(datas):

            for key, value in datas.items():
                
                column += f"{key}"
                data += f"\'{value}\'"

                column += ',' if list(columns)[-1] != key else ')'
                data += ',' if list(columns)[-1] != key else ')'


            query = f"{statement} INTO {table} {column} VALUES {data};"

        return query
    
    def configure_table(self, table:str, statement:str, columns: dict | dict=None):

        statements = ['CREATE', "ALTER", 'DROP']
        search = SearchAlgorithm()
        try:
            #   Ensure the table exists
            #   Ensure the statement exist in statements
            if not search.linearSearch(statements, len(statements), statement): 
                raise Exception('Given statement does not exists in SQLite')

        except Exception as e: return e

        #   Ensure that statement is equal to the listed  statement
        if statement == search.linearSearch(statements, len(statements), statement) and bool(columns):
            query = f"{statement} TABLE IF NOT EXISTS {table}("

            #   Ensure that there is values in columns
            for key, value in columns.items():

                #   Append data
                query += f"{key} {value}"

                #   Ensure the list is not at end
                query += ',' if list(columns)[-1] != key else ');'

        #   Ensure the statements is a DROP
        elif statement ==search.linearSearch(statements, len(statements), statement): query = f"{statement} TABLE IF EXISTS {table};"

        #   Sweep data
        del table, statement, columns

        return query

class SQL(Databases):

        def __init__(self, database:str, port:int | int=None, host:str | str=None, method:str | str = None):
            super().__init__(database, port, host, method)
        
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
            
            try: 
                with self.conn:
                    self.cur.execute(self.configure_table(table, statement, columns))
            except Exception as e:
                return e
        
        #   Inserting values into a table
        def insert_into_table(self, table:str, statement:str, column:tuple, data:dict): 
            self.cur.execute(self.configure_columns(table, statement, column, data))
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

