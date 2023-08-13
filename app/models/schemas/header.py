from pydantic import BaseModel


class HeaderRequest(BaseModel):
    apikey: str
    user_id: str
    language: str

class PreLoginHeaderRequest(BaseModel):
    language: str