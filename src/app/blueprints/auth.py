# Python Imports

# Flask Imports
from flask import Blueprint

# Third-Party Imports


auth = Blueprint("auth", __name__)

"""
Aquí se importan todos los controladores de el blueprint auth
"""
from app.controllers import auth_controller
