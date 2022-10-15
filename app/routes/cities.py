
from fastapi import Depends, APIRouter, Header, Request
from pydantic import BaseModel

from app.enums.languages import LanguageModel

router = APIRouter(
    tags=["Filter"]
)

class City(BaseModel):
    id: int
    countryid: int
    nameAr: str
    nameEn: str

@router.get("/cities")
async def get_cities(country_id: int, lang : LanguageModel = Header(default=LanguageModel.english)):
    if lang is LanguageModel.arabic:
        return {"id": country_id, "name" : "arabic"}
    return {"id": country_id, "name" : "english"}

@router.post("/cities")
async def create_city(city: City ,lang : LanguageModel = Header(default=LanguageModel.english)):
    if lang is LanguageModel.arabic:
        return city
    return city