import os
import pytest

from sqlite3 import OperationalError
from core import SQL
from errorHandler import DuplicatedError, NotFoundError

class TestDBExceptions:

    #   
    #sql = SQL(database='test_database.db')


    def test_duplicateTable(self):
        
        #   Initialize test variables
        __table__ = 'test_table'
        sql = SQL(database='test_database.db')
        
        with pytest.raises(DuplicatedError) as e:
            sql.TableConfigurations(table=__table__, statement='CREATE', columns='*')
        print(e.value)
        #assert e.value == "Duplicated tables"

    def test_notfound(self):

        #   Initialize test variables
        __table__ = 'test_table'
        sql = SQL(database='test_database.db')

        with pytest.raises(NotFoundError) as e:
            sql.TableConfigurations(table=__table__, statement='Kake', columns='*')
        
        print(e.value)
        

            