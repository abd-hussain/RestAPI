from typing import Optional
from pydantic import BaseModel

class ClientAccountModel(BaseModel):
    mobile_number : str
    country_id: int
    app_version: str
    last_otp: Optional[str]
    api_key: Optional[str]
    last_usage: Optional[str]
    
class ClientAccountVerifyModel(BaseModel):
    mobile_number : str
    user_id: int
    otp: str
    api_key: str
