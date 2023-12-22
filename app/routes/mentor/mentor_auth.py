from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.models.database.mentor.db_mentor_user import DB_Mentor_Users
from app.models.schemas.mentor_account import MentorAuth, MentorForgotPassword
from app.utils.send_email import send_email
from app.utils.database import get_db
from app.models.respond import general
from app.utils.oauth2 import create_access_token, verifyPassword

router = APIRouter(    
    prefix="/mentor-auth",
    tags=["Authentication"]
)

@router.post('/login')
def login(payload: MentorAuth, db: Session = Depends(get_db)):
    
    user = db.query(DB_Mentor_Users).filter(DB_Mentor_Users.email == payload.email).first()
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")

    if not verifyPassword(payload.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")
    access_token = create_access_token(data={"api_key" : "079", "user_id" : user.id})
    return general.generalResponse(message= "Logged In successfully", data=access_token)
        
@router.post('/forgotpassword')
def forgotPassword(payload: MentorForgotPassword, db: Session = Depends(get_db)):
    user = db.query(DB_Mentor_Users).filter(DB_Mentor_Users.email == payload.email).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")
    send_email(payload.email, user.password)
    return general.generalResponse(message= "Email send successfully", data=None)
