from typing import List
from decimal import Decimal
from datetime import datetime

from ...dao import loan_dao
from ...domain import Loan
from ..general_service import GeneralService

class LoanService(GeneralService):
    """
    Realization of Loan service.
    """
    _dao = loan_dao

    def find_by_client_id(self, client_id: int) -> List[Loan]:
        """
        Gets objects from the database table by field client_id using the Data Access layer.
        :param client_id: client_id value
        :return: search objects
        """
        objects = self._dao.find_by_client_id(client_id)
        return objects

    def find_by_loan_amount_range(self, min_amount: Decimal, max_amount: Decimal) -> List[Loan]:
        """
        Gets objects from the database table by field loan_amount within a given range using the Data Access layer.
        :param min_amount: minimum loan amount value
        :param max_amount: maximum loan amount value
        :return: search objects
        """
        objects = self._dao.find_by_loan_amount_range(min_amount, max_amount)
        return objects

    def find_by_interest_rate(self, interest_rate: Decimal) -> List[Loan]:
        """
        Gets objects from the database table by field interest_rate using the Data Access layer.
        :param interest_rate: interest_rate value
        :return: search objects
        """
        objects = self._dao.find_by_interest_rate(interest_rate)
        return objects

    def find_by_start_date_range(self, start_date_min: datetime, start_date_max: datetime) -> List[Loan]:
        """
        Gets objects from the database table by field start_date within a given range using the Data Access layer.
        :param start_date_min: minimum start date value
        :param start_date_max: maximum start date value
        :return: search objects
        """
        objects = self._dao.find_by_start_date_range(start_date_min, start_date_max)
        return objects