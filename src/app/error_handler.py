# Python Imports
from typing import Union

# Flask Imports

# Third-Party Imports

# App Imports
from app.exceptions import *


# Base class for all errors
class ErrorHandler:
    def __init__(self):
        pass

    @staticmethod
    def handle_error(error: Union[Exception, BaseError]):
        if hasattr(error, "get_response"):
            return error.get_response()
        elif "OperationalError" in str(error):
            error = MySQLConnectionError(str(error))
            return error.get_response()

        e = str(error)
        error = BaseError(e)
        return error.get_response()
