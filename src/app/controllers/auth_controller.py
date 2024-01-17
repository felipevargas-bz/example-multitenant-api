# Python Imports

# Flask Imports

# Third-Party Imports

# App Imports
from app.blueprints.auth import auth
from app.utils import CustomResponse
from app.services import auth_service


from flask import request


@auth.route("/login/", methods=["POST"])
def login():
    """
    Login for all users

    :return: A response object containing the user's data and a JWT token
    """
    data = request.json
    response = auth_service.login(data)
    return CustomResponse.send_response(data=response)
