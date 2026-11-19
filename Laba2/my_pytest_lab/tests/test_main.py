from contextlib import nullcontext as does_not_raise

import pytest

from src.main import BankAccount


@pytest.mark.smoke
def test_create_account_positive():
    account = BankAccount("Олена Коваль", 250.5)

    assert account.owner == "Олена Коваль"
    assert account.balance == pytest.approx(250.5)


@pytest.mark.parametrize(
    "owner, balance, error_type, message",
    [
        (123, 0, TypeError, "Owner must be a string"),
        ("   ", 0, ValueError, "Owner name cannot be empty"),
        ("Іван", "100", TypeError, "Balance must be a number"),
        ("Іван", -1, ValueError, "Initial balance cannot be negative"),
    ],
)
def test_create_account_errors(owner, balance, error_type, message):
    with pytest.raises(error_type, match=message):
        BankAccount(owner, balance)


@pytest.mark.parametrize(
    "amount, expected_balance",
    [
        (100.0, 1100.0),
        (500.0, 1500.0),
        (0.25, 1000.25),
    ],
)
def test_deposit_positive(bank_account, amount, expected_balance):
    bank_account.deposit(amount)

    assert bank_account.get_balance() == pytest.approx(expected_balance)


@pytest.mark.parametrize(
    "amount, error_type, message",
    [
        ("100", TypeError, "Deposit amount must be a number"),
        (0, ValueError, "Deposit amount must be greater than zero"),
        (-50, ValueError, "Deposit amount must be greater than zero"),
    ],
)
def test_deposit_errors(bank_account, amount, error_type, message):
    with pytest.raises(error_type, match=message):
        bank_account.deposit(amount)


@pytest.mark.parametrize(
    "amount, expected_balance, expectation",
    [
        (200.0, 800.0, does_not_raise()),
        (1000.0, 0.0, does_not_raise()),
        ("200", None, pytest.raises(TypeError, match="Withdraw amount must be a number")),
        (0, None, pytest.raises(ValueError, match="Withdraw amount must be greater than zero")),
        (-1, None, pytest.raises(ValueError, match="Withdraw amount must be greater than zero")),
        (1000.01, None, pytest.raises(ValueError, match="Insufficient funds")),
    ],
)
def test_withdraw_scenarios(bank_account, amount, expected_balance, expectation):
    with expectation:
        bank_account.withdraw(amount)

    if expected_balance is not None:
        assert bank_account.get_balance() == pytest.approx(expected_balance)


@pytest.mark.parametrize(
    "percent, expected_balance, expectation",
    [
        (10.0, 1100.0, does_not_raise()),
        (0.0, 1000.0, does_not_raise()),
        ("5", None, pytest.raises(TypeError, match="Interest percent must be a number")),
        (-1, None, pytest.raises(ValueError, match="Interest percent cannot be negative")),
    ],
)
def test_add_interest_scenarios(bank_account, percent, expected_balance, expectation):
    with expectation:
        bank_account.add_interest(percent)

    if expected_balance is not None:
        assert bank_account.get_balance() == pytest.approx(expected_balance)


def test_get_balance_and_fixture_teardown(bank_account):
    assert bank_account.owner == "Іван Петренко"
    assert bank_account.get_balance() == pytest.approx(1000.0)


FEATURE_ENABLED = False


@pytest.mark.skipif(
    not FEATURE_ENABLED,
    reason="Розширена аналітика балансу ще не реалізована",
)
def test_advanced_balance_report():
    assert False
