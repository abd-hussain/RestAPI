
from fastapi import Request, Depends, APIRouter, status, HTTPException
from sqlalchemy.orm import Session
from app.models.database.db_versions import DB_Versions
from app.models.schemas.leads import ListLeads
from app.models.database.db_terms import DB_Terms
from app.models.database.db_leads import DB_Leads
from app.models.database.db_user import DB_Users
from app.models.database.db_notifications import DB_Notifications
from app.models.respond.general import generalResponse
from app.utils.database.database import get_db
from app.utils.generate import generateRequestId
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
        print(val)
        obj = DB_Leads(**val.dict())
        db.add(obj)
        db.commit()

    return generalResponse(message= "successfully created leads", data= None)

@router.get("/notifications")
async def get_Notifications(id: int ,request: Request, db: Session = Depends(get_db)):
    myHeader = validateLanguageHeader(request)
    query = db.query(DB_Users.id).filter(DB_Users.id == id)

    if query.first() == None:
      raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail={"message": f"This ID not exsist", "request_id": generateRequestId()})

    data = db.query(DB_Notifications.id, DB_Notifications.title_english.label(
        "title"), DB_Notifications.content_english.label(
        "content")).filter(DB_Notifications.receiver_id == id).all()
    if (myHeader.language == "ar"):
        data = db.query(DB_Notifications.id, DB_Notifications.title_arabic.label(
            "title"), DB_Notifications.content_arabic.label(
            "content")).filter(DB_Notifications.receiver_id == id).all()
    return generalResponse(message="list of notifications return successfully", data=data)
