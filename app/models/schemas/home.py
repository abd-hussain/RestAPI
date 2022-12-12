from pydantic import BaseModel
from typing import List, Optional

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

class Story(BaseModel) :
    id: int
    assets: str
    owner: Optional[MentorOut]
    
    class Config:
        orm_mode = True
        
        
class Tips(BaseModel) :
    id: int
    title: str
    desc: str
    note: str
    referance: str
    image: str
    steps: int 
    class Config:
        orm_mode = True

class HomeResponse(BaseModel) :
    main_banner: List[Banner]
    main_story: List[Story]
    main_tips: List[Tips]
    
    class Config:
        orm_mode = True
