
from pydantic import BaseModel
from typing import Optional

class NewNotification(BaseModel):
    id: Optional[int] 
    title_english : str
    title_arabic: str
    content_english: str
    content_arabic: str
    customer_owner_id: Optional[int] 
    attorney_owner_id: Optional[int] 
