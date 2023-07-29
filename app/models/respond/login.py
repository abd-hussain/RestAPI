
from app.models.respond.main import Main
from pydantic.schema import Optional


class _LoginResponse(Main):
    id: int
    api_key: str
    blocked: bool
    first_name: Optional[str]
    last_name: Optional[str]

class LoginResponse(Main):
    data : _LoginResponse
    message: str = ""
        
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
    message: str = ""
