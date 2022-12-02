from pydantic import BaseModel
    
class Post(BaseModel):
    language: str
    content: str
    owner_id : int
    