import os
import pytest

from core import SQL, InitializeData
class TestDatabase:

    #   Initializie connection
    sql = SQL(database='test_database.db')
    table = 'test_table'

    def test_sql_connection(self) -> None:

        """ 
            Ensuring the sql database is created.
            Testing sqlite connection
        """

        #   Asserts the name of the database
        assert os.path.isfile('test_fkh-ps.db')
        assert os.path.isfile('test_database.db')


    def test_createTable(self):

        #   Initialize datasets
        actual = []
        mock = {
                'id':'INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT', 'data': 'TEXT NOT NULL DEFAULT FALSE',
                'data1':'BLOB NOT NULL DEFAULT FALSE', 'data2':'REAL NOT NULL DEFAULT 0', 'date':'DATE NOT NULL DEFAULT CURRENT_DATE'}

        #   Initialize data into the database
        self.sql.TableConfigurations(self.table, 'CREATE', mock)
        
        #   Fetch table information
        for i in self.sql.conn.execute('SELECT name FROM sqlite_master;').fetchall():
           for j in i:
            actual.append(j)

        #   Test the data
        assert self.table in actual

        #   Sweep Data
        del mock, actual

        return


    def test_insertdata(self):
        """
            Creating a dataset for the test,
            and tries to retrieve the data
            from the database
        """
        #   Initialize dataset
        data = [{'data':'Sometext', 'data1':'image.jpg', 'data2':2.0}, 
                {'data':'Sometext', 'data1':'image.jpg', 'data2':2.0}]

        #   Insert the values into the table 
        self.sql.insert_into_table(self.table, data)

        #   Prepare test
        actual = self.sql.select_records(self.table, 'SELECT', columns=('data', 'data1', 'data2'))

        #   Test
        assert actual == data

        #   Sweep Memory
        del data,actual
        return

    def test_selectRecord(self):

        """
        Retrieves the information
        from the database """

        #   Initializing dataset for the test
        data = [{'data':'Sometext', 'data1':'image.jpg', 'data2':2.0}, 
                {'data':'Sometext', 'data1':'image.jpg', 'data2':2.0}]
        
        #  Initialize the data from the database
        actual = self.sql.select_records(self.table, 'SELECT', columns= ("data", "data1", "data2"))

        #   Test the data
        assert actual == data

        #   Sweep Memory
        del actual, data

        return

    def test_request_database(self):

        api = InitializeData()
        api.initialize_data('test_fkh-ps.db', 'git_pro',)

        
        


