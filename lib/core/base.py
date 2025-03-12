#   Base Classes for the application

#   Importing required dependencies
import requests
from typing import Optional
from time import perf_counter
from dotenv import load_dotenv

#   Imporiting custom dependencies
from lib.utils.log_config import DatabaseWatcher, ApiWatcher

#  Loading the environment variables
load_dotenv()

#   Requests repositories
from requests.exceptions import HTTPError, ConnectionError, Timeout, RequestException
log = ApiWatcher()
log.FileHandler()

class Database(object):

    """ Base: Universal class for all database operations """
    def __init__(self, database: str, port: Optional[int] = None, host: Optional[str] = None):

        self.host = host
        self.port = port
        self.db = database
        self.statements = ['CREATE', "ALTER", 'DROP', 'INSERT', 'SELECT']

        self.log = DatabaseWatcher()
        self.log.FileHandler()
    
    def configure_columns(self,  table:str, statement:str, columns:list | tuple):
        
        #   Initialize variables
        row = []
        rows = []
        column = []
        

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

        return query

class APIConfig(object):

    def __init__(self, URL=None, KEY=None, GET = "GET", POST = "POST", PUT='PUT', PATCH='PATCH', DELETE = 'DELETE'):
        self.GET = GET
        self.PUT = PUT
        self.POST = POST
        self.API_URL = URL
        self.API_KEY = KEY
        self.PATCH = PATCH
        self.DELETE = DELETE

        self.logging = log
        

    def ApiCall(self, endpoint: str, head: dict):

        """
            Calling the API
        """

        #   Initialize the start time
        start = perf_counter()

        try:
            r = requests.get(f"{endpoint}", timeout=30, headers=head)

            if r.status_code in [200]:
                
                self.logging.info(f"Succsess : Recieved request code :{r.status_code} Time elapsed: {perf_counter()-start}")
                return r.json()

            if r.status_code in [401, 403]: raise ConnectionError('Unauthorized Access')
            elif r.status_code in [404]: raise HTTPError('Resource not found')     
        except (HTTPError, ConnectionError, Timeout, RequestException) as e: 
            self.logging.error(f"request code :{r.status_code}\n Error: {e}, Time elapsed: {perf_counter()-start}")
        
        self.logging.warning(f" Time elapsed: {perf_counter()-start}\t Request code: {r.status_code}")
        return 

