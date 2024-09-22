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
        expected = f"{__table__} already exists in the database"
        
        with pytest.raises(TableError) as e:
            sql.TableConfigurations(table=__table__, statement='CREATE', columns='*')
        print(e.value)
        #assert expected in e.exconly()

    def test_notfound(self):

        #   Initialize test variables
        __table__ = 'test_table'
        sql = SQL(database='test_database.db')
        expected ="Kake Not found in array"

        #   Rasing exception
        with pytest.raises(TableError) as e:
            sql.TableConfigurations(table=__table__, statement='Kake')
        
        #assert expected in e.exconly()

        

            