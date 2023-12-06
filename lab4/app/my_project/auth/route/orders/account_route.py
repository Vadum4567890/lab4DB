from _decimal import Decimal
from flask import Blueprint, jsonify, Response, request, make_response
from http import HTTPStatus

from ...controller import account_controller
from ...domain import Account

account_bp = Blueprint('accounts', __name__, url_prefix='/accounts')


@account_bp.get('')
def get_all_accounts() -> Response:
    """
    Gets all accounts from the table using the Service layer.
    :return: Response object
    """
    return make_response(jsonify(account_controller.find_all()), HTTPStatus.OK)


@account_bp.post('')
def create_account() -> Response:
    """
    Creates a new account using the Service layer.
    :return: Response object
    """
    content = request.get_json()
    account = Account.create_from_dto(content)
    account_controller.create(account)
    return make_response(jsonify(account.put_into_dto()), HTTPStatus.CREATED)


@account_bp.get('/id/<int:account_id>')
def get_account(account_id: int) -> Response:
    """
    Gets an account by ID.
    :return: Response object
    """
    return make_response(jsonify(account_controller.find_by_id(account_id)), HTTPStatus.OK)


@account_bp.get('/client/<int:client_id>')
def get_accounts_by_client(client_id: int) -> Response:
    """
    Gets accounts by client ID.
    :return: Response object
    """
    return make_response(jsonify(account_controller.find_by_client_id(client_id)), HTTPStatus.OK)


@account_bp.get('/number/<string:account_number>')
def get_account_by_number(account_number: str) -> Response:
    """
    Gets an account by account number.
    :return: Response object
    """
    return make_response(jsonify(account_controller.find_by_account_number(account_number)), HTTPStatus.OK)


@account_bp.get('/balance/<float:min_balance>/<float:max_balance>')
def get_accounts_by_balance_range(min_balance: Decimal, max_balance: Decimal) -> Response:
    """
    Gets accounts by balance range.
    :return: Response object
    """
    return make_response(jsonify(account_controller.find_by_balance_range(min_balance, max_balance)), HTTPStatus.OK)


@account_bp.put('/<int:account_id>')
def update_account(account_id: int) -> Response:
    """
    Updates an account by ID.
    :return: Response object
    """
    content = request.get_json()
    account = Account.create_from_dto(content)
    account_controller.update(account_id, account)
    return make_response("Account updated", HTTPStatus.OK)


@account_bp.patch('/<int:account_id>')
def patch_account(account_id: int) -> Response:
    """
    Patches an account by ID.
    :return: Response object
    """
    content = request.get_json()
    account_controller.patch(account_id, content)
    return make_response("Account updated", HTTPStatus.OK)


@account_bp.delete('/<int:account_id>')
def delete_account(account_id: int) -> Response:
    """
    Deletes an account by ID.
    :return: Response object
    """
    account_controller.delete(account_id)
    return make_response("Account deleted", HTTPStatus.OK)
