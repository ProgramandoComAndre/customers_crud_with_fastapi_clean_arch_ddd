from .customer_repository import CustomerRepository
from .customer import Customer
class InMemoryCustomerRepository(CustomerRepository):
    def __init__(self):
        self.customers = []
    async def insert_customer(self, customer:Customer):
        existing_customer = list(filter(lambda value: customer.get_nif() == value.get_nif(),self.customers))
        if len(existing_customer) != 0:
            raise KeyError("Customer with that nif already exists")
        self.customers.append(customer)
        return customer
    async def find_by_id(self, id):
        existing_customer = list(filter(lambda value: value.get_id() == id,self.customers))
        if len(existing_customer) > 0:
            return existing_customer[0]
        return None
    
    async def find_by_nif(self, nif):
        existing_customer = list(filter(lambda value: value.get_nif() == nif,self.customers))
        if len(existing_customer) > 0:
            return existing_customer[0]
        return None

    async def find_all(self, limit=10):
        return self.customers[:limit] 
        
