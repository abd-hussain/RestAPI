from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.models.database.admin.db_admin_user import DB_Admin_Users
from app.models.schemas.attorney_account import AuthData
from app.utils.database import get_db
from app.models.respond.general import generalResponse
from app.utils.oauth2 import create_access_token, verifyPassword
from app.utils.generate import generateAPIKey
from datetime import datetime

router = APIRouter(
    prefix="/adminauth",
    tags=["Auth"]
)

@router.post('/')
def login(payload: AuthData, db: Session = Depends(get_db)):
    
    admin_user = db.query(DB_Admin_Users).filter(DB_Admin_Users.email == payload.email)
    
    if not admin_user.first() and not admin_user.first():
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")
        
    if not verifyPassword(payload.password, admin_user.first().password):
        raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Admin Password")
    else:
        if admin_user.first().published == False:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN, detail="Admin Under Review")
                
        access_token = create_access_token(data={"api_key" : generateAPIKey(), "user_id" : admin_user.first().id})
        admin_user.last_usage = datetime.utcnow()
        db.commit()
        return generalResponse(message="Admin Logged In successfully", data={"Bearer": access_token, "user" : "admin"})