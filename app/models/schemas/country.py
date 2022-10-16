from pydantic import BaseModel


class Country(BaseModel):
    id: int
    nameAr: str
    nameEn: str
    image: str
    published: bool = True