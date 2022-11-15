from typing import Optional
from pydantic import BaseModel

class Report(BaseModel) :
    client_owner_id: Optional[int]
    mentor_owner_id: Optional[int]
    content: str
    attachment1: Optional[str] 
    attachment2: Optional[str] 
    attachment3: Optional[str] 