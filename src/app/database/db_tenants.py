# Python Imports

# Flask Imports

# Third-Party Imports
from sqlalchemy.pool import NullPool
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base
from sqlalchemy.exc import OperationalError

# App Imports
from config import Setting
from app.exceptions import DisabledTenant, MySQLConnectionError


Base = declarative_base()


# DATABASE SETTINGS
class DBTenant:

    @staticmethod
    def get_known_tenants(tenant: str):
        """
        Verifica que la instancia exista en el dashboard
        :param tenant: str
        :return: True or False
        """
        # Esta función se encarga de verificar que el tenant exista en el dashboard y que esté habilitado
        # para poder conectarse a la base de datos.
        # En este caso al ser un proyecto de prueba, se asume que el tenant existe y está habilitado.
        return True

    @staticmethod
    def prepare_bind(tenant_name: str, application):
        """
        Crea la conexión en caso de no existir
        """
        if tenant_name not in application.config["SQLALCHEMY_BINDS"]:
            mysql_uri = "mysql+pymysql://{user}:{password}@{host}:{port}/{tenant}?charset=utf8".format(
                user=Setting.db_user,
                password=Setting.db_pass,
                host=Setting.db_host,
                port=Setting.db_port,
                tenant=tenant_name,
            )
            application.config["SQLALCHEMY_BINDS"][tenant_name] = mysql_uri
            application.config["SQLALCHEMY_DATABASE_URI"] = mysql_uri
        return application.config["SQLALCHEMY_BINDS"][tenant_name]

    @staticmethod
    def get_tenant_session(application, tenant_name: str):
        try:
            if not DBTenant.get_known_tenants(tenant=tenant_name):
                raise DisabledTenant("La instancia no se encuentra habilitada")
            url = DBTenant.prepare_bind(tenant_name=tenant_name, application=application)
            engine = create_engine(url=url, poolclass=NullPool)
            session = scoped_session(sessionmaker(autocommit=False, bind=engine))

            return session, engine
        except OperationalError as e:
            raise MySQLConnectionError(str(e))
