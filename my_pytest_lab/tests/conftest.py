import pytest

from src.main import BankAccount


@pytest.fixture(scope="function")
def bank_account():
    account = BankAccount(owner="Іван Петренко", balance=1000.0)

    yield account

    account.owner = ""
    account.balance = 0.0
