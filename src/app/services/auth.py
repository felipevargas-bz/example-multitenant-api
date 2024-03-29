# Python Imports
import os

# Flask Imports
from flask import g

# Third-Party Imports
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash

# App Imports
from app.models import User
from app.exceptions import InvalidCredentialsError, EmptyCredentialsError, DisabledUserError

AUTOMATIC_PROCESS_USERNAME = os.getenv("AUTOMATIC_PROCESS_USERNAME")
AUTOMATIC_PROCESS_PASSWORD = os.getenv("AUTOMATIC_PROCESS_PASSWORD")


class AuthService:
    def login(self, data):
        """
        Authenticate a user

        :param data: A dictionary containing the username and password
        :return: A response object containing the user's data and a JWT token
        """
        username = data.get("username")
        password = data.get("password")

        if not (username and password):
            raise EmptyCredentialsError("Usuario y/o contraseña vacíos.")

        auto_process_user = username == AUTOMATIC_PROCESS_USERNAME
        if auto_process_user:
            return self.login_auto_process_user(username, password)

        # Check if the user exists
        user_db = g.session.query(User).filter(User.username == username).first()

        if not user_db:
            raise InvalidCredentialsError("Usuario y/o contraseña incorrectos.")

        if not user_db.status:
            raise DisabledUserError("Usuario deshabilitado.")

        return self.generate_user_token(user_db, password)

    @staticmethod
    def generate_user_token(user_db, password):
        """
        generate a JWT token
        :param user_db:  The user
        :param password:  The password of the customer user
        :return:  A response object containing the customer user's data and a JWT token
        """
        # Check if the password is correct
        if not check_password_hash(user_db.password, password):
            raise InvalidCredentialsError("Usuario y/o contraseña incorrectos.")

        # Data to be stored in the JWT token
        useful_data = {
            "id": user_db.id,
            "username": user_db.username,
            "email": user_db.email,
            "role": user_db.role
        }

        access_token = create_access_token(identity=useful_data)

        response = {"access_token": access_token}

        return response

    @staticmethod
    def login_auto_process_user(username, password):
        """
        Login for automatic process user, automatic process user is a reserved user to other services that need to
        execute automatic tasks without the need of a human user.

        :param username: The username of the automatic process user
        :param password: The password of the automatic process user
        :return:  A response object containing the automatic process user's data and a JWT token
        """
        # Check if the password and username are correct
        if not (
                username == AUTOMATIC_PROCESS_USERNAME
                and password == AUTOMATIC_PROCESS_PASSWORD
        ):
            raise InvalidCredentialsError("Usuario y/o contraseña incorrectos.")

        useful_data = {
            "username": username,
            "role": "AutomaticProcess",
        }

        access_token = create_access_token(identity=useful_data)
        return {"access_token": access_token, "role": "AutomaticProcess"}


auth_service = AuthService()
