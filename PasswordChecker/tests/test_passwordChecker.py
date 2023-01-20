import unittest
import pytest

from PasswordChecker.main import InvalidPasswordError, NotLongEnoughError, passwordChecker


class TestPasswordChecker(unittest.TestCase):
    def test_TooShort(self):
        with pytest.raises(NotLongEnoughError):
            passwordChecker("Short")

    def test_InvalidPassword(self):
        with pytest.raises(InvalidPasswordError):
            passwordChecker("This is not a valid password.")

    def test_GoodPassword(self):
        assert passwordChecker("This.is.a.valid.password") == "This.is.a.valid.password"
