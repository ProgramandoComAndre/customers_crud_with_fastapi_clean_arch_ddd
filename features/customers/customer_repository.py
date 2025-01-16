from abc import ABC, abstractmethod
from .customer import Customer
from .value_objects import Nif
class CustomerRepository(ABC):
    @abstractmethod
    async def insert_customer(self, customer: Customer): pass

    @abstractmethod
    async def find_by_id(self, id: int): pass

    @abstractmethod
    async def find_by_nif(self, nif: Nif): pass
    @abstractmethod
    async def find_all(self, limit=10): pass
