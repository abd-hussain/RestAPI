from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class MentorAccountModel(BaseModel):
    mobile_number : str
    country_id: int
    app_version: str
    last_otp: Optional[str]
    api_key: Optional[str]
    
class InstantMentor(BaseModel) :
    id: int
    suffixe_name: str
    first_name: str
    last_name: str
    rate: float
    profile_img: str 
    hour_rate_by_JD: float              
    class Config:
        orm_mode = True
    
class MentorAccountVerifyModel(BaseModel):
    mobile_number : str
    user_id: int
    country_id: int
    app_version: str
    otp: str
    api_key: str
    
class MentorObjForListResponse(BaseModel) :
    id: int
    category_name: str
    suffixe_name: str
    first_name: str
    last_name: str
    rate: float
    hour_rate_by_JD: float
    profile_img: str

    class Config:
        orm_mode = True
        
        
class ReviewsResponse(BaseModel) :
    id: int
    client_first_name: str
    client_last_name: str
    client_profile_img: str
    mentor_id: int
    stars: float
    comments: str
    created_at: datetime                  
    class Config:
        orm_mode = True
        
class MentorDetailsResponse(BaseModel) :
    suffixe_name: str    
    first_name: str
    last_name: str
    bio: str
    speaking_language: list[str]
    hour_rate_by_JD: float
    total_rate: float
    gender: int
    profile_img: str
    date_of_birth: str
    category_name: str
    country: str
    country_flag: str
    major: list[str]
    working_hours_saturday: list[int]
    working_hours_sunday: list[int]
    working_hours_monday: list[int]
    working_hours_tuesday: list[int]
    working_hours_wednesday: list[int]
    working_hours_thursday: list[int]
    working_hours_friday: list[int]
    reviews: list[ReviewsResponse]
