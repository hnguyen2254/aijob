import pytest
from app import UserAuth, createUser, loginUser, encryptPassword

def test_create_user():
    user_data = {
        "username": "testuser",
        "password": "testpassword",
        "email": "test@example.com"
    }
    result = createUser(user_data)
    assert result is True

def test_login_user():
    credentials = {
        "username": "testuser",
        "password": "testpassword"
    }
    result = loginUser(credentials)
    assert result is True

def test_encrypt_password():
    password = "testpassword"
    encrypted_password = encryptPassword(password)
    assert encrypted_password != password
