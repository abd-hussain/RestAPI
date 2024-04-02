from typing import Optional
from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import List
from app.models.database.attorney.db_attorney_user import FreeCallTypes

class AuthData(BaseModel):
    email : str
    password: str
    userType: str
    
class ChangePassword(BaseModel):
    oldpassword : str
    newpassword: str
    userType: str
    
class ForgotPassword(BaseModel):
    email : str
    userType: str

class AttorneyFilter(BaseModel) :
    id: int
    suffixe_name: str
    first_name: str
    last_name: str
    gender: int
    profile_img: str 
    hour_rate: float
    working_hours: List[int] = []
    rate: Optional[float]
    date: str
    currency: str
    currency_code: str
    country_code: str
    languages: list[str]
    country_name: str
    country_flag: str
    number_of_reviewers: int
    day: str
    hour: int = 0
    class Config:
        orm_mode = True
    
class AttorneyObjForListResponse(BaseModel) :
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
    currency: str
    number_of_reviewers: int
    class Config:
        orm_mode = True
        
class ReviewsResponse(BaseModel) :
    id: int
    customer_first_name: str
    customer_last_name: str
    customer_profile_img: str
    attorney_id: int
    stars: float
    comments: str
    attorney_response:Optional[str]
    flag_image: str
    created_at: datetime                  
    class Config:
        orm_mode = True
     
class AttorneyDetailsResponse(BaseModel) :
    id: int
    suffixe_name: str    
    first_name: str
    last_name: str
    bio: str
    speaking_language: list[str]
    hour_rate: float
    free_call: Optional[FreeCallTypes]
    currency: str
    currency_code: str
    country_code: str
    total_rate: float
    gender: int
    profile_img: str
    date_of_birth: str
    experience_since: str
    category_name: str
    category_id :int
    country: str
    country_flag: str
    working_hours_saturday: list[int]
    working_hours_sunday: list[int]
    working_hours_monday: list[int]
    working_hours_tuesday: list[int]
    working_hours_wednesday: list[int]
    working_hours_thursday: list[int]
    working_hours_friday: list[int]
    reviews: list[ReviewsResponse]
    
class RegisterAttorneyAccountModel(BaseModel):
    id: Optional[int]
    suffixe_name: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    country_id : Optional[str]
    gender : Optional[str]
    date_of_birth : Optional[str]
    bio : Optional[str]
    category_id : Optional[int]
    speaking_language: Optional[list[str]]
    mobile_number : Optional[str]
    working_hours_saturday: Optional[list[int]]
    working_hours_sunday: Optional[list[int]]
    working_hours_monday: Optional[list[int]]
    working_hours_tuesday: Optional[list[int]]
    working_hours_wednesday: Optional[list[int]]
    working_hours_thursday: Optional[list[int]]
    working_hours_friday: Optional[list[int]]
    hour_rate: Optional[str] 
    iban: Optional[str] 
    email : Optional[EmailStr] 
    password: Optional[str] 
    app_version: Optional[str] 
    api_key: Optional[str] 
    invitation_code: Optional[str] 
    push_token: Optional[str] 
    experience_since: Optional[str] 
    profile_img : Optional[str] 
    id_img : Optional[str] 
    cv : Optional[str] 
    cert1 : Optional[str] = ""
    cert2 : Optional[str] = ""
    cert3 : Optional[str] = "" 
    
    
class RegisterCustomerAccountModel(BaseModel):
    id: Optional[int]
    first_name: Optional[str]
    last_name: Optional[str]
    mobile_number : Optional[str]
    email : Optional[EmailStr] 
    password: Optional[str] 
    gender : Optional[str]
    allow_notifications: Optional[bool] 
    invitation_code: Optional[str]
    profile_img : Optional[str]
    app_version: Optional[str]
    date_of_birth : Optional[str]
    api_key: Optional[str] 
    push_token: Optional[str] 
    country_id : Optional[str]


