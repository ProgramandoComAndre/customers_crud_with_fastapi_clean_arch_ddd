from fastapi import FastAPI, Path, HTTPException
from enum import Enum
from typing import Dict, List, Annotated
from random import randint
from pydantic import BaseModel
from json import JSONEncoder


class CustomerType(str, Enum):
    regular = "regular"
    premium = "premium"

class CreateCustomerRequest(BaseModel):
    name: str
    customer_type: CustomerType


app = FastAPI()



fake_customers_bd = [
    {"name": "Andre", "customer_id": 1, "customer_type": CustomerType.regular.capitalize()},
    {"name": "Rui", "customer_id": 2, "customer_type": CustomerType.premium.capitalize()},
    {"name": "Catarina", "customer_id": 3, "customer_type": CustomerType.regular.capitalize()},
    {"name": "Andre", "customer_id": 4, "customer_type": CustomerType.regular.capitalize()},
    {"name": "Rui", "customer_id": 5,"customer_type": CustomerType.premium.capitalize()},
    {"name": "Catarina", "customer_id": 6,"customer_type": CustomerType.regular.capitalize()},
    {"name": "Andre", "customer_id": 7,"customer_type": CustomerType.regular.capitalize()},
    {"name": "Rui", "customer_id": 8,"customer_type": CustomerType.premium.capitalize()},
    {"name": "Catarina", "customer_id": 9,"customer_type": CustomerType.regular.capitalize()},
    {"name": "Andre", "customer_id": 10,"customer_type": CustomerType.regular.capitalize()},
    {"name": "Rui", "customer_id": 11,"customer_type": CustomerType.premium.capitalize()},
    {"name": "Catarina", "customer_id": 12,"customer_type": CustomerType.regular.capitalize()}
]

@app.get("/")
async def root() -> Dict[str,str]:
    return {"message": "Hello World"}

@app.post("/customers")
async def create_customer(create_customer_request: CreateCustomerRequest):
     new_customer = {"name": create_customer_request.name, "customer_id": randint(13,1000), "customer_type": create_customer_request.customer_type}
     fake_customers_bd.append(new_customer)
     return new_customer
@app.get("/customers")
async def get_customers(limit:int=10):
    return fake_customers_bd[:limit]

@app.get("/customers/{customer_id}")
async def get_customer(customer_id:Annotated[int, Path(description="Id of customer")]):
    for customer in fake_customers_bd:
        if customer["customer_id"] == customer_id:
            return customer
        
    json_encoder = JSONEncoder()
    raise HTTPException(404, json_encoder.encode("Not found"))

@app.get("/customers/{customer_id}/customer_type")
async def get_customer_type(customer_id:int)->Dict[str,str]:
    return {"customer_type": CustomerType.regular.capitalize()}



@app.get("/customers_types/{customer_type}")
async def get_plan_details(customer_type: CustomerType) -> Dict[str, str]:
    if(customer_type is CustomerType.regular):
        return {"customer_type": customer_type, "description": "Access to free courses"}
    else:
        return {"customer_type": customer_type, "description": "Access to paid courses and all free courses"}

