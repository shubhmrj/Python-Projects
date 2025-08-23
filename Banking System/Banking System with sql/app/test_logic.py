import pytest
from banking_app.app import db, logic

@pytest.fixture(autouse=True, scope="module")
def setup_db():
    db.set_test_mode(True)
    db.init_db()

def test_register_user():
    result = logic.register_user("Test User", "1234567890", "testuser", "pass123")
    assert result is True

def test_duplicate_user_fails():
    logic.register_user("Another", "9999999999", "dupeuser", "pass")
    result = logic.register_user("Again", "8888888888", "dupeuser", "pass")
    assert result is False

def test_login_success():
    logic.register_user("Login Guy", "1111111111", "logmein", "secret")
    assert logic.login_user("logmein", "secret") is True

def test_login_fail():
    assert logic.login_user("unknown", "nope") is False

def test_deposit_and_withdraw():
    logic.register_user("Money Man", "7777777777", "money", "cash")
    assert logic.deposit("money", 100.0)
    assert logic.withdraw("money", 40.0)
    assert logic.get_balance("money") == 60.0

def test_overdraw_fails():
    logic.register_user("Poor Guy", "5555555555", "broke", "zero")
    assert logic.withdraw("broke", 50.0) is False
