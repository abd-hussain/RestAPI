from pydantic import BaseModel
from typing import Union

class Category(BaseModel):
    id: int
    name_arabic: str
    name_english: str
    description_english: Union[str, None] = None
    description_arabic: Union[str, None] = None
    icon: str
    published: bool = True
    