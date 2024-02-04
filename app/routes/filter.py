from app.models.database.client.db_client_user import DB_Client_Users
from app.models.database.db_majors import DB_Majors
from app.models.database.mentor.db_mentor_user import DB_Mentor_Users
from app.models.respond.general import generalResponse
from sqlalchemy.orm import Session
from fastapi import Request, Depends, APIRouter
from app.utils.database import get_db
from app.models.database.db_category import DB_Categories
from app.models.database.db_suffix import DB_Suffix
from app.models.database.db_country import DB_Countries
from app.utils.validation import validateLanguageHeader

router = APIRouter(
    tags=["Filter"]
)

@router.get("/categories")
async def get_categories(request: Request, db: Session = Depends(get_db)):
    myHeader = validateLanguageHeader(request)
    
    category_column = DB_Categories.name_arabic if myHeader.language == "ar" else DB_Categories.name_english
    categories = db.query(DB_Categories.id, category_column.label("name"), DB_Categories.icon).all()

    return generalResponse(message="list of categories return successfully", data=categories)

@router.get("/countries")
async def get_countries(request: Request, db: Session = Depends(get_db)):
    myHeader = validateLanguageHeader(request)
    
    country_name_column = DB_Countries.name_arabic if myHeader.language == "ar" else DB_Countries.name_english
    country_currency = DB_Countries.currency_arabic if myHeader.language == "ar" else DB_Countries.currency_english
    countries = db.query(DB_Countries.id, DB_Countries.flag_image, country_name_column.label("name"), 
                         country_currency.label("currency"),DB_Countries.dialCode,
                         DB_Countries.country_code, DB_Countries.currency_code,
                         DB_Countries.minLength, DB_Countries.maxLength, 
                         DB_Countries.dollar_equivalent).all()
    
    return generalResponse(message="list of countries return successfully", data=countries)

@router.get("/suffix")
async def get_suffix(request: Request, db: Session = Depends(get_db)):
    myHeader = validateLanguageHeader(request)
    
    suffix_name_column = DB_Suffix.name_arabic if myHeader.language == "ar" else DB_Suffix.name_english
    suffix = db.query(DB_Suffix.id, suffix_name_column.label("name")).all()

    return generalResponse(message="list of suffix return successfully", data=suffix)

@router.get("/majors")
async def get_majors(request: Request, db: Session = Depends(get_db)):
    myHeader = validateLanguageHeader(request)

    majors_column = DB_Majors.name_arabic if myHeader.language == "ar" else DB_Majors.name_english
    majors = db.query(DB_Majors.id, majors_column.label("name")).all()
        
    return generalResponse(message="majors return successfully", data=majors)

@router.post("/checkemial")
async def post_validate_email(email: str, db: Session = Depends(get_db)): 
    mentor_exists = db.query(DB_Mentor_Users).filter(DB_Mentor_Users.email == email).first() is not None
    client_exists = db.query(DB_Client_Users).filter(DB_Client_Users.email == email).first() is not None

    email_exists = mentor_exists or client_exists

    return generalResponse(message="checking email is exsisting", data=email_exists)

@router.post("/checkmobile")
async def post_validate_mobile(mobile: str, db: Session = Depends(get_db)): 
    mentor_exists = db.query(DB_Mentor_Users).filter(DB_Mentor_Users.mobile_number == mobile).first() is not None
    client_exists = db.query(DB_Client_Users).filter(DB_Client_Users.mobile_number == mobile).first() is not None

    mobile_exists = mentor_exists or client_exists

    return generalResponse(message="checking mobile is exsisting", data=mobile_exists)


@router.post("/referalcode")
async def post_validate_invitation_code(code: str, db: Session = Depends(get_db)): 
    mentor_exists = db.query(DB_Mentor_Users).filter(DB_Mentor_Users.invitation_code == code).first() is not None
    client_exists = db.query(DB_Client_Users).filter(DB_Client_Users.invitation_code == code).first() is not None
    
    code_exists = mentor_exists or client_exists

    return generalResponse(message="checking invitation Code exsisting", data=code_exists)


@router.post("/currency-converter")
async def currency_converter(currency: str, request: Request, db: Session = Depends(get_db)):
    
    country = db.query(DB_Countries.currency_code, DB_Countries.dollar_equivalent).all()
    
    dollar_equivalent = 0.0
    
    for coun in country:
        if coun.currency_code == currency:
            dollar_equivalent = coun.dollar_equivalent

    return generalResponse(message="dollar Equivalent", data=dollar_equivalent)