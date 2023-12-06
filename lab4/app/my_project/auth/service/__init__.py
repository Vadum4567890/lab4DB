from .orders.client_service import ClientService
from .orders.account_service import AccountService
from .orders.loan_service import LoanService


client_service = ClientService()
account_service = AccountService()
loan_service = LoanService()
