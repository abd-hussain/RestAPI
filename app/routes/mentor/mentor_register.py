from fastapi import Request, Depends ,APIRouter, Form, HTTPException, status
from pydantic import EmailStr
from sqlalchemy.orm import Session
from app.utils.generate import generateAPIKey, generateActvationCode
from app.utils.validation import validateLanguageHeader
from app.utils.database import get_db
from app.models.database.mentor.db_mentor_user import DB_Mentor_Users
from app.models.schemas.mentor_account import  RegisterMentorAccountModel

from app.utils.validation import validateLanguageHeader
from app.models.respond.general import generalResponse
from app.utils.oauth2 import hashingPassword

router = APIRouter(
    prefix="/mentor",
    tags=["Account"]
)

@router.post("/register")
async def register_mentor(request: Request,payload: RegisterMentorAccountModel,
       db: Session = Depends(get_db)):
    myHeader = validateLanguageHeader(request)
    payload.password = hashingPassword(payload.password)
 
    payload.api_key = generateAPIKey()
    payload.invitation_code = generateActvationCode()

    query1 = db.query(DB_Mentor_Users).filter(DB_Mentor_Users.mobile_number == payload.mobile_number).first()
    query2 = db.query(DB_Mentor_Users).filter(DB_Mentor_Users.email == payload.email).first()

    if query1 != None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail= "User with this mobile number already exsist")
    if query2 != None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail= "User with this email already exsist")


    obj = DB_Mentor_Users(**payload.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    
    return generalResponse(message= "Account Created successfully", data=None)


    
