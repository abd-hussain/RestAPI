from fastapi import FastAPI
from app.routes import subcategories, categories, countries, cities, report
from app.models.database import db_models
from app.utils.public_api import origins
from app.utils.database.database import engine
from fastapi.middleware.cors import CORSMiddleware

db_models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": " -#- Welcome To My API -#- "}

app.include_router(categories.router)
app.include_router(subcategories.router)
app.include_router(countries.router)
app.include_router(cities.router)
app.include_router(report.router)

