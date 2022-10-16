from fastapi import Depends, APIRouter, Header, Request
from pydantic import BaseModel

from app.enums.languages import LanguageModel

router = APIRouter(
    prefix="/countries",
    tags=["countries"]
)

class Country(BaseModel):
    id: int
    nameAr: str
    nameEn: str
    image: str
    published: bool = True

@router.get("/")
async def get_countries(lang : LanguageModel = Header(default=LanguageModel.english)):
    if lang is LanguageModel.arabic:
        return {"lang" : "arabic"}
    return {"lang" : "english"}

@router.post("/")
async def create_countries(country: Country, lang : LanguageModel = Header(default=LanguageModel.english)):
    if lang is LanguageModel.arabic:
        return {"country.id": country.id, "lang" : "arabic"}
    return {"country.id": country.id, "lang" : "english"}

@router.put("/")
async def update_countries(country_id: int ,lang : LanguageModel = Header(default=LanguageModel.english)):
    if lang is LanguageModel.arabic:
        return country_id
    return country_id


@router.delete("/")
async def delete_countries(country_id: int ,lang : LanguageModel = Header(default=LanguageModel.english)):
    if lang is LanguageModel.arabic:
        return country_id
    return country_id