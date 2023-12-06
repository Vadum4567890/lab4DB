from _decimal import Decimal
from datetime import datetime
from http import HTTPStatus
from typing import List

from flask_restx import abort

from ...service import client_service
from ...domain import Client
from ..general_controller import GeneralController


class ClientController(GeneralController):
    _service = client_service

    def find_by_email(self, email: str) -> List[Client]:
        objects = self._service.find_by_email(email)
        if not objects:
            abort(HTTPStatus.NOT_FOUND)
        return [obj.put_into_dto() for obj in objects]

    def find_by_phone_number(self, phone_number: str) -> List[Client]:
        objects = self._service.find_by_phone_number(phone_number)
        if not objects:
            abort(HTTPStatus.NOT_FOUND)
        return [obj.put_into_dto() for obj in objects]