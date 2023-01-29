from typing import Optional
from pydantic import BaseModel

class StoryPayload(BaseModel) :
    owner_id: Optional[int]
    language: Optional[str] 
    assets: Optional[str] 
    published: Optional[bool] 