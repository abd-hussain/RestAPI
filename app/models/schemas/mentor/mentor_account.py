from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, EmailStr

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
    class_min: int
    hour_rate_by_JD: float
    rate: float
    gender: int
    blocked: bool
    profile_img: str
    date_of_birth: str
    country_id: int

    class Config:
        orm_mode = True
class MentorListResponse(BaseModel) :
    list: List[MentorObjForListResponse]

    class Config:
        orm_mode = True
        
        
class MentorDetailsResponse(BaseModel) :
    suffixe_name: str    
    first_name: str
    last_name: str
    bio: str
    speaking_language: list[str]
    class_min: int
    hour_rate_by_JD: float
    rate: float
    gender: int
    profile_img: str
    date_of_birth: str
    category_name: str
    country: str
    country_flag: str
    major: list[str]

        
