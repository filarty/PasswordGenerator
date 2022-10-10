from unittest import TestCase

from source.PasswordGenerate import Password

password = Password()

class PasswordTest(TestCase):
    def test_upper_case(self):
        password_string = "".join(password._add_upper_case())
        self.assertTrue(password_string.isupper())
        