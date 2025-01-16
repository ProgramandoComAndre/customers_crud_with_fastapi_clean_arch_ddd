import sys
import os
import unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from features.customers.customer_service import CustomerService
from features.customers.in_memory_customer_repository import InMemoryCustomerRepository
from features.customers.dtos.register_new_customer_dto import RegisterNewCustomerDto
from features.customers import Customer
class NifTest(unittest.IsolatedAsyncioTestCase):
    async def test_should_register_customer(self):
        dto = RegisterNewCustomerDto(first_name="Sonia", last_name="Teixeira", nif="275466205")
        repository = InMemoryCustomerRepository()
        service = CustomerService(repository)
        customer = await service.register_new_customer(dto)
        self.assertIsInstance(customer, Customer)

    async def test_should_not_register_customer_if_nif_already_exists(self):
        dto = RegisterNewCustomerDto(first_name="Sonia", last_name="Teixeira", nif="275466205")
        repository = InMemoryCustomerRepository()
        service = CustomerService(repository)
        customer = await service.register_new_customer(dto)
        with self.assertRaises(Exception):
            await service.register_new_customer(dto)
if __name__=="__main__":
    unittest.main()