from fastapi import Depends, APIRouter, Header, Request
from pydantic import BaseModel
from typing import Union
from app.enums.languages import LanguageModel

router = APIRouter(
    prefix="/categories",
    tags=["categories"]
)

class Category(BaseModel):
    id: int
    nameAr: str
    nameEn: str
    description: Union[str, None] = None
    published: bool = True

@router.get("/")
async def get_categories(lang : LanguageModel = Header(default=LanguageModel.english)):
    if lang is LanguageModel.arabic:
        return {"id": 1, "name" : "arabic"}
    return {"id": 1, "name" : "english"}

@router.post("/")
async def create_category(cat: Category ,lang : LanguageModel = Header(default=LanguageModel.english)):
    if lang is LanguageModel.arabic:
        return cat
    return cat

@router.put("/")
async def update_category(cat_id: int ,lang : LanguageModel = Header(default=LanguageModel.english)):
    if lang is LanguageModel.arabic:
        return cat_id
    return cat_id


@router.delete("/")
async def delete_category(cat_id: int ,lang : LanguageModel = Header(default=LanguageModel.english)):
    if lang is LanguageModel.arabic:
        return cat_id
    return cat_id