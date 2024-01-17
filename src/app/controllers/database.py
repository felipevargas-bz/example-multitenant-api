# Python Imports

# Flask Imports

# Third-Party Imports

# App Imports
from app.blueprints.application import api
from app.utils import CustomResponse
from app.services import db_service
from app.utils.functions import check_access


@api.route("/start_database", methods=["GET"])
@check_access(("Admin",))
def start_database():
    db_service.start_database()
    return CustomResponse.send_response(
        data={"ok": "Tablas creadas correctamente."},
        status_code=201,
    )


@api.route("/drop_tables", methods=["GET"])
@check_access(("Admin",))
def drop_tables():
    db_service.drop_tables()
    return CustomResponse.send_response(
        data={"dropped": "Tablas eliminadas correctamente."},
        status_code=201,
    )
