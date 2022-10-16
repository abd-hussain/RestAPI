from fastapi import Depends, APIRouter, Header, Request, status, Response

from app.enums.languages import LanguageModel
from app.models.schemas.subcategory import SubCategory

router = APIRouter(
    prefix="/subcategories",
    tags=["subcategories"]
)

@router.get("/")
async def get_subcategories(cat_id: int, lang : LanguageModel = Header(default=LanguageModel.english)):
    if lang is LanguageModel.arabic:
        return {"cat_id": cat_id, "lang" : "arabic"}
    return {"cat_id": cat_id, "lang" : "english"}

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_subcategories(payload: SubCategory, lang : LanguageModel = Header(default=LanguageModel.english)):
    if lang is LanguageModel.arabic:
        return {"cat_id": payload.catid, "lang" : "arabic"}
    return {"cat_id": payload.catid, "lang" : "english"}

@router.put("/")
async def update_subcategories(id: int ,lang : LanguageModel = Header(default=LanguageModel.english)):
    if lang is LanguageModel.arabic:
        return id
    return id


@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_subcategories(id: int ,lang : LanguageModel = Header(default=LanguageModel.english)):
    if lang is LanguageModel.arabic:
        return id
    return id