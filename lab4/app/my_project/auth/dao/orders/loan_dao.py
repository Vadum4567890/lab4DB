from typing import List
from decimal import Decimal
from datetime import datetime

from ..general_dao import GeneralDAO
from ...domain import Loan


class LoanDAO(GeneralDAO):
    """
    Realization of Loan data access layer.
    """
    _domain_type = Loan

    def find_by_client_id(self, client_id: int) -> List[object]:
        """
        Gets Loan objects from the database table by field client_id.
        :param client_id: client_id value
        :return: search objects
        """
        return self._session.query(self._domain_type).filter(Loan.client_id == client_id).all()

    def find_by_loan_amount_range(self, min_amount: Decimal, max_amount: Decimal) -> List[object]:
        """
        Gets Loan objects from the database table by field loan_amount within a given range.
        :param min_amount: minimum loan amount value
        :param max_amount: maximum loan amount value
        :return: search objects
        """
        return self._session.query(self._domain_type).filter(Loan.loan_amount.between(min_amount, max_amount)).all()

    def find_by_interest_rate(self, interest_rate: Decimal) -> List[object]:
        """
        Gets Loan objects from the database table by field interest_rate.
        :param interest_rate: interest_rate value
        :return: search objects
        """
        return self._session.query(self._domain_type).filter(Loan.interest_rate == interest_rate).all()

    def find_by_start_date_range(self, start_date_min: datetime, start_date_max: datetime) -> List[object]:
        """
        Gets Loan objects from the database table by field start_date within a given range.
        :param start_date_min: minimum start date value
        :param start_date_max: maximum start date value
        :return: search objects
        """
        return self._session.query(self._domain_type).filter(Loan.start_date.between(start_date_min, start_date_max)).all()
