# Python Imports

# Flask Imports
from flask import request

# Third-Party Imports

# App Imports
from app.blueprints.application import api
from app.utils import CustomResponse
from app.services import user_service
from app.utils.functions import check_access


@api.route("/users", methods=["GET"])
@check_access(("Admin",))
def get_users():
    query_parameters = request.args.to_dict()
    response = user_service.get_all(query_parameters)
    return CustomResponse.send_response(data=response)


@api.route("/users/<int:user_id>", methods=["GET"])
@check_access(("Admin",))
def get_user(user_id):
    response = user_service.get_by_id(user_id)
    return CustomResponse.send_response(data=response)


@api.route("/users/", methods=["POST"])
def create_users():
    data_to_process = request.json
    user_service.create(data_to_process)
    return CustomResponse.send_response(
        data={"created": "Registro creado correctamente."},
        status_code=201,
    )


@api.route("/users/admin/", methods=["POST"])
@check_access(("AutomaticProcess",))
def create_admin_users():
    data_to_process = request.json
    user_service.create_admin_user(data_to_process)
    return CustomResponse.send_response(
        data={"created": "Registro creado correctamente."},
        status_code=201,
    )


@api.route("/users/<int:user_id>/", methods=["PUT"])
@check_access(("Admin",))
def update_users(user_id):
    data_to_process = request.json
    user_service.update(user_id, data_to_process)
    return CustomResponse.send_response(
        data={"updated": "Registro actualizado correctamente."},
        status_code=200,
    )


@api.route("/users/<int:user_id>/", methods=["DELETE"])
@check_access(("Admin",))
def delete_users(user_id):
    user_service.delete(user_id)
    return CustomResponse.send_response(
        data={"deleted": "Registro eliminado correctamente."},
        status_code=200,
    )
