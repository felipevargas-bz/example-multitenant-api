"""
    Erros
"""
# Python Imports

# Flask Imports
from flask import jsonify

# Third-Party Imports

# App Imports


class BaseError(Exception):
    """ """
    code = 500
    message = "Hemos tenido un problema, por favor intente nuevamente"
    type = "Error interno"

    def __init__(self, message: str = None, code: int = None):
        self.message = message or self.__get_message()
        self.code = code or self.__get_code()

    @classmethod
    def __get_code(cls):
        return cls.code

    @classmethod
    def __get_message(cls):
        return cls.message

    @classmethod
    def __get_type(cls):
        return cls.type

    def get_response(self):
        return jsonify({"msg": self.message, "type": self.__get_type()}), self.code


class ValidationError(BaseError):
    """ """
    code = 400
    message = "Error de validación"
    type = "Error de validación"


class AppIntegrityError(BaseError):
    """ """
    code = 409
    message = "Error de integridad"
    type = "Error de integridad"


class InternalServerError(BaseError):
    """ """
    code = 500
    message = "Error interno"
    type = "Error interno"


class BadRequest(BaseError):
    """ """
    code = 400
    message = "Solicitud incorrecta"
    type = "Solicitud incorrecta"


class ExternalAPIError(BaseError):
    """ """
    code = 500
    message = "Error de API externa"
    type = "Error de API externa"


class NotFoundError(BaseError):
    """ """
    code = 404
    message = "No encontrado"
    type = "Recurso no encontrado"


class UnauthorizedError(BaseError):
    """ """
    code = 401
    message = "No autorizado"
    type = "No autorizado"


class ApplicationError(BaseError):
    """ """
    code = 500
    message = "Error de aplicación"
    type = "Error de aplicación"


class MySQLConnectionError(BaseError):
    """ """
    code = 500
    message = "Error de conexión a la base de datos"
    type = "Error de conexión a la base de datos"


class TenantNotFound(BaseError):
    """ """
    code = 404
    message = "Instancia no encontrada"
    type = "Instancia no encontrada"


class DisabledTenant(BaseError):
    """ """
    code = 404
    message = "Instancia deshabilitada"
    type = "Instancia deshabilitada"


class InvalidCredentialsError(BaseError):
    """ """
    code = 401
    message = "Credenciales inválidas"
    type = "Credenciales inválidas"


class EmptyCredentialsError(BaseError):
    """ """
    code = 401
    message = "Credenciales vacías"
    type = "Credenciales vacías"


class DisabledUserError(BaseError):
    """ """
    code = 401
    message = "Usuario deshabilitado"
    type = "Usuario deshabilitado"


class InvalidTokenError(BaseError):
    """ """
    code = 401
    message = "Token inválido"
    type = "Token inválido"


class HTTPError(BaseError):
    """ """
    code = 500
    message = "Error HTTP"
    type = "Error HTTP"
