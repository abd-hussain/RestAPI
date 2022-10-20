from typing import List
from pydantic import BaseModel


class Leads(BaseModel):
    full_name: str
    mobile_number: str
    email: str
    owner_id: int
    
class ListLeads(BaseModel):
    list: List[Leads]


