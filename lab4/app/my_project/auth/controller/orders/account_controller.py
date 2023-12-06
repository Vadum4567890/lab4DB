from _decimal import Decimal
from datetime import datetime
from http import HTTPStatus
from typing import List

from flask_restx import abort

from ...service import account_service
from ...domain import Account
from ..general_controller import GeneralController


class AccountController(GeneralController):
    _service = account_service

    def find_by_client_id(self, client_id: int) -> List[Account]:
        objects = self._service.find_by_client_id(client_id)
        if not objects:
            abort(HTTPStatus.NOT_FOUND)
        return [obj.put_into_dto() for obj in objects]

    def find_by_account_number(self, account_number: str) -> List[Account]:
        objects = self._service.find_by_account_number(account_number)
        if not objects:
            abort(HTTPStatus.NOT_FOUND)
        return [obj.put_into_dto() for obj in objects]

    def find_by_balance_range(self, min_balance: Decimal, max_balance: Decimal) -> List[Account]:
        objects = self._service.find_by_balance_range(min_balance, max_balance)
        if not objects:
            abort(HTTPStatus.NOT_FOUND)
        return [obj.put_into_dto() for obj in objects]