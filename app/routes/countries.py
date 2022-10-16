from fastapi import APIRouter, Header, status
from app.enums.languages import LanguageModel
from app.models.schemas.country import Country

router = APIRouter(
    prefix="/countries",
    tags=["countries"]
)

@router.get("/")
async def get_countries(lang : LanguageModel = Header(default=LanguageModel.english)):
    if lang is LanguageModel.arabic:
        return {"lang" : "arabic"}
    return {"lang" : "english"}

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_countries(payload: Country, lang : LanguageModel = Header(default=LanguageModel.english)):
    if lang is LanguageModel.arabic:
        return {"country.id": payload.id, "lang" : "arabic"}
    return {"country.id": payload.id, "lang" : "english"}

@router.put("/")
async def update_countries(id: int ,lang : LanguageModel = Header(default=LanguageModel.english)):
    if lang is LanguageModel.arabic:
        return id
    return id


@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_countries(id: int ,lang : LanguageModel = Header(default=LanguageModel.english)):
    if lang is LanguageModel.arabic:
        return id
    return id