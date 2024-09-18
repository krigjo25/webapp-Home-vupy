import os
import pytest
import sqlite3

from core import SQL

class TestDatabase:

    def test_sql_connection(self) -> None:

        """ Testing sqlite connection"""
        sql = SQL(database='test_database')

        #   Asserts the name of the database
        assert os.path.exists('test_database')

    #   Create
    def test_createTable(self): pass

    #   Update
    def test_updateTable(self): pass

    #   Select
    def test_selectRecord(self): pass

    #   Delete data
    def test_deleteData(self): pass


