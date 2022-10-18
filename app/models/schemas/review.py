from typing import Optional
from pydantic import BaseModel

class Review(BaseModel) :
    item_id:int
    stars: int
    content: str
    
class ReviewDelete(BaseModel) :
    item_id:int