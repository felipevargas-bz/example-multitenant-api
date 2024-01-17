# Python Imports
from functools import wraps
from typing import Union
import os

# Flask Imports
from flask import g

# Third-Party Imports
from sqlalchemy.exc import OperationalError
from flask_jwt_extended import get_current_user, verify_jwt_in_request

# App Imports
from extensions import jwt
from app.models import User
from app.exceptions import MySQLConnectionError, ValidationError, UnauthorizedError


AUTOMATIC_PROCESS_USERNAME = os.getenv("AUTOMATIC_PROCESS_USERNAME")


@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    """callback for fetching authenticated user from db"""
    try:
        username = jwt_data["sub"]["username"]
        g.pymes_plus_token = jwt_data["sub"]["pymes_plus_token"]

        if username == AUTOMATIC_PROCESS_USERNAME:
            return jwt_data["sub"]
        entity = (
            admin
            if (admin := g.session.query(Admin).filter(Admin.username == username).first())
            else g.session.query(CustomerUser)
            .filter(CustomerUser.username == username)
            .first()
        )
        g.current_user = entity
        return entity
    except OperationalError as e:
        raise MySQLConnectionError(str(e))
    except KeyError as e:
        raise ValidationError(f"La llave {e} no existe en los datos del token")


# @check_access decorator function
def check_access(roles: tuple = ()):
    def decorator(f):
        @wraps(f)
        def decorator_function(*args, **kwargs):
            try:
                # calling @jwt_required()
                verify_jwt_in_request()
                # fetching current user from db
                current_user: Union[Admin, CustomerUser, dict] = get_current_user()
                role = (
                    current_user["role"]
                    if isinstance(current_user, dict)
                    else current_user.role
                )

                # checking user role
                if role not in roles:
                    raise UnauthorizedError(
                        f"Acceso denegado. No tienes permisos para acceder a este recurso."
                    )
                return f(*args, **kwargs)

            except KeyError as e:
                raise ValidationError(f"La llave {e} no existe en los datos del usuario actual")
            except AttributeError as e:
                raise ValidationError(f"{e}")

        return decorator_function

    return decorator
