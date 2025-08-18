import pytest
from decimal import Decimal

# Assuming these are the classes we're testing
# You'll need to replace these imports with your actual implementation
class BankAccount:
    def __init__(self, account_id, owner_name, balance=0.0):
        self.account_id = account_id
        self.owner_name = owner_name
        self.balance = Decimal(str(balance))
        
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += Decimal(str(amount))
        return self.balance
        
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= Decimal(str(amount))
        return self.balance
        
    def get_balance(self):
        return self.balance

class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}
        
    def create_account(self, account_id, owner_name, initial_balance=0.0):
        if account_id in self.accounts:
            raise ValueError(f"Account with ID {account_id} already exists")
        account = BankAccount(account_id, owner_name, initial_balance)
        self.accounts[account_id] = account
        return account
        
    def get_account(self, account_id):
        if account_id not in self.accounts:
            raise ValueError(f"Account with ID {account_id} does not exist")
        return self.accounts[account_id]
        
    def transfer(self, from_account_id, to_account_id, amount):
        if amount <= 0:
            raise ValueError("Transfer amount must be positive")
            
        from_account = self.get_account(from_account_id)
        to_account = self.get_account(to_account_id)
        
        from_account.withdraw(amount)
        to_account.deposit(amount)
        
        return from_account.get_balance(), to_account.get_balance()


# Tests for the BankAccount class
class TestBankAccount:
    def test_init(self):
        account = BankAccount("123", "John Doe", 100.0)
        assert account.account_id == "123"
        assert account.owner_name == "John Doe"
        assert account.balance == Decimal("100.0")
        
    def test_deposit(self):
        account = BankAccount("123", "John Doe", 100.0)
        new_balance = account.deposit(50.0)
        assert new_balance == Decimal("150.0")
        assert account.balance == Decimal("150.0")
        
    def test_deposit_negative_amount(self):
        account = BankAccount("123", "John Doe", 100.0)
        with pytest.raises(ValueError, match="Deposit amount must be positive"):
            account.deposit(-50.0)
            
    def test_withdraw(self):
        account = BankAccount("123", "John Doe", 100.0)
        new_balance = account.withdraw(50.0)
        assert new_balance == Decimal("50.0")
        assert account.balance == Decimal("50.0")
        
    def test_withdraw_negative_amount(self):
        account = BankAccount("123", "John Doe", 100.0)
        with pytest.raises(ValueError, match="Withdrawal amount must be positive"):
            account.withdraw(-50.0)
            
    def test_withdraw_insufficient_funds(self):
        account = BankAccount("123", "John Doe", 100.0)
        with pytest.raises(ValueError, match="Insufficient funds"):
            account.withdraw(150.0)
            
    def test_get_balance(self):
        account = BankAccount("123", "John Doe", 100.0)
        assert account.get_balance() == Decimal("100.0")
        

# Tests for the Bank class
class TestBank:
    def test_init(self):
        bank = Bank("Test Bank")
        assert bank.name == "Test Bank"
        assert bank.accounts == {}
        
    def test_create_account(self):
        bank = Bank("Test Bank")
        account = bank.create_account("123", "John Doe", 100.0)
        assert account.account_id == "123"
        assert account.owner_name == "John Doe"
        assert account.balance == Decimal("100.0")
        assert "123" in bank.accounts
        
    def test_create_duplicate_account(self):
        bank = Bank("Test Bank")
        bank.create_account("123", "John Doe", 100.0)
        with pytest.raises(ValueError, match="Account with ID 123 already exists"):
            bank.create_account("123", "Jane Smith", 200.0)
            
    def test_get_account(self):
        bank = Bank("Test Bank")
        bank.create_account("123", "John Doe", 100.0)
        account = bank.get_account("123")
        assert account.account_id == "123"
        assert account.owner_name == "John Doe"
        assert account.balance == Decimal("100.0")
        
    def test_get_nonexistent_account(self):
        bank = Bank("Test Bank")
        with pytest.raises(ValueError, match="Account with ID 123 does not exist"):
            bank.get_account("123")
            
    def test_transfer(self):
        bank = Bank("Test Bank")
        bank.create_account("123", "John Doe", 100.0)
        bank.create_account("456", "Jane Smith", 50.0)
        from_balance, to_balance = bank.transfer("123", "456", 30.0)
        assert from_balance == Decimal("70.0")
        assert to_balance == Decimal("80.0")
        assert bank.get_account("123").balance == Decimal("70.0")
        assert bank.get_account("456").balance == Decimal("80.0")
        
    def test_transfer_negative_amount(self):
        bank = Bank("Test Bank")
        bank.create_account("123", "John Doe", 100.0)
        bank.create_account("456", "Jane Smith", 50.0)
        with pytest.raises(ValueError, match="Transfer amount must be positive"):
            bank.transfer("123", "456", -30.0)
            
    def test_transfer_insufficient_funds(self):
        bank = Bank("Test Bank")
        bank.create_account("123", "John Doe", 100.0)
        bank.create_account("456", "Jane Smith", 50.0)
        with pytest.raises(ValueError, match="Insufficient funds"):
            bank.transfer("123", "456", 150.0)
            
    def test_transfer_nonexistent_account(self):
        bank = Bank("Test Bank")
        bank.create_account("123", "John Doe", 100.0)
        with pytest.raises(ValueError, match="Account with ID 456 does not exist"):
            bank.transfer("123", "456", 50.0)


# Using pytest fixtures for more complex scenarios
@pytest.fixture
def populated_bank():
    bank = Bank("Test Bank")
    bank.create_account("123", "John Doe", 1000.0)
    bank.create_account("456", "Jane Smith", 2000.0)
    bank.create_account("789", "Bob Johnson", 500.0)
    return bank

class TestBankOperations:
    def test_multiple_transfers(self, populated_bank):
        bank = populated_bank
        # Transfer from account 123 to 456
        bank.transfer("123", "456", 200.0)
        # Transfer from account 456 to 789
        bank.transfer("456", "789", 300.0)
        
        assert bank.get_account("123").balance == Decimal("800.0")
        assert bank.get_account("456").balance == Decimal("1900.0")
        assert bank.get_account("789").balance == Decimal("800.0")
        
    def test_deposit_and_withdraw_sequence(self, populated_bank):
        bank = populated_bank
        account = bank.get_account("123")
        
        account.deposit(500.0)
        assert account.balance == Decimal("1500.0")
        
        account.withdraw(300.0)
        assert account.balance == Decimal("1200.0")
        
        account.deposit(100.0)
        account.withdraw(50.0)
        assert account.balance == Decimal("1250.0")