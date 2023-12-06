from typing import List
from decimal import Decimal
from datetime import datetime

from ..general_dao import GeneralDAO
from ...domain import Account, Client, Loan

class AccountDAO(GeneralDAO):
    """
    Realization of Account data access layer.
    """
    _domain_type = Account

    def find_by_client_id(self, client_id: int) -> List[object]:
        """
        Gets Account objects from the database table by field client_id.
        :param client_id: client_id value
        :return: search objects
        """
        return self._session.query(self._domain_type).filter(Account.client_id == client_id).all()

    def find_by_account_number(self, account_number: str) -> List[object]:
        """
        Gets Account objects from the database table by field account_number.
        :param account_number: account_number value
        :return: search objects
        """
        return self._session.query(self._domain_type).filter(Account.account_number == account_number).all()

    def find_by_balance_range(self, min_balance: Decimal, max_balance: Decimal) -> List[object]:
        """
        Gets Account objects from the database table by field balance within a given range.
        :param min_balance: minimum balance value
        :param max_balance: maximum balance value
        :return: search objects
        """
        return self._session.query(self._domain_type).filter(Account.balance.between(min_balance, max_balance)).all()
