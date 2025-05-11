#   Error handler

class OperationalError(Exception):
    """ Raises when duplicated is not allowed """

    error = {
        000:"Dublicated data",
        200:"Table already exists with-in the database",
        404:"Table does not exist in the database",
        500:'Column has to be a type of list'}

    def __init__(self, code) -> None:
        super().__init__(code)
        self.code = code

    def __str__(self):
        return self.error[self.code]

class NotFoundError(Exception):
    """ Raises when the requested resource is not found """

    error = {
        404: "404: Resource not found",
        500: "500: Internal server error"
    }

    def __init__(self, code) -> None:
        super().__init__(code)
        self.code = code