from fastapi import  APIRouter, Header, status

from app.enums.languages import LanguageModel
from app.models.schemas.category import Category

router = APIRouter(
    prefix="/categories",
    tags=["categories"]
)

@router.get("/")
async def get_categories(lang : LanguageModel = Header(default=LanguageModel.english)):
    if lang is LanguageModel.arabic:
        return {"id": 1, "name" : "arabic"}
    return {"id": 1, "name" : "english"}

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_category(payload: Category ,lang : LanguageModel = Header(default=LanguageModel.english)):
    if lang is LanguageModel.arabic:
        return payload
    return payload

@router.put("/")
async def update_category(id: int ,lang : LanguageModel = Header(default=LanguageModel.english)):
    if lang is LanguageModel.arabic:
        return id
    return id


@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_category(id: int ,lang : LanguageModel = Header(default=LanguageModel.english)):
    if lang is LanguageModel.arabic:
        return id
    return id