# Python Imports

# Flask Imports
from flask import Flask, make_response, jsonify

# Third-Party Imports
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# App Imports
from config import Setting
from app.utils import CustomResponse
from extensions import extensions
from .exceptions import TenantNotFound
from app.middlewares import middleware_tenant
from app.error_handler import ErrorHandler

db = SQLAlchemy()


def create_application():
    # apply configuration
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Setting)

    CORS(app)
    db.init_app(app)

    api_url_prefix = "/api"
    auth_url_prefix = "/auth"
    with app.app_context():
        from app.blueprints.application import api
        from app.blueprints.auth import auth

        app.register_blueprint(auth, url_prefix=auth_url_prefix)
        app.register_blueprint(api, url_prefix=api_url_prefix)

    return app


# Create App
application = create_application()
# Register Extensions
for extension in extensions:
    extension.init_app(application)


@application.before_request
def before_request():
    middleware_tenant(application, db)


@application.errorhandler(Exception)
def handle_error(error):
    return ErrorHandler().handle_error(error)


@application.route("/", methods=["GET"])
def root_route():
    response = dict(
        message="The application is running", mode=f"Debug: {bool(Setting.debug)}"
    )
    return make_response(jsonify(response), 200)


@application.teardown_request
def remove_session(param):
    db.session.remove()
