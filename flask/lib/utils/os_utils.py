#   Misc os utils

#   Import the necessary libraries
import os
from pathlib import Path

from log_config import UtilsWatcher
from exception_handler import NotFoundError

logger = UtilsWatcher('OS Utils Misc')
logger.file_handler()

class OsUtils(object):

    @staticmethod
    def find_project_root( marker: str ) -> Path:
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
    def find_directory(dir: str) -> Path:
        """
        Get the root directory of the script.
        :return: The root directory of the script.
        """
        return Path(os.path.dirname(os.path.abspath(__file__))).parent
    
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

            else:
                logger.info(f"Directory {path} already exists.")

        except Exception as e:
            logger.error(f"Error creating directory {path}: {e}")

if __name__ == "__main__":
    pass
    #   Test the function
    #oum = OsUtils()
    #print(oum.find_project_root("README.md"))