# Python Imports

# Flask Imports

# Third-Party Imports

# App Imports
from app.blueprints.application import api
from app.utils import CustomResponse
from app.services import db_service
from app.utils.functions import check_access


@api.route("/create_tables", methods=["GET"])
@check_access(("AutomaticProcess",))
def start_database():
    db_service.create_tables()
    return CustomResponse.send_response(
        data={"ok": "Tablas creadas correctamente."},
        status_code=201,
    )


@api.route("/drop_tables", methods=["GET"])
@check_access(("AutomaticProcess",))
def drop_tables():
    db_service.drop_tables()
    return CustomResponse.send_response(
        data={"dropped": "Tablas eliminadas correctamente."},
        status_code=201,
    )
