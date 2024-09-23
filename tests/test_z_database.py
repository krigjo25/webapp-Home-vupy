import os

def test_drop_database():
    """Removes the testing database"""
    os.remove('test_database.db')
    #os.remove('fkh-ps.db')
