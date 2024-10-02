#   Importing repositories
import os, json, sqlite3
import logging, requests

from dotenv import load_dotenv
load_dotenv()

#   errorHandler
from errorHandler import OperationalError

#   Requests repositories
from requests.exceptions import HTTPError, ConnectionError, Timeout, RequestException

class Base():

    """ Base: What would includes in several databases"""
    def __init__(self, database:str, port:int | int=None, host:str | str=None):

        self.host = host
        self.port = port
        self.db = database
        self.statements = ['CREATE', "ALTER", 'DROP', 'INSERT', 'SELECT']

        del host, database, port
        return
    
    def configure_columns(self,  table:str, statement:str, columns:list | tuple):
        
        #   Initialize variables
        row = []
        column = []
        rows = []
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
 
            for i in range(len(column)): query+= "?," if i+1 < len(column) else "?);"

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

    #   Adapted from documentations
    def dict_factory(self, cursor, row):
        columns = [column[0] for column in cursor.description]
        return {key: value for key, value in zip(columns, row)}
    
    #   Delete rows / table / database
    def delete_row(self, table:str, column:str, value:str): return self.cur.execute(f"DELETE FROM {table} WHERE {column} = {value};")
    def drop_table(self, table:str): return self.cur.execute(f'DROP table IF EXISTS {table}')
    def drop_database(self, db:str): return self.cur.execute(f'DROP DATABASE IF EXISTS {self.db}')  

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
            self.cur.row_factory = self.dict_factory

            return print('Established connection to the Database')

        def TableConfigurations(self, table:str, statement:str, columns:dict): 

            #   Initializing the tables
            tables = [i['name'] for i in self.select_records('sqlite_master', 'SELECT')]

            #   Ensure that table does not exists and statements is a known keyword
            if statement.upper() not in self.statements: raise OperationalError(404)
            if table in tables and statement == 'CREATE': raise OperationalError(200)

            #   Initialize the query
            query = self.configure_table(table, statement, columns)

            #   Query execution
            self.cur.execute(query)
            self.conn.commit()
            
            #   Sweep memory
            del tables, table, columns
            del statement

            return
        
        #   Inserting values into a table
        def insert_into_table(self, table:str, data:list):

            #   Initializing tables
            tables = [i['name'] for i in self.cur.execute('SELECT name FROM sqlite_master').fetchall()]

            #   Ensure that table exists
            if table not in tables: raise OperationalError(404)
            if not isinstance(data, list): raise SyntaxError('accepts only lists as argument')

            #   Initialize query
            query = self.configure_columns(table, 'INSERT', data)

            #   Execute query
            self.cur.executemany(query[0],query[1])
            self.conn.commit()

            #   Sweep Memory
            del query, tables, table, data
            return
        
        def select_records(self, table:str, statement:str, columns:tuple | tuple = tuple("*")):
            return self.cur.execute(self.configure_columns(table, statement, columns)).fetchall()

class APIConfig():
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
            elif r.status_code in [401, 403]: return json.dumps({"Error": "Encountered an AUTHORIZATION Error"})
            
        except (HTTPError, ConnectionError, Timeout, RequestException) as e: 
            logging.error(e)
        return

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
        

        #   Create a connection to github
        response = self.ApiCall(f"{self.API_URL}user/repos", head=self.head)
        
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
        repo = []

        for i in range(len(response)):
            #   Structure the items from github
            repo += [{"name":response[i]['name'], "description":response[i]['description'], "url":response[i]['html_url'], 'owner':response[i]['owner']['login'], 'lang':"", 'date':response[i]['created_at']}]

            #   Fetch repo languages
            fetch_languages(repo, f"{self.API_URL}/repos/{repo[i]['owner']}/{repo[i]['name']}/languages")

        return repo

    def updateDatabase(self, db:str, table:str):

        columns = []
        sql = SQL(db)
        repo = self.fetch_repos()

        x = sql.cur.execute('SELECT name FROM sqlite_master;').fetchall()

        if bool(x):
            if table in x[0]:

                for j in range(len(repo)):

                    for k in range(len(repo[j]['lang'])):
                        
                        if repo[j]['lang'][k] not in columns:
                            columns.append(repo[j]['lang'][k])

                    columns.sort()

                    sql.insert_into_table(table, repo)
        
        else:
            query = {}
                    
            for i in range(len(repo)):

                for key, lang in repo[i].items():

                    if key not in columns:
                        columns.append(key)
            if "id" not in columns: columns.append("id")

            for i in range(len(columns)):

                #   Ensure the columns not equal date nor id
                if 'date' == columns[i]:
                    query[columns[i]] = 'DATE NOT NULL DEFAULT CURRENT_DATE'
                elif columns[i] == 'id':
                    query[columns[i]] = 'INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT'

                else:
                    query[columns[i]] = "TEXT NOT NULL DEFAULT False"

            columns = query
            sql.TableConfigurations(table, "CREATE", columns=columns)

                  
            del query

        #   Sweep data
        del columns, repo

        return 
