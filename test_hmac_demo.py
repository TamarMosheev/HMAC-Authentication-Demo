import pytest
from hmac_demo import create_hmac, is_message_authentic

def test_create_hmac_output():
    key = b'secret'
    message = b'Hello'
    mac = create_hmac(message, key)
    assert isinstance(mac, str)
    assert len(mac) == 64  # SHA-256 produces 64-character hex digest

def test_authentic_message():
    key = b'my_shared_secret'
    message = b'Test message'
    mac = create_hmac(message, key)
    assert is_message_authentic(message, mac, key) is True

def test_modified_message():
    key = b'my_shared_secret'
    message = b'Original message'
    modified_message = b'Altered message'
    mac = create_hmac(message, key)
    assert is_message_authentic(modified_message, mac, key) is False

def test_wrong_key():
    key = b'correct_key'
    wrong_key = b'incorrect_key'
    message = b'Secure data'
    mac = create_hmac(message, key)
    assert is_message_authentic(message, mac, wrong_key) is False
