# Python Imports

# Flask Imports
from flask import jsonify

# Third-Party Imports

# App Imports


class CustomResponse:
    @staticmethod
    def send_response(*, data=None, error=None, status_code=200):
        return (
            jsonify(
                dict(
                    data=data if data else {},
                    error=error if error else {},
                    status_code=status_code,
                ),
            ),
            status_code,
        )
