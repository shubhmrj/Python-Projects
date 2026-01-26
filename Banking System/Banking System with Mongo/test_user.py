import pytest
from user_auth import signup, authenticate

def test_signup():
    user_id = signup("testuser", "testpass", "Savings")
    assert isinstance(user_id, str) and len(user_id) == 4

def test_login_success():
    user_id = signup("validuser", "validpass", "Checking")
    user_data = authenticate(user_id, "validpass")
    assert user_data is not None

def test_login_failure():
    assert authenticate("9999", "wrongpass") is None
