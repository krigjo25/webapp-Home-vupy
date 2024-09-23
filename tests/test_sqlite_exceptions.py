import os
import pytest

from sqlite3 import OperationalError
from core import SQL
from errorHandler import TableError

class TestDBExceptions:

    #   
    #sql = SQL(database='test_database.db')


    def test_duplicateTable(self):
        
        #   Initialize test variables
        __table__ = 'test_table'
        sql = SQL(database='test_database.db')
        expected = f"Table already exists with-in the database"
        
        mock = {
                'id':'INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT', 'data': 'TEXT NOT NULL DEFAULT FALSE',
                'data1':'BLOB NOT NULL DEFAULT FALSE', 'data2':'REAL NOT NULL DEFAULT 0', 'date':'DATE NOT NULL DEFAULT CURRENT_DATE'}
        

        with pytest.raises(TableError) as e:

            sql.TableConfigurations(table=__table__, statement='CREATE', columns=mock)
        
        assert expected == f"{e.value}"

    def test_notfound(self):

        #   Initialize test variables
        __table__ = 'test_table'
        sql = SQL(database='test_database.db')
        expected ="Table does not exist in the database"

        #   Rasing exception
        with pytest.raises(TableError) as e:
            sql.TableConfigurations(table=__table__, statement='Kake', columns={"*":"*"})

        assert expected == f"{e.value}"

        

            