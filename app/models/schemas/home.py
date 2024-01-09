from pydantic import BaseModel
from typing import Optional

class MentorOut(BaseModel):
    id: int
    first_name: Optional[str]
    last_name : Optional[str] 
    gender : Optional[int]
    blocked : Optional[bool] 
    profile_img : Optional[str]
    country_id : Optional[int] 
    
    class Config:
        orm_mode = True
        