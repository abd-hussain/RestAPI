from typing import Optional
from pydantic import BaseModel

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
