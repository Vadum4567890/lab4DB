from typing import List


from ..general_dao import GeneralDAO
from ...domain import Client


class ClientDAO(GeneralDAO):
    """
    Realization of Client data access layer.
    """
    _domain_type = Client

    def find_by_email(self, email: str) -> List[object]:
        """
        Gets Client objects from the database table by field email.
        :param email: email value
        :return: search objects
        """
        return self._session.query(self._domain_type).filter(Client.email == email).all()

    def find_by_phone_number(self, phone_number: str) -> List[object]:
        """
        Gets Client objects from the database table by field phone_number.
        :param phone_number: phone_number value
        :return: search objects
        """
        return self._session.query(self._domain_type).filter(Client.phone_number == phone_number).all()
