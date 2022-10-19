from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class AccountModel(BaseModel):
    mobile_number : str
    os_type: str
    country_id: int
    device_type_name: str
    os_version: str
    app_version: str
    last_otp: Optional[str]
    api_key: Optional[str]
    
class AccountVerifyModel(BaseModel):
    mobile_number : str
    user_id: int
    os_type: str
    country_id: int
    device_type_name: str
    os_version: str
    app_version: str
    otp: str
    api_key: str
    
class UpdateAccountModel(BaseModel):
    first_name : Optional[str] 
    last_name : Optional[str] 
    mobile_number : Optional[str] 
    email : Optional[str] 
    gender : Optional[int] 
    hide_number : Optional[bool] 
    hide_email : Optional[bool] 
    blocked : Optional[bool] 
    referal_code : Optional[str] 
    profile_img : Optional[str] 
    os_type : Optional[str] 
    device_type_name : Optional[str] 
    os_version : Optional[str] 
    app_version : Optional[str] 
    date_of_birth : Optional[str] 
    country_id : Optional[int] 
    allow_notifications : Optional[bool] 
    last_usage: datetime = datetime.now()
