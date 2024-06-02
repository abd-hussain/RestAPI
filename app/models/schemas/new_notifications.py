from typing import Optional
from pydantic import BaseModel

class NewNotification(BaseModel):
    id: Optional[int]
    title_english : str
    title_arabic: str
    content_english: str
    content_arabic: str
    customers_owner_id: int = None
    attorney_owner_id: int = None
