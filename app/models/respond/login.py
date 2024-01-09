
from app.models.respond.main import Main
from pydantic.schema import Optional


class _LoginResponse(Main):
    id: int
    api_key: str
    blocked: bool
    first_name: Optional[str]
    last_name: Optional[str]
    last_otp: str
    
class LoginResponse(Main):
    data : _LoginResponse
    message: str = ""
        