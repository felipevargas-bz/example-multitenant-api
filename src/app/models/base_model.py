# Python Imports

# Flask Imports

# Third-Party Imports
from pymysql.err import IntegrityError, OperationalError

# App Imports
from app import db
from app.database.db_tenants import Base
from app.exceptions import AppIntegrityError, MySQLConnectionError, BaseError


class BaseModel(Base):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.SMALLINT, server_default="1")

    def save(self):
        try:
            db.session.add(self)
            db.session.flush()
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            raise AppIntegrityError("No se pudo guardar el registro")
        except OperationalError as e:
            db.session.rollback()
            raise MySQLConnectionError(str(e))
        except Exception as e:
            db.session.rollback()
            raise BaseError(str(e))

    def remove(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise BaseError(str(e))
