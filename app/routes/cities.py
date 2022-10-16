
from fastapi import Depends, APIRouter, Header, Request
from pydantic import BaseModel

from app.enums.languages import LanguageModel

router = APIRouter(
    prefix="/cities",
    tags=["cities"]
)

class City(BaseModel):
    id: int
    countryid: int
    nameAr: str
    nameEn: str
    published: bool = True

@router.get("/")
async def get_cities(country_id: int, lang : LanguageModel = Header(default=LanguageModel.english)):
    if lang is LanguageModel.arabic:
        return {"id": country_id, "name" : "arabic"}
    return {"id": country_id, "name" : "english"}

@router.post("/")
async def create_city(city: City ,lang : LanguageModel = Header(default=LanguageModel.english)):
    if lang is LanguageModel.arabic:
        return city
    return city

@router.put("/")
async def update_city(city_id: int ,lang : LanguageModel = Header(default=LanguageModel.english)):
    if lang is LanguageModel.arabic:
        return city_id
    return city_id


@router.delete("/")
async def delete_city(city_id: int ,lang : LanguageModel = Header(default=LanguageModel.english)):
    if lang is LanguageModel.arabic:
        return city_id
    return city_id