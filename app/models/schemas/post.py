from typing import Optional
from pydantic import BaseModel

class Post(BaseModel) :
    id: Optional[int]
    customers_owner_id: Optional[int]
    category_id: int
    content: str
    post_img: Optional[str] 

class PostComment(BaseModel) :
    post_id: int
    user_type: str 
    content: str
    up: int
    down: int