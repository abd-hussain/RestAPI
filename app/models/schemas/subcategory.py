
from pydantic import BaseModel
from typing import Union

class SubCategory(BaseModel):
    id: int
    category_id: int
    name_arabic: str
    name_english: str
    icon: str
    description_english: Union[str, None] = None
    description_arabic: Union[str, None] = None
    published: bool = True