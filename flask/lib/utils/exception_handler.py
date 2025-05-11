#   Error handler

from typing import Optional

class OperationalError(Exception):
    """ Raises when duplicated is not allowed """

    error = {
        000:"Dublicated data",
        200:"Table already exists with-in the database",
        404:"Table does not exist in the database",
        500:'Column has to be a type of list'}

    def __init__(self, code, message:Optional[str]) -> None:
        
        super().__init__(code, message)
        self.status_code = code
        self.message = message

        if message is None:
            self.message = self.error[code]

class NotFoundError(Exception):
    """ Raises when the requested resource is not found """

    error = {404: "404: Resource not found"}

    def __init__(self, code, message:Optional[str]) -> None:
        super().__init__(code, message)
        self.status_code = code
        self.message = message

        if message is None:
            self.message = self.error[code]