from datetime import datetime
from typing import Optional
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
    
class UpdateMentorAccountModel(BaseModel):
    first_name : Optional[str] 
    last_name : Optional[str] 
    mobile_number : Optional[str] 
    email : Optional[EmailStr]
    gender : Optional[int]
    blocked : Optional[bool] 
    referal_code : Optional[str] 
    invitation_code : Optional[str]
    profile_img : Optional[str] 
    app_version : Optional[str] 
    date_of_birth : Optional[str] 
    country_id : Optional[int] 
    last_usage: datetime = datetime.now()
