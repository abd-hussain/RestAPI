from app.models.respond.general import generalResponse
from sqlalchemy.orm import Session
from fastapi import Request, Depends, APIRouter
from app.utils.database.database import get_db
from app.models.database.db_category import DB_Categories
from app.models.database.db_country import DB_Countries
from app.utils.validation import validateLanguageHeader
from app.models.database.db_subcategory import DB_Subcategories

router = APIRouter(
    tags=["Filter"]
)

@router.get("/categories")
async def get_categories(request: Request, db: Session = Depends(get_db)):
    myHeader = validateLanguageHeader(request)
    categories = db.query(DB_Categories.id, DB_Categories.name_english.label(
        "name"), DB_Categories.icon, DB_Categories.description_english.label(
        "description")).all()
    if (myHeader.language == "ar"):
        categories = db.query(DB_Categories.id, DB_Categories.name_arabic.label(
            "name"), DB_Categories.icon, DB_Categories.description_arabic.label(
        "description")).all()

    return generalResponse(message="list of categories return successfully", data=categories)

@router.get("/subcategories")
async def get_subcategories(cat_id: int, request: Request, db: Session = Depends(get_db)):
    myHeader = validateLanguageHeader(request)

    subCategories = db.query(DB_Subcategories.id, DB_Subcategories.name_english.label(
        "name")).filter(DB_Subcategories.category_id == cat_id).all()
    if (myHeader.language == "ar"):
        subCategories = db.query(DB_Subcategories.id, DB_Subcategories.name_arabic.label(
            "name")).filter(DB_Subcategories.category_id == cat_id).all()

    return generalResponse(message="list of subCategories return successfully", data=subCategories)

@router.get("/countries")
async def get_countries(request: Request, db: Session = Depends(get_db)):
    myHeader = validateLanguageHeader(request)
    countries = db.query(DB_Countries.id, DB_Countries.flag_image, DB_Countries.name_english.label(
        "name"), DB_Countries.currency_english.label("currency"), DB_Countries.prefix_number).all()
    print(countries)
    if (myHeader.language == "ar"):
        countries = db.query(DB_Countries.id, DB_Countries.flag_image, DB_Countries.name_arabic.label(
            "name"), DB_Countries.currency_arabic.label("currency"), DB_Countries.prefix_number).all()

    return generalResponse(message="list of countries return successfully", data=countries)