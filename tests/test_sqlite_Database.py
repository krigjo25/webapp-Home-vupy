import os
import pytest

from core import SQL

class TestDatabase:

    def test_sql_connection(self) -> None:

        """ Testing sqlite connection"""
        sql = SQL(database='test_database.db')

        #   Asserts the name of the database
        assert os.path.exists('test_database.db')

        #   Sweep data
        del sql

    #   Table tests
    def test_createTable(self):
        sql = SQL(database='test_database.db')
        table = 'test_table'
        mock = {
                'id':'INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT', 'data': 'TEXT NOT NULL DEFAULT FALSE',
                'data':'BLOB NOT NULL DEFAULT FALSE', 'data':'REAL NOT NULL DEFAULT 0',
                'data':'NULL NOT NULL DEFAULT NULL', 'date':'NUMERIC NOT NULL DEFAULT DATE'}

        #   Initialize data into the database
        sql.TableConfigurations(table, 'CREATE', mock)
        
        #   Fetch table information
        actual = sql.conn.execute('SELECT name FROM sqlite_master;').fetchall()

        #   Test the data
        assert actual[0][0] == table

        #   Sweep Data
        del sql, mock, table, actual

        return
    
    #   Update
    def test_updateTable(self): pass

    # Value tests
#    def test_insertdata(self): pass

    #   Select
#    def test_selectRecord(self): pass

    #   Delete data
#    def test_deleteData(self): pass

#    def test_droptable(self): pass

 #   def test_dropdatabase(self): pass

