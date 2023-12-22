
from pydantic import BaseModel
from typing import Optional

class NewNotification(BaseModel):
    id: Optional[int] 
    title_english : str
    title_arabic: str
    content_english: str
    content_arabic: str
    readed: bool = False
    client_owner_id: Optional[int] 
    mentor_owner_id: Optional[int] 
