#   Misc os utils

#   Import the necessary libraries
import os, time
from pathlib import Path
from typing import Optional

from logger_config import APIWatcher
from exception_handler import NotFoundError

logger = APIWatcher('OS-Utils', 'logs')
logger.file_handler()

class OsUtils(object):

    def __init__(self):
        self.find_project_root
        pass

    @staticmethod
    def find_project_root(marker: str) -> Path:
        """
        Find the root directory of the project.
        :return: The root directory of the project.
        """

        path = Path(os.getcwd()).resolve()

        try:
            while path.name != path.parent.name:
            
                #   Ensure that the marker is located in the directory
                if (path / marker).exists():
                    logger.info(f"{marker} found in {path}\n")

                    return path
                
                #   updating the path
                path = path.parent

                logger.info(f"Checking {path} for marker '{marker}'")
            
            raise NotFoundError(404)
        
        except NotFoundError as e:
            logger.error(f"Marker '{marker}' not found in the directory tree.\n Code {e}\n")

            return e

    @staticmethod
    def create_directory(self, path:str):
        """
        Create a directory if it does not exist.
        :param path: The path to the directory.
        :return: None
        """

        try:
            if not os.path.exists(path):
                os.makedirs(path)
                logger.info(f"Directory {path} created.")

            else: logger.info(f"Directory {path} already exists.")

        except Exception as e: logger.error(f"Error creating directory {path}: {e}")


    def find_directory(self, marker:str, DIR:Optional[str] = None) -> Path:
        """
        Get the root directory of the script.
        :return: The root directory of the script.
        """

        root = self.find_project_root(marker)

        if not DIR: return root

        try:
            if os.path.isdir(DIR): return Path(DIR)
            
            
        except NotFoundError as e:
            logger.error(f"Directory '{DIR}' not found in the directory tree.\n Code {e}\n")

            return e
        start = time.perf_counter()


        with os.scandir(root) as dir:

            list_dir = [entry.path for entry in dir if entry.is_dir() and entry.name == "VueClient"]

        
        for i in list_dir:

            with os.scandir(i) as dir:
                list_dir = [entry.path for entry in dir if entry.is_dir()]

        for i in list_dir:

            with os.scandir(i) as dir:
                list_dir = [entry.path for entry in dir if entry.is_dir() and entry.name == "assets"]

 
        for i in list_dir:
            with os.scandir(i) as dir:
                list_dir = [entry.path for entry in dir if entry.is_dir() and entry.name == "img"]

        for i in list_dir:

            with os.scandir(i) as dir:
                list_dir = [entry.path for entry in dir]
        
        end = time.perf_counter()
        print(f"Time taken to find the directory: {end - start} seconds")

        print(list_dir)

if __name__ == "__main__":
    pass
    #   Test the function
    oum = OsUtils()
    print(oum.find_directory('flask', 'carousel'))