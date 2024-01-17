# Python Imports

# Flask Imports
from flask import request, g

# Third-Party Imports

# App Imports
from app.exceptions import TenantNotFound


def middleware_tenant(application, db):

    if request.method != "OPTIONS":
        from app.database import DBTenant

        tenant = request.headers.get("tenant")
        if not tenant:
            raise TenantNotFound("No ha enviado el parámetro tenant en los headers")

        g.tenant = tenant
        session, engine = DBTenant.get_tenant_session(application=application, tenant_name=tenant)

        g.session = session
        g.engine = engine
        db.session = session

        # Asignamos la url almacenado en el bind
        application.config["SQLALCHEMY_DATABASE_URI"] = application.config["SQLALCHEMY_BINDS"][tenant]
