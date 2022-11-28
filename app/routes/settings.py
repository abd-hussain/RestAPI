
from fastapi import Request, Depends, APIRouter, status
from sqlalchemy.orm import Session
from app.models.database.db_versions import DB_Versions
from app.models.schemas.leads import ListLeads
from app.models.database.db_terms import DB_Terms
from app.models.database.db_leads import DB_Leads
from app.models.respond.general import generalResponse
from app.utils.database import get_db
from app.utils.validation import validateLanguageHeader


router = APIRouter(
    prefix="/settings",
    tags=["Settings"]
)

@router.get("/versions")
async def get_Versions(request: Request, db: Session = Depends(get_db)):
    myHeader = validateLanguageHeader(request)
    data = db.query(DB_Versions.id, DB_Versions.version.label(
        "number"), DB_Versions.content_english.label(
        "content"), DB_Versions.is_forced).all()
    if (myHeader.language == "ar"):
          data = db.query(DB_Versions.id, DB_Versions.version.label(
        "number"), DB_Versions.content_arabic.label(
        "content"), DB_Versions.is_forced).all()
    return generalResponse(message="list of versions return successfully", data=data)


@router.get("/terms")
async def get_Terms(request: Request, db: Session = Depends(get_db)):
    myHeader = validateLanguageHeader(request)
    data = db.query(DB_Terms.id, DB_Terms.title_english.label(
        "title"), DB_Terms.content_english.label(
        "content")).all()
    if (myHeader.language == "ar"):
        data = db.query(DB_Terms.id, DB_Terms.title_arabic.label(
            "title"), DB_Terms.content_arabic.label(
            "content")).all()
    return generalResponse(message="list of terms return successfully", data=data)

@router.post("/leads", status_code=status.HTTP_201_CREATED)
async def upload_leads(payload: ListLeads,request: Request, db: Session = Depends(get_db)):    
    myHeader = validateLanguageHeader(request)
    
    for val in payload.list:
        obj = DB_Leads(**val.dict())
        db.add(obj)
        db.commit()

    return generalResponse(message= "successfully created leads", data= None)