from typing import Union
from fastapi import FastAPI, Header
from pydantic import BaseModel
from pydantic import BaseModel
from app.routes import subcategories, categories

app = FastAPI()


@app.get("/")
async def root():
    return {"message": " -#- Welcome To My API -#- "}

## categories ##
app.include_router(categories.router)


## subcategories ##
app.include_router(subcategories.router)

