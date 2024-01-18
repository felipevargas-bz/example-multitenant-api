# Python Imports

# Flask Imports

# Third-Party Imports

# App Imports
from app.models.base_model import BaseModel, db


class User(BaseModel):
    __tablename__ = "users"

    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(50), nullable=False, server_default="User")
