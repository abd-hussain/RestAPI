from pydantic import BaseModel


class City(BaseModel):
    id: int
    countryid: int
    nameAr: str
    nameEn: str
    published: bool = True