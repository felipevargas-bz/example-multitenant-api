# Python Imports

# Flask Imports
from flask import g

# Third-Party Imports
from sqlalchemy import text

# App Imports
from app.database.db_tenants import Base


class DatabaseService:
    def __init__(self):
        pass

    @staticmethod
    def create_tables():
        Base.metadata.create_all(g.engine)

    @staticmethod
    def drop_tables():
        Base.metadata.drop_all(g.engine)


db_service = DatabaseService()
