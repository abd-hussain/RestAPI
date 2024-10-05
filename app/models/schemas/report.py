from typing import Optional
from pydantic import BaseModel

class Report(BaseModel) :
    id: int
    api_key: str
    content: str
    attachment1: Optional[str] 
    attachment2: Optional[str] 
    attachment3: Optional[str] 