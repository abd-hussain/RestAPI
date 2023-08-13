from app.models.database.client.db_client_user import DB_Client_Users
from app.models.database.db_majors import DB_Majors
from app.models.database.mentor.db_mentor_user import DB_Mentor_Users
from app.models.respond.general import generalResponse
from sqlalchemy.orm import Session
from fastapi import Request, Depends, APIRouter
from app.models.schemas.referal_code import ReferalCode
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
        "name"), DB_Countries.currency_english.label("currency"), DB_Countries.dialCode, DB_Countries.minLength, DB_Countries.maxLength).filter(DB_Countries.name_english.contains(search)).limit(limit).offset(skip).all()
    if (myHeader.language == "ar"):
        countries = db.query(DB_Countries.id, DB_Countries.flag_image, DB_Countries.name_arabic.label(
            "name"), DB_Countries.currency_arabic.label("currency"), DB_Countries.dialCode, DB_Countries.minLength, DB_Countries.maxLength).filter(DB_Countries.name_arabic.contains(search)).limit(limit).offset(skip).all()
   
    return generalResponse(message="list of countries return successfully", data=countries)

@router.get("/suffix")
async def get_suffix(request: Request, db: Session = Depends(get_db)):
    myHeader = validateLanguageHeader(request)
    
    suffix = db.query(DB_Suffix.id, DB_Suffix.name_english.label("name")).all()
    if (myHeader.language == "ar"):
        suffix = db.query(DB_Suffix.id, DB_Suffix.name_arabic.label("name")).all()

    return generalResponse(message="list of suffix return successfully", data=suffix)

@router.get("/majors")
async def get_majors(request: Request, db: Session = Depends(get_db)):
    myHeader = validateLanguageHeader(request)

    majors = db.query(DB_Majors.id, DB_Majors.name_english.label("name")).all()
    if (myHeader.language == "ar"):
        majors = db.query(DB_Majors.id, DB_Majors.name_arabic.label("name")).all()
        
    return generalResponse(message="majors return successfully", data=majors)


@router.post("/referalcode")
async def post_validate_referal_code(payload: ReferalCode, db: Session = Depends(get_db)): 

    mentor_query = db.query(DB_Mentor_Users.invitation_code).all()
    client_query = db.query(DB_Client_Users.invitation_code).all()
    
    clientList = [''.join(i) for i in client_query]
    mentorList = [''.join(x) for x in mentor_query]

    codeIsExsist = False
    
    if (payload.code) in mentorList:
        codeIsExsist = True
    
    if (payload.code) in clientList:
        codeIsExsist = True

    return generalResponse(message="checking Referal Code exsisting", data=codeIsExsist)

@router.post("/checkemial")
async def post_validate_email(email: str, db: Session = Depends(get_db)): 
    mentor_query = db.query(DB_Mentor_Users.email).all()
    client_query = db.query(DB_Client_Users.email).all()
    
    clientList = [''.join(i) for i in client_query]
    mentorList = [''.join(x) for x in mentor_query]
    
    emailIsExsist = False

    if email in mentorList:
        emailIsExsist = True
    
    if email in clientList:
        emailIsExsist = True

    return generalResponse(message="checking email is exsisting", data=emailIsExsist)

@router.post("/checkmobile")
async def post_validate_mobile(mobile: str, db: Session = Depends(get_db)): 
    mentor_query = db.query(DB_Mentor_Users.mobile_number).all()
    client_query = db.query(DB_Client_Users.mobile_number).all()
    
    clientList = [''.join(i) for i in client_query]
    mentorList = [''.join(x) for x in mentor_query]
    
    mobileIsExsist = False

    if mobile in mentorList:
        mobileIsExsist = True
    
    if mobile in clientList:
        mobileIsExsist = True

    return generalResponse(message="checking mobile is exsisting", data=mobileIsExsist)