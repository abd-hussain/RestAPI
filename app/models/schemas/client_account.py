from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr

class ClientAccountModel(BaseModel):
    mobile_number : str
    country_id: int
    os_type: str
    device_type_name: str
    os_version: str
    app_version: str
    last_otp: Optional[str]
    api_key: Optional[str]
    
class ClientAccountVerifyModel(BaseModel):
    mobile_number : str
    user_id: int
    otp: str
    api_key: str
    
class UpdateClientAccountModel(BaseModel):
    first_name : Optional[str] 
    last_name : Optional[str] 
    mobile_number : Optional[str] 
    email : Optional[EmailStr] 
    gender : Optional[int] 
    blocked : Optional[bool] 
    invitation_code : Optional[str]
    profile_img : Optional[str]
    os_type : Optional[str]
    device_type_name : Optional[str]
    os_version : Optional[str]
    app_version : Optional[str]
    date_of_birth : Optional[str] 
    country_id : Optional[int] 
    last_usage: datetime = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
