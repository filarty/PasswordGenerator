from unittest import TestCase

from source.PasswordGenerate import Password

import string

password = Password()

class PasswordTest(TestCase):
    def test_upper_case(self):
        password_string = "".join(password._add_upper_case())
        self.assertTrue(password_string.isupper())
    
    def test_lower_case(self):
        password_string = "".join(password._add_lower_case())
        self.assertTrue(password_string.islower())
    
    def test_numbers_case(self):
        password_string = "".join(password._add_number_case())
        self.assertTrue(password_string.isdigit())
        
    def test_symbols_case(self):
        password_string = "".join(password._add_symbols_case())
        self.assertTrue(all((password_string.find(i) for i in string.punctuation)))
    