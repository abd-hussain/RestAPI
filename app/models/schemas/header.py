from pydantic import BaseModel


# class HeaderRequest(BaseModel):
#     apikey: str
#     user_id: str
#     language: str

class languageHeaderRequest(BaseModel):
    language: str
    
class headerRequest(BaseModel):
    language: str
    api_key: str