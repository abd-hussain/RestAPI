from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.models.database.mentor.db_mentor_user import DB_Mentor_Users
from app.models.schemas.mentor_account import MentorAuth
from app.utils.database import get_db
from app.models.respond.general import generalResponse
from app.utils.oauth2 import create_access_token, verifyPassword
from app.utils.generate import generateAPIKey
from datetime import datetime

router = APIRouter(    
    prefix="/mentor-auth",
    tags=["Authentication"]
)

@router.post('/')
def login(payload: MentorAuth, db: Session = Depends(get_db)):
    
    user = db.query(DB_Mentor_Users).filter(DB_Mentor_Users.email == payload.email).first()
    
    if not user or not verifyPassword(payload.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")
        
    if user.published == False:
         raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="User Under Review")

    if user.blocked == True:
         raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="User Blocked")
    
    access_token = create_access_token(data={"api_key" : generateAPIKey(), "user_id" : user.id})
    
    user.last_usage = datetime.utcnow().strftime("%d/%m/%Y %H:%M:%S")
    db.commit()
    
    return generalResponse(message="Logged In successfully", data=access_token)
