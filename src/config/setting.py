# Python Imports
import os
from datetime import timedelta

# Flask Imports

# Third-Party Imports
from dotenv import load_dotenv

# App Imports

load_dotenv()


class DBConfig:
    # Database
    db_host = os.getenv("DB_HOST")
    db_port = os.getenv("DB_PORT")
    db_name = os.getenv("DB_NAME")
    db_user = os.getenv("DB_USER")
    db_pass = os.getenv("DB_PASS")


class SQLAlchemyConfig:
    # For SQL Alchemy
    SQLALCHEMY_DATABASE_URI = (
        "mysql+pymysql://{user}:{password}@{host}:{port}/{tenant}?charset=utf8".format(
            user=DBConfig.db_user,
            password=DBConfig.db_pass,
            host=DBConfig.db_host,
            port=DBConfig.db_port,
            tenant="909123123",
        )
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_BINDS = dict()
    APPLICATIONINSIGHTS_CONNECTION_STRING = os.getenv(
        "APPLICATIONINSIGHTS_CONNECTION_STRING"
    )


class JWTConfig:
    JWT_SECRET_KEY = os.getenv("SECRET_KEY")
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=3)


class Setting(
    DBConfig, SQLAlchemyConfig, JWTConfig
):
    # App
    name = os.getenv("APP_NAME")
    host = os.getenv("APP_HOST")
    port = os.getenv("APP_PORT")
    debug = os.getenv("APP_DEBUG")
    api_name = os.getenv("APP_API")
    time_zone = os.getenv("TZ")
    DEBUG = bool(debug)
    ENV = os.environ["APP_ENVIRONMENT"]
    SECRET_KEY = os.environ["SECRET_KEY"]

    # Content Length 200 Mb
    MAX_CONTENT_LENGTH = 200 * 1024 * 1024
