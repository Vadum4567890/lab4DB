from __future__ import annotations
from typing import Dict, Any
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from .... import db
from ..i_dto import IDto


class Client(db.Model, IDto):
    __tablename__ = "clients"

    client_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    phone_number = db.Column(db.String(20))

    accounts = db.relationship("Account", backref="client", lazy=True)
    loans = db.relationship("Loan", backref="client", lazy=True)

    def __repr__(self) -> str:
        return f"Client({self.client_id}, '{self.first_name}', '{self.last_name}', '{self.email}', '{self.phone_number}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "client_id": self.client_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "phone_number": self.phone_number
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Client:
        return Client(
            first_name=dto_dict.get("first_name"),
            last_name=dto_dict.get("last_name"),
            email=dto_dict.get("email"),
            phone_number=dto_dict.get("phone_number")
        )
