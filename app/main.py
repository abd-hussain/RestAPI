from typing import Union
from fastapi import FastAPI, Header
from app.routes import subcategories, categories, countries, cities, report

app = FastAPI()

@app.get("/")
async def root():
    return {"message": " -#- Welcome To My API -#- "}

app.include_router(categories.router)
app.include_router(subcategories.router)
app.include_router(countries.router)
app.include_router(cities.router)
app.include_router(report.router)

