from os import path, environ

from dotenv import load_dotenv

base_dir = path.abspath(path.dirname(__name__))
load_dotenv(path.join(base_dir, '.env'))


class Config:
    SECRET_KEY = environ.get('SECRET_KEY')

    SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
