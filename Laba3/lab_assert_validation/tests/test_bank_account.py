import pytest

from src.bank_account import BankAccount


def test_account_starts_with_zero_balance():
    assert BankAccount().get_balance() == 0


def test_account_uses_initial_balance():
    assert BankAccount(250).get_balance() == 250


def test_negative_initial_balance_raises_error():
    with pytest.raises(ValueError, match="Initial balance cannot be negative"):
        BankAccount(-1)


def test_deposit_adds_money():
    account = BankAccount()
    account.deposit(100)

    assert account.get_balance() == 100


@pytest.mark.parametrize("amount", [0, -10])
def test_deposit_rejects_non_positive_amount(amount):
    with pytest.raises(ValueError, match="Amount must be positive"):
        BankAccount().deposit(amount)


def test_withdraw_subtracts_money():
    account = BankAccount(250)
    account.withdraw(100)

    assert account.get_balance() == 150


@pytest.mark.parametrize("amount", [0, -10])
def test_withdraw_rejects_non_positive_amount(amount):
    with pytest.raises(ValueError, match="Amount must be positive"):
        BankAccount(250).withdraw(amount)


def test_withdraw_rejects_insufficient_funds():
    with pytest.raises(ValueError, match="Insufficient funds"):
        BankAccount(100).withdraw(101)
