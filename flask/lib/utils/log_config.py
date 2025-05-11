#  Handling the application logging

#   Importing required dependencies
import os, logging as Log
from typing import Optional, Union

from os_utils import OSUtils

class Logger(object):

    """
        Logger class to handle application logging
    """
    def __init__(self, name:str, log_dir:Optional[str] = None):

        """
            *   Initialize the logger
            *   Set the logging level to DEBUG
            *   Set the logging format
            *   Set the logging handler
            *   param name: str - default: Class name
        """
        
        #   Initialize the handler
        self.name = name or self.__class__.__name__
        
        self.log = Log.getLogger(f"{self.name}")
        self.log.setLevel(Log.DEBUG)
        self.log_dir = log_dir
        
        #   Initialize the Flags
        self.file_handler = False
        self.console_handler = False


    def save_path(self, dir:str):
        #   Find root directory

        #   find the log directory
        
        #   Ensure the directory exists
        if os.path.exists(dir):

            #   Save the directory
            self.log.file
            return

        #   Create the directory
        OSUtils().create_directory(dir)


        
    def setup_handler(self, handler:Union[Log.FileHandler | Log.StreamHandler]):
        
        """
            *   Setup the Log handler
            *   param handler:[Log.FileHandler, Log.StreamHandler]
        """
        #   Initializing the formatter
        formatter = Log.Formatter('%(asctime)s - %(levelname)s -\t %(name)s -\t %(message)s')
        handler.setFormatter(formatter)
        self.log.addHandler(handler)
    
    def console_handler(self):


        """
            *   Add a console handler to the logger
        """
        
        #   Ensure that the Flag is not set to True
        if not self.console_handler:
            
            #   Set the flag
            self.console_handler = True
            
            #   Initializing the handler
            handler = Log.StreamHandler()
            self.setup_handler(handler)

            #   Send message to the console
            self.log.info(f"{self.name} has been initialized.")

    def file_handler(self):

        """
            *   Add a file handler to the logger
        """
        #   Ensure that the Flag is not set to True
        if not self.file_handler:

            #   Initialize the log directory
            if self.log_dir:
                self.save_path(self.log_dir)
            #   Initializing the handler
            handler = Log.FileHandler(f"{self.name}.log")
            self.setup_handler(handler)

            #   Send message to the console
            self.log.info(f"{self.name} has been initialized.")
            
            #   Set the flag
            self.file_handler = True

        else:
            self.log.warning(f"{self.name} Console handler already initialized")

    def info(self, message):
        self.log.info(message)
    
    def error(self, message):
        self.log.error(message)
    
    def warn(self, message):
        self.log.warning(message)
    
    def debug(self, message):
        self.log.debug(message)

class AppWatcher(Logger):

    def __init__(self):
        super().__init__(name=f"{self.__class__.__name__}")

class UtilsWatcher(Logger):
    
    def __init__(self, name:Optional[str] = None, log_dir:Optional[str] = None):
        super().__init__(name=f"{self.__class__.__name__} -- {name}", log_dir=log_dir)


class DatabaseWatcher(Logger):

    def __init__(self, name:Optional[str] = None):
        super().__init__(name=f"{self.__class__.__name__} -- {name}")
        
        
