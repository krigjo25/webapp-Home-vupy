class OperationalError(Exception):
    """ Raises when duplicated is not allowed """

    error = {
        200:"Table already exists with-in the database",
        404:"Table does not exist in the database",
        500:'Column has to be a type of list'

    }
    def __init__(self, code) -> None:
        super().__init__(code)
        self.code = code

    def __str__(self):
        return self.error[self.code]
