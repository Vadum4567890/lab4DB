from _decimal import Decimal
from datetime import datetime
from http import HTTPStatus
from typing import List

from flask_restx import abort

from ...service import loan_service
from ...domain import Loan
from ..general_controller import GeneralController

class LoanController(GeneralController):
    """
    Realization of Loan controller.
    """
    _service = loan_service

    def find_by_client_id(self, client_id: int) -> List[Loan]:
        """
        Gets objects from the database table by field client_id using the Service layer.
        :param client_id: client_id value
        :return: DTO for search objects
        """
        objects = self._service.find_by_client_id(client_id)
        if not objects:
            abort(HTTPStatus.NOT_FOUND)
        return [obj.put_into_dto() for obj in objects]

    def find_by_loan_amount_range(self, min_amount: Decimal, max_amount: Decimal) -> List[Loan]:
        """
        Gets objects from the database table by field loan_amount within a given range using the Service layer.
        :param min_amount: minimum loan amount value
        :param max_amount: maximum loan amount value
        :return: DTO for search objects
        """
        objects = self._service.find_by_loan_amount_range(min_amount, max_amount)
        if not objects:
            abort(HTTPStatus.NOT_FOUND)
        return [obj.put_into_dto() for obj in objects]

    def find_by_interest_rate(self, interest_rate: Decimal) -> List[Loan]:
        """
        Gets objects from the database table by field interest_rate using the Service layer.
        :param interest_rate: interest_rate value
        :return: DTO for search objects
        """
        objects = self._service.find_by_interest_rate(interest_rate)
        if not objects:
            abort(HTTPStatus.NOT_FOUND)
        return [obj.put_into_dto() for obj in objects]

    def find_by_start_date_range(self, start_date_min: datetime, start_date_max: datetime) -> List[Loan]:
        """
        Gets objects from the database table by field start_date within a given range using the Service layer.
        :param start_date_min: minimum start date value
        :param start_date_max: maximum start date value
        :return: DTO for search objects
        """
        objects = self._service.find_by_start_date_range(start_date_min, start_date_max)
        if not objects:
            abort(HTTPStatus.NOT_FOUND)
        return [obj.put_into_dto() for obj in objects]
