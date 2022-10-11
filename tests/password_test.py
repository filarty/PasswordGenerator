from unittest import TestCase

from source.PasswordGenerate import Password

from source.math import get_random_distribution_numbers

import string

password = Password()

class PasswordTest(TestCase):
    def test_upper_case(self):
        password_string = "".join(password._add_upper_case(4))
        self.assertTrue(password_string.isupper())
    
    def test_lower_case(self):
        password_string = "".join(password._add_lower_case(4))
        self.assertTrue(password_string.islower())
    
    def test_numbers_case(self):
        password_string = "".join(password._add_number_case(4))
        self.assertTrue(password_string.isdigit())
        
    def test_symbols_case(self):
        password_string = "".join(password._add_symbols_case(4))
        self.assertTrue(all((string.punctuation.find(i) for i in password_string)))

class MathFuncTest(TestCase):
    def test_symbol_summ(self):
        self.assertEqual(6, sum(get_random_distribution_numbers(6)))
        self.assertEqual(10, sum(get_random_distribution_numbers(10)))
        self.assertEqual(15, sum(get_random_distribution_numbers(15)))
        self.assertEqual(23, sum(get_random_distribution_numbers(23)))
        self.assertEqual(55, sum(get_random_distribution_numbers(55)))