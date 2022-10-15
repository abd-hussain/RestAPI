from fastapi import Depends, APIRouter, Header, Request
from pydantic import BaseModel
from typing import Union
from app.enums.languages import LanguageModel

router = APIRouter(
    tags=["Filter"]
)

class Category(BaseModel):
    id: int
    nameAr: str
    nameEn: str
    description: Union[str, None] = None

@router.get("/categories")
async def get_categories(lang : LanguageModel = Header(default=LanguageModel.english)):
    if lang is LanguageModel.arabic:
        return {"id": 1, "name" : "arabic"}
    return {"id": 1, "name" : "english"}

@router.post("/categories")
async def create_category(cat: Category ,lang : LanguageModel = Header(default=LanguageModel.english)):
    if lang is LanguageModel.arabic:
        return cat
    return cat