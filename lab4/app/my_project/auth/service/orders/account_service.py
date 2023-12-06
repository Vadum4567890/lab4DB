from typing import List
from decimal import Decimal

from ...dao import account_dao
from ...domain import Account
from ..general_service import GeneralService

class AccountService(GeneralService):
    """
    Realization of Account service.
    """
    _dao = account_dao

    def find_by_client_id(self, client_id: int) -> List[Account]:
        """
        Gets objects from the database table by field client_id using the Data Access layer.
        :param client_id: client_id value
        :return: search objects
        """
        objects = self._dao.find_by_client_id(client_id)
        return objects

    def find_by_account_number(self, account_number: str) -> List[Account]:
        """
        Gets objects from the database table by field account_number using the Data Access layer.
        :param account_number: account_number value
        :return: search objects
        """
        objects = self._dao.find_by_account_number(account_number)
        return objects

    def find_by_balance_range(self, min_balance: Decimal, max_balance: Decimal) -> List[Account]:
        """
        Gets objects from the database table by field balance within a given range using the Data Access layer.
        :param min_balance: minimum balance value
        :param max_balance: maximum balance value
        :return: search objects
        """
        objects = self._dao.find_by_balance_range(min_balance, max_balance)
        return objects
