from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr


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
    mobile_number : str
    os_type: str
    device_type_name: str
    os_version: str
    app_version: str
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[EmailStr]
    gender: Optional[int]
    hide_number: Optional[bool] = False
    referal_code: Optional[str]
    profile_img: Optional[str]
    last_usage: datetime = datetime.now()
    date_of_birth:Optional[str] 