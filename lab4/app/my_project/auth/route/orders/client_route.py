from flask import Blueprint, jsonify, Response, request, make_response
from http import HTTPStatus

from ...controller import client_controller
from ...domain import Client

client_bp = Blueprint('clients', __name__, url_prefix='/clients')


@client_bp.get('')
def get_all_clients() -> Response:
    """
    Gets all clients from the table using the Service layer.
    :return: Response object
    """
    return make_response(jsonify(client_controller.find_all()), HTTPStatus.OK)


@client_bp.post('')
def create_client() -> Response:
    """
    Creates a new client using the Service layer.
    :return: Response object
    """
    content = request.get_json()
    client = Client.create_from_dto(content)
    client_controller.create(client)
    return make_response(jsonify(client.put_into_dto()), HTTPStatus.CREATED)


@client_bp.get('/id/<int:client_id>')
def get_client(client_id: int) -> Response:
    """
    Gets a client by ID.
    :return: Response object
    """
    return make_response(jsonify(client_controller.find_by_id(client_id)), HTTPStatus.OK)


@client_bp.get('/email/<string:email>')
def get_client_by_email(email: str) -> Response:
    """
    Gets a client by email.
    :return: Response object
    """
    return make_response(jsonify(client_controller.find_by_email(email)), HTTPStatus.OK)


@client_bp.get('/phone/<string:phone_number>')
def get_client_by_phone(phone_number: str) -> Response:
    """
    Gets a client by phone number.
    :return: Response object
    """
    return make_response(jsonify(client_controller.find_by_phone_number(phone_number)), HTTPStatus.OK)


@client_bp.put('/<int:client_id>')
def update_client(client_id: int) -> Response:
    """
    Updates a client by ID.
    :return: Response object
    """
    content = request.get_json()
    client = Client.create_from_dto(content)
    client_controller.update(client_id, client)
    return make_response("Client updated", HTTPStatus.OK)


@client_bp.patch('/<int:client_id>')
def patch_client(client_id: int) -> Response:
    """
    Patches a client by ID.
    :return: Response object
    """
    content = request.get_json()
    client_controller.patch(client_id, content)
    return make_response("Client updated", HTTPStatus.OK)


@client_bp.delete('/<int:client_id>')
def delete_client(client_id: int) -> Response:
    """
    Deletes a client by ID.
    :return: Response object
    """
    client_controller.delete(client_id)
    return make_response("Client deleted", HTTPStatus.OK)