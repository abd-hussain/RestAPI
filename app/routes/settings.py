
from fastapi import Request, Depends, APIRouter, status
from sqlalchemy.orm import Session
from app.models.database.db_versions import DB_Versions, Platform
from app.models.schemas.leads import ListLeads
from app.models.database.db_leads import DB_Leads
from app.models.respond.general import generalResponse
from app.utils.database import get_db
from app.utils.validation import validateLanguageHeader


router = APIRouter(
    prefix="/settings",
    tags=["Settings"]
)

@router.get("/versions")
async def get_Versions(platform: str, request: Request, db: Session = Depends(get_db)):
    myHeader = validateLanguageHeader(request)
    
    enumValue = Platform.client
    
    if platform == "mentor":
        enumValue = Platform.mentor
    
    data = db.query(DB_Versions.id, DB_Versions.version.label(
        "number"), DB_Versions.content_english.label(
        "content"), DB_Versions.is_forced, DB_Versions.platform).filter(
                         DB_Versions.platform == enumValue).all()
    if (myHeader.language == "ar"):
          data = db.query(DB_Versions.id, DB_Versions.version.label(
        "number"), DB_Versions.content_arabic.label(
        "content"), DB_Versions.is_forced, DB_Versions.platform).filter(
                         DB_Versions.platform == enumValue).all()
    return generalResponse(message="list of versions return successfully", data=data)

@router.post("/leads", status_code=status.HTTP_201_CREATED)
async def upload_leads(payload: ListLeads, db: Session = Depends(get_db)):    
    
    for val in payload.list:
        obj = DB_Leads(**val.dict())
        db.add(obj)
        db.commit()
    return generalResponse(message= "successfully created leads", data= None)