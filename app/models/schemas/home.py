from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

from app.models.database.db_event import EventState

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
        
class Banner(BaseModel) :
    image: str
    action_type: Optional[str]
    
    class Config:
        orm_mode = True
        
        
class Event(BaseModel) :
    id: int
    title: str
    image: str
    description: str
    joining_clients: int
    max_number_of_attendance: int
    date_from: datetime
    date_to: datetime
    price: float
    state: EventState

    class Config:
        orm_mode = True

class HomeResponse(BaseModel) :
    main_banner: List[Banner]
    main_event: List[Event]

    class Config:
        orm_mode = True