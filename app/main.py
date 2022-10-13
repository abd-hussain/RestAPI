from typing import Union
from fastapi import FastAPI, Header
from pydantic import BaseModel
from pydantic import BaseModel

from app.enums.languages import LanguageModel

app = FastAPI()


class Category(BaseModel):
    id: int
    nameAr: str
    nameEn: str
    image: str
    description: Union[str, None] = None

@app.get("/")
async def root():
    return {"message": "Hello World"}

## categories ##
@app.get("/categories")
async def get_categories(lang : LanguageModel = Header(default=LanguageModel.english)):
    if lang is LanguageModel.arabic:
        return {"id": 1, "name" : "arabic"}
    return {"id": 1, "name" : "english"}

@app.post("/categories")
async def create_category(cat: Category ,lang : LanguageModel = Header(default=LanguageModel.english)):
    if lang is LanguageModel.arabic:
        return cat
    return cat

## subcategories ##

@app.get("/subcategories")
async def get_subcategories(cat_id: int, lang : LanguageModel = Header(default=LanguageModel.english)):
    if lang is LanguageModel.arabic:
        return {"cat_id": cat_id, "lang" : "arabic"}
    return {"cat_id": cat_id, "lang" : "english"}
