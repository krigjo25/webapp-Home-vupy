import os
import pytest

from core import SQL, GithubApi
class TestDatabase:

    #
    sql = SQL(database='test_database.db')
    table = 'test_table'

    def test_sql_connection(self) -> None:

        """ Testing sqlite connection"""

        #   Asserts the name of the database
        assert os.path.exists('test_database.db')

    #   Table tests
    def test_createTable(self):

        #   Initialize a database connection

        #   Initialize query
        mock = {
                'id':'INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT', 'data': 'TEXT NOT NULL DEFAULT FALSE',
                'data1':'BLOB NOT NULL DEFAULT FALSE', 'data2':'REAL NOT NULL DEFAULT 0', 'date':'DATE NOT NULL DEFAULT CURRENT_DATE'}

        #   Initialize data into the database
        self.sql.TableConfigurations(self.table, 'CREATE', mock)
        
        #   Fetch table information
        actual = self.sql.conn.execute('SELECT name FROM sqlite_master;').fetchall()

        #   Test the data
        assert actual[0][0] == self.table

        #   Sweep Data
        del mock, actual

        return

    # Value tests
    def test_insertdata(self):
        
        data = []
        columns = ('data', 'data1', 'data2')
        mock = [('Sometext', 'image.jpg', 2.0), ('Sometext', 'image.jpg', 2.0)]

        for i in mock:
            for j in range(len(columns)):    
                data.append({columns[j]:i[j]})

        #   Insert the values into the table 
        self.sql.insert_into_table(self.table, data)

        # Ensure that the response, is equal
        actual = self.sql.select_records(self.table, 'SELECT', columns=columns)
        
        assert actual == mock

    #   Select
    def test_selectRecord(self):
        
        mock = [('Sometext', 'image.jpg', 2.0), ('Sometext', 'image.jpg', 2.0)]
        actual = self.sql.select_records(self.table, 'SELECT', columns= ("data", "data1", "data2"))
        assert actual == mock

    def test_request_database(self):

        api = GithubApi()
        api.updateDatabase('fkh-ps.db', 'git_pro')
        api.updateDatabase('fkh-ps.db', 'git_pro')
        #os.remove('fkh-ps.db')
        


