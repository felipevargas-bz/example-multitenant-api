# Python Imports

# Flask Imports
from flask import request

# Third-Party Imports

# App Imports
from app.blueprints.application import api
from app.utils import CustomResponse
from app.services import item_service
from app.utils.functions import check_access


@api.route("/items", methods=["GET"])
@check_access(("Admin",))
def get_items():
    query_parameters = request.args.to_dict()
    response = item_service.get_all(query_parameters)
    return CustomResponse.send_response(data=response)


@api.route("/items/<int:item_id>", methods=["GET"])
@check_access(("Admin", "User"))
def get_item(item_id):
    response = item_service.get_by_id(item_id)
    return CustomResponse.send_response(data=response)


@api.route("/items/", methods=["POST"])
@check_access(("Admin",))
def create_items():
    data_to_process = request.json
    item_service.create(data_to_process)
    return CustomResponse.send_response(
        data={"created": "Registro creado correctamente."},
        status_code=201,
    )


@api.route("/items/<int:item_id>/", methods=["PUT"])
@check_access(("Admin",))
def update_items(item_id):
    data_to_process = request.json
    item_service.update(item_id, data_to_process)
    return CustomResponse.send_response(
        data={"updated": "Registro actualizado correctamente."},
        status_code=200,
    )


@api.route("/items/<int:item_id>/", methods=["DELETE"])
@check_access(("Admin",))
def delete_items(item_id):
    item_service.delete(item_id)
    return CustomResponse.send_response(
        data={"deleted": "Registro eliminado correctamente."},
        status_code=200,
    )
