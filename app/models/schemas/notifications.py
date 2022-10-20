from typing import List
from pydantic import BaseModel
    
class Notifications(BaseModel):
    list: List[int]
    user_id : int


