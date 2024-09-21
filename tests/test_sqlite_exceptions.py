import os
import pytest

from sqlite3 import OperationalError
from core import SQL
from errorHandler import DuplicatedError

class TestDBExceptions:

    #   
    #sql = SQL(database='test_database.db')


    def test_duplicateTable(self):
        
        __table__ = 'test_table'
        sql = SQL(database='test_database.db')
        
        with pytest.raises(DuplicatedError) as e:
            sql.TableConfigurations(table=__table__, statement='CREATE', columns='*')


            