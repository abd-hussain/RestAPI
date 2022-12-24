from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class MentorAccountModel(BaseModel):
    mobile_number : str
    country_id: int
    app_version: str
    last_otp: Optional[str]
    api_key: Optional[str]
    
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
    reviews: list[ReviewsResponse]

        
