from typing import Optional
from pydantic import BaseModel

class Report(BaseModel) :
    customers_owner_id: Optional[int]
    attorney_owner_id: Optional[int]
    content: str
    attachment1: Optional[str] 
    attachment2: Optional[str] 
    attachment3: Optional[str] 