from app.models.respond.general import generalResponse
from sqlalchemy.orm import Session
from fastapi import Request, Depends, APIRouter
from app.utils.database import get_db
from app.models.database.db_category import DB_Categories
from app.models.database.db_suffix import DB_Suffix
from app.models.database.db_country import DB_Countries
from app.utils.validation import validateLanguageHeader
from typing import Optional

router = APIRouter(
    tags=["Filter"]
)

@router.get("/categories")
async def get_categories(request: Request, db: Session = Depends(get_db)):
    myHeader = validateLanguageHeader(request)
    
    categories = db.query(DB_Categories.id, DB_Categories.name_english.label(
        "name"), DB_Categories.icon).all()
    if (myHeader.language == "ar"):
        categories = db.query(DB_Categories.id, DB_Categories.name_arabic.label(
            "name"), DB_Categories.icon).all()

    return generalResponse(message="list of categories return successfully", data=categories)

@router.get("/countries")
async def get_countries(request: Request, db: Session = Depends(get_db), limit: int = 10, skip: int = 0, search: Optional[str] = ""):
    myHeader = validateLanguageHeader(request)
    countries = db.query(DB_Countries.id, DB_Countries.flag_image, DB_Countries.name_english.label(
        "name"), DB_Countries.currency_english.label("currency"), DB_Countries.prefix_number).filter(DB_Countries.name_english.contains(search)).limit(limit).offset(skip).all()
    if (myHeader.language == "ar"):
        countries = db.query(DB_Countries.id, DB_Countries.flag_image, DB_Countries.name_arabic.label(
            "name"), DB_Countries.currency_arabic.label("currency"), DB_Countries.prefix_number).filter(DB_Countries.name_arabic.contains(search)).limit(limit).offset(skip).all()
   
    return generalResponse(message="list of countries return successfully", data=countries)


@router.get("/suffix")
async def get_suffix(request: Request, db: Session = Depends(get_db)):
    myHeader = validateLanguageHeader(request)
    
    suffix = db.query(DB_Suffix.id, DB_Suffix.name_english.label("name")).all()
    if (myHeader.language == "ar"):
        suffix = db.query(DB_Suffix.id, DB_Suffix.name_arabic.label("name")).all()

    return generalResponse(message="list of suffix return successfully", data=suffix)