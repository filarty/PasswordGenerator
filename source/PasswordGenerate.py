from typing import TypeVar

import random

import string

Tself = TypeVar("Tself", bound="Password")

class Password:
    def __init__(self) -> Tself:
        self.password = None
        
    def generate(self, count: int) -> str:
        """ generate

        Args:
            count (int): count symbols in password

        Returns:
            str: password in str
        """
        string_list: list[str] = (self._add_lower_case() + self._add_number_case() + self._add_symbols_case() + self._add_upper_case())
        random.shuffle(string_list)
        return "".join(string_list)
        
    def _add_upper_case(self, count: int) -> str:
        return random.sample(string.ascii_uppercase, random.randint(1, count))
    
    def _add_lower_case(self, count: int) -> str:
        return random.sample(string.ascii_lowercase, random.randint(1, count))
    
    def _add_number_case(self, count: int) -> str:
        return random.sample(string.digits, random.randint(1, count))
    
    def _add_symbols_case(self, count: int) -> str:
        return random.sample(string.punctuation, random.randint(1, count))
    
if __name__ == "__main__":
    password = Password()
    print(password.generate(8))