import datetime

from _decimal import Decimal
from flask import Blueprint, jsonify, Response, request, make_response
from http import HTTPStatus

from ...controller import loan_controller
from ...domain import Loan

loan_bp = Blueprint('loans', __name__, url_prefix='/loans')


@loan_bp.get('')
def get_all_loans() -> Response:
    """
    Gets all loans from the table using the Service layer.
    :return: Response object
    """
    return make_response(jsonify(loan_controller.find_all()), HTTPStatus.OK)


@loan_bp.post('')
def create_loan() -> Response:
    """
    Creates a new loan using the Service layer.
    :return: Response object
    """
    content = request.get_json()
    loan = Loan.create_from_dto(content)
    loan_controller.create(loan)
    return make_response(jsonify(loan.put_into_dto()), HTTPStatus.CREATED)


@loan_bp.get('/id/<int:loan_id>')
def get_loan(loan_id: int) -> Response:
    """
    Gets a loan by ID.
    :return: Response object
    """
    return make_response(jsonify(loan_controller.find_by_id(loan_id)), HTTPStatus.OK)


@loan_bp.get('/client/<int:client_id>')
def get_loans_by_client(client_id: int) -> Response:
    """
    Gets loans by client ID.
    :return: Response object
    """
    return make_response(jsonify(loan_controller.find_by_client_id(client_id)), HTTPStatus.OK)


@loan_bp.get('/amount/<float:loan_amount>')
def get_loans_by_amount(loan_amount: Decimal) -> Response:
    """
    Gets loans by loan amount.
    :return: Response object
    """
    return make_response(jsonify(loan_controller.find_by_loan_amount(loan_amount)), HTTPStatus.OK)


@loan_bp.get('/interest_rate/<float:interest_rate>')
def get_loans_by_interest_rate(interest_rate: Decimal) -> Response:
    """
    Gets loans by interest rate.
    :return: Response object
    """
    return make_response(jsonify(loan_controller.find_by_interest_rate(interest_rate)), HTTPStatus.OK)


@loan_bp.get('/start_date/<path:start_date>')
def get_loans_by_start_date(start_date: datetime) -> Response:
    """
    Gets loans by start date.
    :return: Response object
    """
    try:
        parsed_date = datetime.strptime(start_date, '%Y-%m-%dT%H:%M:%S')
        return parsed_date,\
            make_response(jsonify(loan_controller.find_by_start_date(start_date)), HTTPStatus.OK)
    except ValueError:
        return "Invalid datetime format"


@loan_bp.put('/<int:loan_id>')
def update_loan(loan_id: int) -> Response:
    """
    Updates a loan by ID.
    :return: Response object
    """
    content = request.get_json()
    loan = Loan.create_from_dto(content)
    loan_controller.update(loan_id, loan)
    return make_response("Loan updated", HTTPStatus.OK)


@loan_bp.patch('/<int:loan_id>')
def patch_loan(loan_id: int) -> Response:
    """
    Patches a loan by ID.
    :return: Response object
    """
    content = request.get_json()
    loan_controller.patch(loan_id, content)
    return make_response("Loan updated", HTTPStatus.OK)


@loan_bp.delete('/<int:loan_id>')
def delete_loan(loan_id: int) -> Response:
    """
    Deletes a loan by ID.
    :return: Response object
    """
    loan_controller.delete(loan_id)
    return make_response("Loan deleted", HTTPStatus.OK)
