from pydantic import BaseModel
from typing import Union

class Category(BaseModel):
    id: int
    nameAr: str
    nameEn: str
    description: Union[str, None] = None
    published: bool = True