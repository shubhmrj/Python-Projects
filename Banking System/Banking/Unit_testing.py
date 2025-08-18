import pytest
from Banking.Banking import BankAccount

@pytest.fixture
def bank_account():
    return BankAccount("John Doe", 1000)

def test_initial_balance(bank_account):
    assert bank_account.get_balance() == 1000

def test_deposit(bank_account):
    bank_account.deposit(500)
    assert bank_account.get_balance() == 1500

def test_withdraw_success(bank_account):
    bank_account.withdraw(300)
    assert bank_account.get_balance() == 700

def test_withdraw_insufficient_funds(bank_account):
    with pytest.raises(ValueError, match="Insufficient funds"):
        bank_account.withdraw(2000)

def test_negative_deposit(bank_account):
    with pytest.raises(ValueError, match="Deposit amount must be positive"):
        bank_account.deposit(-50)

def test_negative_withdraw(bank_account):
    with pytest.raises(ValueError, match="Withdrawal amount must be positive"):
        bank_account.withdraw(-100)
