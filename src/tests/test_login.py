import pytest
from src.main import login

def test_login_pass():
    login_passes=login("dortiz6@unibe.org", "dev15#avatar")
    assert login_passes

def test_login_fail_wrong_user():
    login_fails=login("jmorfe@unibe.org", "dev15#avatar")
    assert not login_fails

def test_login_fail_wrong_password():
    login_fails=login("dortiz6@unibe.org", "avatar_dev")
    assert not login_fails

def test_login_fail_wrong_user_and_password():
    login_fails=login("jmorfe@unibe.org", "avatar_dev")
    assert not login_fails