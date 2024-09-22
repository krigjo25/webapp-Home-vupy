class DuplicatedError(Exception):
    """ Raises when duplicated is not allowed """

    error = {
        '000': "Duplication found",

    }
    def __init__(self, code) -> None:
        super().__init__(code)
        self.code = code

    def __str__(self):
        return self.error[f"{self.code}"]

class NotFoundError(Exception):
    """ Raises when the system can't find the argument"""
    pass
