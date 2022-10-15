from fastapi import Depends, APIRouter, Header, Request
from pydantic import BaseModel

from app.enums.languages import LanguageModel

router = APIRouter(
    tags=["Filter"]
)

class Country(BaseModel):
    id: int
    nameAr: str
    nameEn: str
    image: str

@router.get("/countries")
async def get_countries(lang : LanguageModel = Header(default=LanguageModel.english)):
    if lang is LanguageModel.arabic:
        return {"lang" : "arabic"}
    return {"lang" : "english"}

@router.post("/countries")
async def create_countries(country: Country, lang : LanguageModel = Header(default=LanguageModel.english)):
    if lang is LanguageModel.arabic:
        return {"country.id": country.id, "lang" : "arabic"}
    return {"country.id": country.id, "lang" : "english"}