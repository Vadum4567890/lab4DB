from typing import List

from ...dao import client_dao
from ...domain import Client
from ..general_service import GeneralService


class ClientService(GeneralService):
    """
    Realization of Client service.
    """
    _dao = client_dao

    def find_by_email(self, email: str) -> List[Client]:
        """
        Gets objects from the database table by field email using the Data Access layer.
        :param email: email value
        :return: search objects
        """
        objects = self._dao.find_by_email(email)
        return objects

    def find_by_phone_number(self, phone_number: str) -> List[Client]:
        """
        Gets objects from the database table by field phone_number using the Data Access layer.
        :param phone_number: phone_number value
        :return: search objects
        """
        objects = self._dao.find_by_phone_number(phone_number)
        return objects