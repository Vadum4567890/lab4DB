from __future__ import annotations
from typing import Dict, Any
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from .... import db
from ..i_dto import IDto


class Account(db.Model, IDto):
    __tablename__ = "accounts"

    account_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    client_id = db.Column(db.Integer, db.ForeignKey('clients.client_id'))
    account_number = db.Column(db.String(20), unique=True)
    balance = db.Column(db.DECIMAL(10, 2))

    def __repr__(self) -> str:
        return f"Account({self.account_id}, {self.client_id}, '{self.account_number}', {self.balance})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "account_id": self.account_id,
            "client_id": self.client_id,
            "account_number": self.account_number,
            "balance": self.balance
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Account:
        return Account(
            client_id=dto_dict.get("client_id"),
            account_number=dto_dict.get("account_number"),
            balance=dto_dict.get("balance")
        )