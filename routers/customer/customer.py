from fastapi import APIRouter, Depends
from features.customers.in_memory_customer_repository import InMemoryCustomerRepository
from typing import Annotated, List
from pydantic import BaseModel
from features.customers.customer_service import CustomerService
from features.customers.dtos.register_new_customer_dto import RegisterNewCustomerDto
CustomerRouter = APIRouter(prefix="/v1/customers", tags=["customer"])

service = CustomerService(InMemoryCustomerRepository())

class CreateCustomerResponse(BaseModel):
    name: str
    nif: str
    id: str


@CustomerRouter.post("/", response_model= CreateCustomerResponse)
async def create_customer(customerDto: RegisterNewCustomerDto, service: Annotated[CustomerService, Depends(service)]):
     customer = await service.register_new_customer(customerDto)
     res = CreateCustomerResponse(name=str(customer.get_name()), nif=str(customer.get_nif()), id=str(customer.get_id()))
     return res

@CustomerRouter.get("/", response_model= List[CreateCustomerResponse])
async def get_customers(service: Annotated[CustomerService, Depends(service)],limit:int=10):
    customers = await service.get_all_customers(limit)
    customers_mapped = list(map(lambda customer: CreateCustomerResponse(name=str(customer.get_name()), nif=str(customer.get_nif()), id=str(customer.get_id())),customers))
    return customers_mapped
     