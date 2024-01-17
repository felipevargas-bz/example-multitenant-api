# Python Imports

# Flask Imports

# Third-Party Imports
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

# App Imports
from .model import Item


class ItemSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Item
        load_instance = True
