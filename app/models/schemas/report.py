from typing import Optional
from pydantic import BaseModel

class Report(BaseModel) :
    content: Optional[str]
    attachment1: Optional[str] 
    attachment2: Optional[str] 
    attachment3: Optional[str] 