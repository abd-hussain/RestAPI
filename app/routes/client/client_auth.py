from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.models.database.client.db_client_user import DB_Client_Users
from app.models.schemas.client_account import ClientAccountModel, ClientAccountVerifyModel
from app.utils.generate import generateAPIKey, generateOTP
from app.utils.database import get_db
from app.models.respond.general import generalResponse
from app.models.respond.login import LoginResponse
from app.utils.validation import verifyKey
from app.utils.oauth2 import create_access_token
from datetime import datetime

router = APIRouter(    
    prefix="/client-auth",
    tags=["Authentication"]
)

@router.post('/' , response_model=LoginResponse)
def authentication(payload: ClientAccountModel, db: Session = Depends(get_db)):
    user = db.query(DB_Client_Users).filter(DB_Client_Users.mobile_number == payload.mobile_number).first()
    payload.last_otp = generateOTP()
    payload.last_usage = datetime.utcnow()
    
    if user is None:

        user = create_user(db, payload)
        return generalResponse(message= "successfully created new account", data=user)
    
    if user.blocked == True:
         raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="User Blocked")
         
    user = update_user(db, user, payload.last_otp)
    return generalResponse(message= "OTP Sended successfully", data=user)

@router.post('-verify')
def verify_otp(payload: ClientAccountVerifyModel, db: Session =  Depends(get_db)):
    user = db.query(DB_Client_Users).filter(DB_Client_Users.mobile_number == payload.mobile_number).first()

    if user is None:
      raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Mobile number is not valid")
    
    if not verifyKey(payload.otp, user.last_otp):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="OTP is not valid")

    if not verifyKey(payload.user_id, user.id):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="id is not valid")
    
    if not verifyKey(payload.api_key, user.api_key):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="API Key is not valid")
    
    access_token = create_access_token(data={"api_key" : payload.api_key, "user_id" : payload.user_id})
    
    user.last_usage = datetime.utcnow()
    db.commit()
    
    return generalResponse(message= "You Have Loged in Successfully", data={"token" : access_token, "token_type": "bearer"})


#############################################################################################

def create_user(db: Session, user_data: ClientAccountModel):
    user_data.api_key = generateAPIKey()
    new_user = DB_Client_Users(**user_data.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def update_user(db: Session, user: DB_Client_Users, last_otp: str):
    user.last_otp = last_otp
    db.commit()
    return user
