
import random

import string

import math_random as mr

class Password:
    def __init__(self) -> None:
        self.password = None
        
    def generate(self, count: int) -> str:
        """ generate

        Args:
            count (int): count symbols in password

        Returns:
            str: password in str
        """
        lower, upper, symb, number = mr.get_random_distribution_numbers(count)
        string_list: list[str] = (self._add_lower_case(lower) + self._add_number_case(upper) + self._add_symbols_case(symb) 
                                + self._add_upper_case(number))
        random.shuffle(string_list)
        return "".join(string_list)
        
    def _add_upper_case(self, count: int) -> list[str]:
        return random.sample(string.ascii_uppercase, count)
    
    def _add_lower_case(self, count: int) -> list[str]:
        return random.sample(string.ascii_lowercase, count)
    
    def _add_number_case(self, count: int) -> list[str]:
        return random.sample(string.digits, count)
    
    def _add_symbols_case(self, count: int) -> list[str]:
        return random.sample(string.punctuation, count)
    
if __name__ == "__main__":
    password = Password()
    print(password.generate(8))