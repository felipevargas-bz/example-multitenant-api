# Python Imports

# Flask Imports

# Third-Party Imports
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

# App Imports
from .model import User


class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        exclude = ("password",)
