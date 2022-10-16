
from fastapi import  APIRouter, Header, status
from app.enums.languages import LanguageModel
from app.models.schemas.city import City

router = APIRouter(
    prefix="/cities",
    tags=["cities"]
)

@router.get("/")
async def get_cities(country_id: int, lang : LanguageModel = Header(default=LanguageModel.english)):
    if lang is LanguageModel.arabic:
        return {"id": country_id, "name" : "arabic"}
    return {"id": country_id, "name" : "english"}

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_city(payload: City ,lang : LanguageModel = Header(default=LanguageModel.english)):
    if lang is LanguageModel.arabic:
        return payload
    return payload

@router.put("/")
async def update_city(id: int ,lang : LanguageModel = Header(default=LanguageModel.english)):
    if lang is LanguageModel.arabic:
        return id
    return id


@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_city(id: int ,lang : LanguageModel = Header(default=LanguageModel.english)):
    if lang is LanguageModel.arabic:
        return id
    return id