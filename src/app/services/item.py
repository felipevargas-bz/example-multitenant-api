# Python Imports

# Flask Imports

# Third-Party Imports

# App Imports
from app.models import Item, ItemSchema
from .base_service import BaseService


class ItemService(BaseService):
    def __init__(self):
        super().__init__(Item, ItemSchema)


item_service = ItemService()
