#   Importing repositories
import os
import sqlite3
import logging
import requests
from typing import Optional,Tuple

from dotenv import load_dotenv
load_dotenv()

#   errorHandler
from errorHandler import OperationalError

#   Requests repositories
from requests.exceptions import HTTPError, ConnectionError, Timeout, RequestException

#   Configuring the logger
logging.basicConfig(
    level=logging.DEBUG, 
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
    handlers=[logging.FileHandler("app.log"), 
              logging.StreamHandler()])
class Base():

    """ Base: What would includes in several databases"""
    def __init__(self, database: str, port: Optional[int] = None, host: Optional[str] = None):

        self.host = host
        self.port = port
        self.db = database
        self.statements = ['CREATE', "ALTER", 'DROP', 'INSERT', 'SELECT']

    
    def configure_columns(self,  table:str, statement:str, columns:list | tuple):
        
        #   Initialize variables
        row = []
        rows = []
        column = []
        tmp = ""

        if statement.upper() == "INSERT":

            for data in columns:

                for key, value in data.items():

                    #   Ensure that the key does not exists in column
                    if key not in column: column.append(key)
                    
                
            for data in columns:
                for key, value in data.items():

                    if type(value) == list or type(value) == tuple:
                        for i in value:
                            tmp += i
                        
                            row.append(i)
                    else:
                        row.append(value)

                    if len(row) == len(column):
                        rows.append(tuple(row))
                        row = []


            query = f"{statement} INTO {table}{tuple(column)} VALUES("
 
            for i in range(len(column)): 
                query+= "?," if i+1 < len(column) else f"?);"
        elif statement.upper() == "SELECT":

            for i in range(len(columns)):
                column += {columns[i]} if i != columns[-1] else columns[i]
            
            columns = column
            column = ""

            for i in range(len(columns)):
                column += columns[i] + "," if i +1 < len(columns) else f"{columns[i]}"
            
            query = f"{statement} {column} FROM {table};"

            return query

        #   Sweep memory
        del table, statement, columns
        del column,  row

        return [query, rows]
    
    def configure_table(self, table:str, statement:str, columns: dict | dict=None):

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

        return query

    #  Universal methods
    def delete_row(self, table:str, column:str, value:str): return self.cur.execute(f"DELETE FROM {table} WHERE {column} = {value};")
    def drop_table(self, table:str): return self.cur.execute(f'DROP table IF EXISTS {table}')
    def drop_database(self, db:str): return self.cur.execute(f'DROP DATABASE IF EXISTS {self.db}')  

class SQL(Base):

        def __init__(self, database: str): 
            super().__init__(database)
            self.database = database

            #   Establishing a connection to the database
            try:
                
                self.conn = sqlite3.connect(self.db)

                #   Ensure that the connection is established
                if not self.conn: raise OperationalError(100)

            except Exception as e: 
                logging.error(f"An error occured while trying to connect to the database: {e}")
                raise OperationalError(100)

            #   Initializing the cursor
            self.cur = self.conn.cursor()
            self.cur.row_factory = self.dict_factory
            logging.info(f"Connection to {self.db} established")
        
        def dict_factory(self, cursor, row):

            """
                #   Adopted from the sqlite3 documentation
                #   Converts the row from a tuple into a dictionary
            """
            columns = [column[0] for column in cursor.description]
            return {key: value for key, value in zip(columns, row)}

        def TableConfigurations(self, table:str, statement:str, columns:dict): 

            #   Initializing the tables
            tables = [i['name'] for i in self.select_records('sqlite_master', 'SELECT')]

            #   Ensure that table does not exists and statements is a known keyword
            if statement.upper() not in self.statements:
                logging.error(f"Unknown statement: {statement}")
                raise OperationalError(404)

            if table in tables and statement == 'CREATE':
                logging.error(f"Table {table} already exists")
                raise OperationalError(200)

            #   Initialize the query
            query = self.configure_table(table, statement, columns)
            logging.info(f"Executing query: {query}")


            #   Query execution
            self.cur.execute(query)
            self.conn.commit()
            
            #   Sweep memory
            del tables, table, columns
            del statement

            return
        
        #   Inserting values into a table
        def initialize_records(self, table:str, data:list):

            try:

                #   Initializing tables
                tables = [i['name'] for i in self.cur.execute('SELECT name FROM sqlite_master').fetchall()]


                #   Ensure that table exists
                if table not in tables:
                    logging.error(f"{table} Not found in {tables}")
                    raise OperationalError(404)
                else:
                    sqlData = self.select_records(table, 'SELECT')
                    if sqlData == data:
                        print(data)
                
                if not isinstance(data, list): 
                    raise SyntaxError('accepts only lists as argument')

            except (sqlite3.Error, OperationalError) as e:
                logging.error(f"An error occured while attempting to insert data into the table: {e}")
            
            #   Initialize query
            query = self.configure_columns(table, 'INSERT', data)
            #   Execute query
            self.cur.executemany(query[0],query[1])
            self.conn.commit()
        
        def select_records(self, table:str, statement:str, columns:Tuple[str] = ("*",)):
            return self.cur.execute(self.configure_columns(table, statement, columns)).fetchall()

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

        InitializeData('test_fkh-ps.db').upsertData('test_poitegr', repo)

class InitializeData():

    def __init__(self, db: str):
        self.sql = SQL(db)
        self.tables = self.sql.select_records('sqlite_master', 'SELECT')


    def upsertData(self, table: str, repo: list):

        """
            Initializing the data by fetching the repositories from the API
            and Ensures the database is up to date
        """

        try:
            #   Ensure that the table is a string
            if not isinstance(table, str):
                raise SyntaxError('Table has to be a string')

            #   Ensure that the repo is a list
            if not isinstance(repo, list): 
                raise SyntaxError('Repo has to be a list')

        except SyntaxError as e:
            logging.error(f"An error occured while trying to initialize the data: {e}")
            raise SyntaxError(e)
        
        #   Initializing variables
        data = {}
        columns = []

        #   Ensure the existance of the table
        if table in [i['name'] for i in self.tables]:
            self.sql.initialize_records(table, repo)

        else:
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
            print(data)
            self.sql.TableConfigurations(table, "CREATE", columns=data)