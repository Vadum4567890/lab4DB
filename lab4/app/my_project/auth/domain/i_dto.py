from abc import abstractmethod
from typing import Dict


class IDto:
    """
    Interface to put and extract DTO objects to/from domain objects.
    """

    @abstractmethod
    def put_into_dto(self) -> Dict[str, object]:
        pass

    @staticmethod
    @abstractmethod
    def create_from_dto(dto_dict: Dict[str, object]) -> object:
        pass