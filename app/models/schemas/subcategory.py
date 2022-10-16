
from pydantic import BaseModel
from typing import Union

class SubCategory(BaseModel):
    id: int
    catid: int
    nameAr: str
    nameEn: str
    image: str
    description: Union[str, None] = None
    published: bool = True