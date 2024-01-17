# Python Imports
import os

# Flask Imports

# Third-Party Imports
from dotenv import load_dotenv

# App Imports
from app import application

load_dotenv()

if __name__ == "__main__":
    app_host = os.getenv("APP_HOST")
    app_port = int(os.getenv("APP_PORT"))
    application.run(host=app_host, port=app_port, debug=False)
