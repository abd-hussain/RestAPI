from app.models.schemas.report import Report
from app.models.respond import general
from sqlalchemy.orm import Session
from fastapi import status, Depends, APIRouter
from app.utils.database.database import get_db
from app.models.database import db_models
from app.utils.oauth2 import get_current_user

router = APIRouter(
    prefix="/report",
    tags=["Report"]
)

@router.post("/issue", status_code=status.HTTP_201_CREATED)
def create_issue(payload: Report,db: Session = Depends(get_db), get_current_user: int = Depends(get_current_user)):    
    obj = db_models.Issues_Reported_items(**payload.dict())
    db.add(obj)
    db.commit()
    return general.generalResponse(message= "successfully created issue", data= None)

@router.post("/suggestion", status_code=status.HTTP_201_CREATED)
def create_suggestion(payload: Report,db: Session = Depends(get_db), get_current_user: int = Depends(get_current_user)):    
    obj = db_models.Suggestion_Reported_items(**payload.dict())
    db.add(obj)
    db.commit()
    return general.generalResponse(message= "successfully created suggestion", data= None)