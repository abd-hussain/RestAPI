from fastapi import Depends, APIRouter, Header, Request
from pydantic import BaseModel
from typing import Union

from app.enums.languages import LanguageModel

router = APIRouter(
    prefix="/subcategories",
    tags=["subcategories"]
)

class SubCategory(BaseModel):
    id: int
    catid: int
    nameAr: str
    nameEn: str
    image: str
    description: Union[str, None] = None
    published: bool = True

@router.get("/")
async def get_subcategories(cat_id: int, lang : LanguageModel = Header(default=LanguageModel.english)):
    if lang is LanguageModel.arabic:
        return {"cat_id": cat_id, "lang" : "arabic"}
    return {"cat_id": cat_id, "lang" : "english"}

@router.post("/")
async def create_subcategories(sub: SubCategory, lang : LanguageModel = Header(default=LanguageModel.english)):
    if lang is LanguageModel.arabic:
        return {"cat_id": sub.catid, "lang" : "arabic"}
    return {"cat_id": sub.catid, "lang" : "english"}