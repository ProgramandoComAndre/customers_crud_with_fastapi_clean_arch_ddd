from .customer_repository import CustomerRepository
from .dtos import RegisterNewCustomerDto
from .customer import Customer
from .value_objects import Name, Nif
from fastapi import Depends
import uuid
class CustomerService:
    def __init__(self, customer_repository: CustomerRepository = Depends()):
        self.customer_repository = customer_repository
    
    async def register_new_customer(self, customer_dto: RegisterNewCustomerDto):
        customer = Customer(Name(customer_dto.first_name, customer_dto.last_name), Nif(customer_dto.nif), uuid.uuid4())
        registered_customer = await self.customer_repository.insert_customer(customer)
        if registered_customer is None:
            raise Exception("Customer already exists")
        return registered_customer
    
    def __call__(self):
        return self
    async def get_all_customers(self, limit=10):
        return await self.customer_repository.find_all(limit)    
        