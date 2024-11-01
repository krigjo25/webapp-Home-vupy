import os
import sqlite3
import logging
import requests
from typing import Optional,Tuple

from dotenv import load_dotenv
load_dotenv()

#   errorHandler
from lib.errorHandler import OperationalError

class Base():

    """ Base: Universal class for all database operations """
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

        return query

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
                
                if not isinstance(data, list): 
                    raise SyntaxError('accepts only lists as argument')

            except (sqlite3.Error, OperationalError) as e:
                logging.error(f"An error occured while attempting to insert data into the table: {e}")
            
            #   Initialize query
            query = self.configure_columns(table, 'INSERT', data)

            #   Execute query
            self.cur.executemany(query[0], query[1])
            self.conn.commit()
        
        def select_records(self, table:str, statement:str, columns:Tuple[str] = ("*",)):
            return self.cur.execute(self.configure_columns(table, statement, columns)).fetchall()
