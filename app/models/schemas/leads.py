from typing import List, Optional
from pydantic import BaseModel


class Leads(BaseModel):
    full_name: str
    mobile_number: str
    email: str
    client_owner_id: Optional[int]
    mentor_owner_id: Optional[int]

class ListLeads(BaseModel):
    list: List[Leads]


