#  App congiguration settings

# Importing required modules
import os

class DefaulthConfig(object):
    DEBUG = False
    TESTING = False
    SESSION_TYPE = None
    VITE_AUTO_INSERT = True
    SESSION_PERMANENT = False
    STATIC_FOLDER = "VueClient/src/assets"
    DATABASE_URL = os.getenv('DATABASE_URL')

class DevelopmentConfig(DefaulthConfig):
    SESSION_TYPE ='filesystem'
    DEBUG = True


class TestConfig(DefaulthConfig):
    TESTING = True
    SESSION_TYPE ='filesystem'
    DEBUG = True

class ProdConfig(DefaulthConfig):
    DEBUG = False
    DATABASE_URL = os.getenv("DATABASE_URL")
    TESTING = True
    
    SESSION_TYPE ='filesystem'
    