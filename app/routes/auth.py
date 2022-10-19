from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.models.database import db_user
from app.models.schemas.account import AccountModel, AccountVerifyModel
from app.utils.generate import generateAPIKey, generateOTP, generateRequestId
from app.utils.database.database import get_db
from app.models.respond import general, login
from app.utils.validation import verifyKey
from app.utils.oauth2 import create_access_token

router = APIRouter(    
    prefix="/auth",
    tags=["Authentication"]
)

@router.post('/', response_model=login.LoginResponse)
def authentication(payload: AccountModel, db: Session =  Depends(get_db)):
    query = db.query(db_user.DB_Users).filter(db_user.DB_Users.mobile_number == payload.mobile_number)
    payload.last_otp = generateOTP()
    
    if query.first() == None:
        payload.api_key = generateAPIKey()
        obj = db_user.Accounts(**payload.dict())
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return general.generalResponse(message= "successfully created account", data=obj)
    
    query.update({"last_otp" : payload.last_otp}, synchronize_session=False)
    db.commit()
    return general.generalResponse(message= "OTP Sended successfully", data=query.first())

@router.post('-debug', response_model=login.LoginDebugResponse)
def authentication(payload: AccountModel, db: Session =  Depends(get_db)):
    query = db.query(db_user.DB_Users).filter(db_user.DB_Users.mobile_number == payload.mobile_number)
    payload.last_otp = generateOTP()
    
    if query.first() == None:
        payload.api_key = generateAPIKey()
        obj = db_user.DB_Users(**payload.dict())
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return general.generalResponse(message= "successfully created account", data=obj)
    
    query.update({"last_otp" : payload.last_otp}, synchronize_session=False)
    db.commit()
    return general.generalResponse(message= "OTP Sended successfully", data=query.first())

@router.post('-verify/')
def verify_otp(payload: AccountVerifyModel, db: Session =  Depends(get_db)):
    query = db.query(db_user.DB_Users).filter(db_user.DB_Users.mobile_number == payload.mobile_number)

    if query.first() == None:
      raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail={"message": f"Mobile number is not valid", "request_id": generateRequestId()})
    
    if not verifyKey(payload.otp, query.first().last_otp):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail={"message": f"OTP is not valid", "request_id": generateRequestId()})

    if not verifyKey(payload.api_key, query.first().api_key):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail={"message": f"API Key is not valid", "request_id": generateRequestId()})
    
    access_token = create_access_token(data={"api_key" : payload.api_key, "user_id" : payload.user_id})
    
    return general.generalResponse(message= "You Have Loged in Successfully", data={"token" : access_token, "token_type": "bearer"})