from pydantic import BaseModel,StringConstraints
from typing import Annotated

class RegisterNewCustomerDto(BaseModel):
    first_name: Annotated[str, StringConstraints(min_length=1)]
    last_name: str    
    nif: Annotated[str, StringConstraints(min_length=9, max_length=9)]