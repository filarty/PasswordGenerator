import asyncio

from abc import ABC, abstractmethod

from PasswordGenerate import Password


class BaseService(ABC):
    _name_service: str
        
    @property
    def name_service(self):
        return self.name_service
    
    @abstractmethod
    def get_value(self):
        ...
    
class PasswordGeneratorService(BaseService):
    """PasswordGenerator

    Args:
        _name_service (str): name of service
        count_symbols (int): counts number for password generate
    """
    _name_service: str = "Password Generator v1.0"
    
    def __init__(self, count_symbols: int) -> None:
        self.count_symbols = count_symbols
        self.password = Password() 
    
    async def get_value(self):
        result = await asyncio.get_event_loop().run_in_executor(None, self.password.generate, self.count_symbols)
        return result