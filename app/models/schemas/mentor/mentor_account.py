from typing import Optional
from pydantic import BaseModel, EmailStr
from datetime import datetime

class MentorAuth(BaseModel):
    email : str
    password: str
    
class MentorChangePassword(BaseModel):
    oldpassword : str
    newpassword: str
    
class MentorForgotPassword(BaseModel):
    email : str


class MentorFilter(BaseModel) :
    id: int
    suffixe_name: str
    first_name: str
    last_name: str
    gender: int
    profile_img: str 
    hour_rate: float
    bio: str
    working_hours: list[int]
    rate: Optional[float]
    date: str
    day: str
    hour: int
    class Config:
        orm_mode = True
    
class InstantMentor(BaseModel) :
    id: int
    suffixe_name: str
    first_name: str
    last_name: str
    rate: float
    gender: int
    profile_img: str 
    hour_rate: float              
    class Config:
        orm_mode = True
    

    
class MentorObjForListResponse(BaseModel) :
    id: int
    category_name: str
    suffixe_name: str
    first_name: str
    last_name: str
    rate: float
    hour_rate: float
    profile_img: str
    languages: list[str]
    country_name: str
    country_flag: str
    number_of_reviewr: int

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
    hour_rate: float
    total_rate: float
    gender: int
    profile_img: str
    date_of_birth: str
    experience_since: str
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
    
    
class UpdateMentorAccountInfoModel(BaseModel):
    suffixe_name: Optional[str]     
    first_name: Optional[str] 
    last_name: Optional[str] 
    speaking_language: Optional[list[str]]
    mobile_number : Optional[str] 
    email : Optional[EmailStr] 
    gender : Optional[int] 
    date_of_birth : Optional[str] 
    profile_img : Optional[str]
    id_img : Optional[str]
    country_id : Optional[int] 

class SpeakingLanguage(BaseModel):
    list: list[str]
    
    
    
class RegisterMentorAccountModel(BaseModel):
    suffixe_name: Optional[str]
    first_name: Optional[str] 
    last_name: Optional[str] 
    country_id : Optional[int] 
    gender : Optional[int] 
    date_of_birth : Optional[str] 
    mobile_number : Optional[str] 
    referal_code : Optional[str] 
    profile_img : Optional[str]
    id_img : Optional[str]
    bio : Optional[str]
    majors: Optional[list[int]]
    category_id : Optional[int]
    cv : Optional[str]
    cert1 : Optional[str]
    cert2 : Optional[str]
    cert3 : Optional[str]
    speaking_language: Optional[list[str]]
    working_hours_saturday: Optional[list[str]]
    working_hours_sunday: Optional[list[str]]
    working_hours_monday: Optional[list[str]]
    working_hours_tuesday: Optional[list[str]]
    working_hours_wednesday: Optional[list[str]]
    working_hours_thursday: Optional[list[str]]
    working_hours_friday: Optional[list[str]]
    hour_rate: Optional[float]
    email : Optional[EmailStr] 
    password: Optional[str]
    app_version: Optional[str]
    api_key: Optional[str]
    invitation_code: Optional[str]
    push_token: Optional[str]
    experience_since: Optional[str]


    


