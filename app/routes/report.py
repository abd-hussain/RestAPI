from ast import And
from app.models.schemas.report import Report
from app.models.respond.general import generalResponse
from sqlalchemy.orm import Session
from fastapi import Request, status, Depends, APIRouter
from app.utils.database import get_db
from app.models.database import db_suggestion_reported, db_issue_reported
from app.models.database.client.db_client_user import DB_Client_Users
from app.models.database.mentor.db_mentor_user import DB_Mentor_Users
from app.utils.oauth2 import get_current_user
from app.utils.validation import validateLanguageHeader

router = APIRouter(
    prefix="/report",
    tags=["Report"]
)

@router.post("/issue", status_code=status.HTTP_201_CREATED)
async def create_issue(payload: Report,db: Session = Depends(get_db), get_current_user: int = Depends(get_current_user)):    
    client_query = db.query(DB_Client_Users).filter(DB_Client_Users.id == payload.user_id)
    mentor_query = db.query(DB_Mentor_Users).filter(DB_Mentor_Users.id == payload.user_id)

    if client_query.first() != None or mentor_query.first() != None:
        obj = db_issue_reported.DB_Issues_Reported(**payload.dict())
        db.add(obj)
        db.commit()
        return generalResponse(message= "successfully created issue", data= None)
        
    return generalResponse(message= "This User not exsist", data= None)

@router.get("/issue")
async def get_issue(request: Request, db: Session = Depends(get_db), get_current_user: int = Depends(get_current_user), limit: int = 10, skip: int = 0):
    myHeader = validateLanguageHeader(request)
    issues = db.query(db_issue_reported.DB_Issues_Reported.id, db_issue_reported.DB_Issues_Reported.user_id, 
                    db_issue_reported.DB_Issues_Reported.content, db_issue_reported.DB_Issues_Reported.attachment1, 
                    db_issue_reported.DB_Issues_Reported.attachment2, db_issue_reported.DB_Issues_Reported.attachment3).limit(limit).offset(skip).all()
    return generalResponse(message="list of issues return successfully", data=issues)

@router.post("/suggestion", status_code=status.HTTP_201_CREATED)
def create_suggestion(payload: Report,db: Session = Depends(get_db), get_current_user: int = Depends(get_current_user)):   
    client_query = db.query(DB_Client_Users).filter(DB_Client_Users.id == payload.user_id)
    mentor_query = db.query(DB_Mentor_Users).filter(DB_Mentor_Users.id == payload.user_id)

    if client_query.first() != None or mentor_query.first() != None:
        obj = db_suggestion_reported.DB_Suggestion_Reported(**payload.dict())
        db.add(obj)
        db.commit()
        return generalResponse(message= "successfully created suggestion", data= None)

    return generalResponse(message= "This User not exsist", data= None)

@router.get("/suggestion")
async def get_suggestion(request: Request, db: Session = Depends(get_db), get_current_user: int = Depends(get_current_user), limit: int = 10, skip: int = 0):
    myHeader = validateLanguageHeader(request)
    issues = db.query(db_suggestion_reported.DB_Suggestion_Reported.id, db_suggestion_reported.DB_Suggestion_Reported.user_id, 
                    db_suggestion_reported.DB_Suggestion_Reported.content, db_suggestion_reported.DB_Suggestion_Reported.attachment1, 
                    db_suggestion_reported.DB_Suggestion_Reported.attachment2, db_suggestion_reported.DB_Suggestion_Reported.attachment3).limit(limit).offset(skip).all()
    return generalResponse(message="list of suggestions return successfully", data=issues)