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
        
        
class Tips(BaseModel) :
    id: int
    category_id: int
    title: str
    desc: str
    note: str
    referance: str
    image: str
    steps: int
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

class ClientHomeResponse(BaseModel) :
    main_banner: List[Banner]
    main_tips: List[Tips]
    main_event: List[Event]

    class Config:
        orm_mode = True
        
        
class MentorHomeResponse(BaseModel) :
    main_banner: List[Banner]
    main_event: List[Event]

    class Config:
        orm_mode = True
