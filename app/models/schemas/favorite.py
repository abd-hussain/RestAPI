from typing import Optional
from pydantic import BaseModel

class Favorite(BaseModel) :
    item_id:int
    status: bool
