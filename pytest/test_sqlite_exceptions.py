import os
import pytest

from core import SQL, GithubApi
from errorHandler import OperationalError
class TestDBExceptions:

    """ 
        Testing Exceptions in the database
        __SQL__ -> Testing database
        __table__ -> Table to be mocked
    """
    __table__ = 'test_table'

    __sql__ = SQL(database='test_database.db')

    def test_duplicateTable(self):
        
        #   Initialize test variables
        expected = f"Table already exists with-in the database"
        mock = {
                'id':'INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT', 'data': 'TEXT NOT NULL DEFAULT FALSE',
                'data1':'BLOB NOT NULL DEFAULT FALSE', 'data2':'REAL NOT NULL DEFAULT 0', 'date':'DATE NOT NULL DEFAULT CURRENT_DATE'}
        
        #   Raise Table Error
        with pytest.raises(OperationalError) as e:

            #   Call function to raise
            self.__sql__.TableConfigurations(table=self.__table__, statement='CREATE', columns=mock)
        
        assert expected == f"{e.value}"

    def test_notfound(self):

        #   Initialize test variables
        expected ="Table does not exist in the database"

        #   Rasing exception
        with pytest.raises(OperationalError) as e:

            #   Call function to raise
            self.__sql__.TableConfigurations(table=self.__table__, statement='Kake', columns={"*":"*"})

        assert expected == f"{e.value}"

    def test_identical_entries(self):

        """
            Testing the duplicated entires from the API
        """
                #   Initialize test variables
        
        db = 'test_fkh-ps.db'
        table = 'git_pro'
        expected = f"Table already exists with-in the database"

        #   Raise duplication Error
        with pytest.raises(OperationalError) as e:

            #   Call function to raise
            GithubApi().updateDatabase(db =db, table= table)
            
        
        assert expected == f"{e.value}"

        

            