import os
from http import HTTPStatus
import secrets
from typing import Dict, Any

from flask import Flask
from flask_restx import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists, create_database
from flask_cors import CORS
from .auth.route import register_routes

SECRET_KEY = "SECRET_KEY"
SQLALCHEMY_DATABASE_URI = "SQLALCHEMY_DATABASE_URI"
MYSQL_ROOT_USER = "root"
MYSQL_ROOT_PASSWORD = '1234'


# Database
db = SQLAlchemy()

todos = {}


def create_app(app_config: Dict[str, Any], additional_config: Dict[str, Any]) -> Flask:
    """
    Creates Flask application
    :param app_config: Flask configuration
    :param additional_config: additional configuration
    :return: Flask application object
    """
    _process_input_config(app_config, additional_config)
    app = Flask(__name__)
    app.config["SECRET_KEY"] = secrets.token_hex(16)
    app.config = {**app.config, **app_config}

    _init_db(app)  # Initialize the database

    register_routes(app)
    _init_swagger(app)
    CORS(app)
    return app


def _init_swagger(app: Flask) -> None:
    # A-lia Swagger
    restx_api = Api(app, title='Meuf test backend',
                    description='A simple backend')  # https://flask-restx.readthedocs.io/

    @restx_api.route('/number/<string:todo_id>')
    class TodoSimple(Resource):
        @staticmethod
        def get(todo_id):
            return todos, 202

        @staticmethod
        def put(todo_id):
            todos[todo_id] = todo_id
            return todos, HTTPStatus.CREATED

    @app.route("/hi")
    def hello_world():
        return todos, HTTPStatus.OK


def _init_db(app: Flask) -> None:
    """
    Initializes DB with SQLAlchemy
    :param app: Flask application object
    """
    try:
        print("Initializing SQLAlchemy...")
        db.init_app(app)

        if not database_exists(app.config[SQLALCHEMY_DATABASE_URI]):
            print("Creating database...")
            create_database(app.config[SQLALCHEMY_DATABASE_URI])
            print("Database created.")
        else:
            with app.app_context():
                db.drop_all()

        from .auth import domain
        with app.app_context():
            db.create_all()
    except Exception as e:
        print("Exception during database initialization:", e)


def _process_input_config(app_config: Dict[str, Any], additional_config: Dict[str, Any]) -> None:
    """
    Processes input configuration
    :param app_config: Flask configuration
    :param additional_config: additional configuration
    """
    # Get root username and password
    root_user = additional_config.get('MYSQL_ROOT_USER', "")
    root_password = additional_config.get('MYSQL_ROOT_PASSWORD', "")
    # Set root username and password in app_config using f-string
    app_config[SQLALCHEMY_DATABASE_URI] = f"mysql://{root_user}:{root_password}@localhost/privatbankrm"

