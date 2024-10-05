from typing import Optional
from pydantic import BaseModel

class RegisterUnknownAccountModel(BaseModel):
    id: int
    language: str
    api_key: str
    os_type: Optional[str] 
    os_version: Optional[str] 
    device_name: Optional[str] 
    app_version: Optional[str] 