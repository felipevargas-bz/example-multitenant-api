# Python Imports

# Flask Imports

# Third-Party Imports

# App Imports
from app.models import User, UserSchema
from .base_service import BaseService


class UserService(BaseService):
    def __init__(self):
        super().__init__(User, UserSchema)


user_service = UserService()
