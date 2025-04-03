from os import environ

from dotenv import load_dotenv

load_dotenv()


class Config:
    # General pattern
    # mssql+pyodbc://<username>:<password>@<dsn_name>?driver=<driver_name>
    # mssql+pyodbc://@<server_name>/<db_name>?driver=<driver_name>
    SQLALCHEMY_DATABASE_URI = environ.get("LOCAL_DATABASE_URL")
    SECRET_KEY = environ.get("SECRET_KEY")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = environ.get("SECRET_KEY")
