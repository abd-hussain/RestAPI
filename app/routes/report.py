from app.models.schemas.report import Report
from app.models.respond.general import generalResponse
from sqlalchemy.orm import Session
from fastapi import Request, status, Depends, APIRouter
from app.utils.database.database import get_db
from app.models.database import db_suggestion_reported, db_issue_reported, db_user
from app.utils.oauth2 import get_current_user
from app.utils.validation import validateLanguageHeader

router = APIRouter(
    prefix="/report",
    tags=["Report"]
)

@router.post("/issue", status_code=status.HTTP_201_CREATED)
async def create_issue(payload: Report,request: Request, db: Session = Depends(get_db), get_current_user: int = Depends(get_current_user)):    
    myHeader = validateLanguageHeader(request)
    query = db.query(db_user.DB_Users).filter(db_user.DB_Users.id == payload.user_id)

    if query.first() != None :
        obj = db_issue_reported.DB_Issues_Reported(**payload.dict())
        db.add(obj)
        db.commit()
        return generalResponse(message= "successfully created issue", data= None)
        
    return generalResponse(message= "This User not exsist", data= None)

@router.get("/issue")
async def get_issue(request: Request, db: Session = Depends(get_db), get_current_user: int = Depends(get_current_user)):
    myHeader = validateLanguageHeader(request)
    issues = db.query(db_issue_reported.DB_Issues_Reported.id, db_issue_reported.DB_Issues_Reported.user_id, 
                    db_issue_reported.DB_Issues_Reported.content, db_issue_reported.DB_Issues_Reported.attachment1, 
                    db_issue_reported.DB_Issues_Reported.attachment2, db_issue_reported.DB_Issues_Reported.attachment3).all()
    return generalResponse(message="list of issues return successfully", data=issues)

@router.post("/suggestion", status_code=status.HTTP_201_CREATED)
def create_suggestion(payload: Report,db: Session = Depends(get_db), get_current_user: int = Depends(get_current_user)):    
    query = db.query(db_user.DB_Users).filter(db_user.DB_Users.id == payload.user_id)

    if query.first() != None :
        obj = db_suggestion_reported.DB_Suggestion_Reported(**payload.dict())
        db.add(obj)
        db.commit()
        return generalResponse(message= "successfully created suggestion", data= None)

    return generalResponse(message= "This User not exsist", data= None)

@router.get("/suggestion")
async def get_suggestion(request: Request, db: Session = Depends(get_db), get_current_user: int = Depends(get_current_user)):
    myHeader = validateLanguageHeader(request)
    issues = db.query(db_suggestion_reported.DB_Suggestion_Reported.id, db_suggestion_reported.DB_Suggestion_Reported.user_id, 
                    db_suggestion_reported.DB_Suggestion_Reported.content, db_suggestion_reported.DB_Suggestion_Reported.attachment1, 
                    db_suggestion_reported.DB_Suggestion_Reported.attachment2, db_suggestion_reported.DB_Suggestion_Reported.attachment3).all()
    return generalResponse(message="list of suggestions return successfully", data=issues)