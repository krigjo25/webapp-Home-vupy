import os
import pytest
import sqlite3

from core import SQL

def test_sql_connection() -> None:

    """ Testing sqlite connection"""
    sql = SQL(database='test_database')

    #   Asserts the name of the database
    assert os.path.exists('test_database')



