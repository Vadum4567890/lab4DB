from __future__ import annotations
from typing import Dict, Any
from .... import db
from ..i_dto import IDto


class Loan(db.Model, IDto):
    __tablename__ = "loans"

    loan_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    client_id = db.Column(db.Integer, db.ForeignKey('clients.client_id'))
    loan_amount = db.Column(db.DECIMAL(10, 2))
    interest_rate = db.Column(db.DECIMAL(5, 2))
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)

    def __repr__(self) -> str:
        return f"Loan({self.loan_id}, {self.client_id}, {self.loan_amount}, {self.interest_rate}, '{self.start_date}', '{self.end_date}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "loan_id": self.loan_id,
            "client_id": self.client_id,
            "loan_amount": self.loan_amount,
            "interest_rate": self.interest_rate,
            "start_date": self.start_date,
            "end_date": self.end_date
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Loan:
        return Loan(
            client_id=dto_dict.get("client_id"),
            loan_amount=dto_dict.get("loan_amount"),
            interest_rate=dto_dict.get("interest_rate"),
            start_date=dto_dict.get("start_date"),
            end_date=dto_dict.get("end_date")
        )