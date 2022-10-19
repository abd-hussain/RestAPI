from pydantic import BaseModel


class Country(BaseModel):
    id: int
    name_arabic: str
    name_english: str
    flag_image: str
    currency_arabic : str  
    currency_english : str
    prefix_number : str
    published: bool = True