from pydantic import BaseModel
from app.utils.generate import generateRequestId
from datetime import datetime
from pydantic.schema import Optional

from typing import Any

def generalResponse(message: str, data : Any):
    return { "data": data, "message" : message}


class Main(BaseModel):
    class Config:
        orm_mode = True        
        
        
#################################################################

class _AccountResponse(Main):
    mobile_number : str
    os_type: str
    device_type_name: str
    os_version: str
    app_version: str
    first_name: str
    last_name: str
    email: str
    gender: int
    hide_number: bool
    referal_code: str
    profile_img: str
    last_usage: datetime
    date_of_birth:str
class AccountResponse(Main):
    data : _AccountResponse
    message: str = "aboud masoud"
    request_id: str = generateRequestId()
    

#################################################################

class _LoginResponse(Main):
    id: int
    api_key: str
    blocked: bool
    first_name: Optional[str]
    last_name: Optional[str]

class LoginResponse(Main):
    data : _LoginResponse
    message: str = "aboud masoud"
    request_id: str = generateRequestId()
        
#################################################################
class _LoginDebugResponse(Main):
    id: int
    api_key: str
    blocked: bool
    first_name: Optional[str]
    last_name: Optional[str]
    last_otp: str

class LoginDebugResponse(Main):
    data : _LoginDebugResponse
    message: str = "aboud masoud"
    request_id: str = generateRequestId()
    
#################################################################

class _Reviews(Main):
    stars: int
    content:str
    
class Reviews(Main):
    data : list[_Reviews]
    message: str = "aboud masoud"
    request_id: str = generateRequestId()
    
#################################################################