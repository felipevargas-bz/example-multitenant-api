# Python Imports

# Flask Imports

# Third-Party Imports

# App Imports
from app.models.base_model import BaseModel, db


class Item(BaseModel):

    __tablename__ = "items"

    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(255), nullable=False)
