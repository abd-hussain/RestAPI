from fastapi import Depends ,APIRouter, HTTPException, status
from sqlalchemy.orm import Session
from app.utils.database import get_db
from app.models.database.mentor.db_mentor_user import DB_Mentor_Users
from app.models.schemas.mentor_account import MentorChangePassword

from app.utils.oauth2 import get_current_user
from app.models.respond.general import generalResponse
from app.utils.oauth2 import verifyPassword, hashingPassword

router = APIRouter(
    prefix="/mentor-settings",
    tags=["Account"]
)

@router.get("/hour-rate")
async def get_hourRate(db: Session = Depends(get_db), get_current_user: int = Depends(get_current_user)):

    query = db.query(DB_Mentor_Users.hour_rate).filter(DB_Mentor_Users.id == get_current_user.user_id).first()

    if query == None:
       return generalResponse(message="profile was not found", data=None)

    return generalResponse(message="hour_rate return successfully", data=query)

@router.put("/hour-rate")
async def update_hourRate(rate: str,
                         db: Session = Depends(get_db), get_current_user: int = Depends(get_current_user)):
  
    query = db.query(DB_Mentor_Users).filter(DB_Mentor_Users.id == get_current_user.user_id)

    if rate != None:
        query.update({"hour_rate" : rate}, synchronize_session=False)
        db.commit()
        
    return generalResponse(message= "Change hour_rate successfully", data=None)

@router.put("/change-password")
async def update_password(payload: MentorChangePassword,
                         db: Session = Depends(get_db), get_current_user: int = Depends(get_current_user)):
  
    query = db.query(DB_Mentor_Users).filter(DB_Mentor_Users.id == get_current_user.user_id)

    if not verifyPassword(payload.oldpassword, query.first().password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")
    if payload.newpassword != None:
        query.update({"password" : hashingPassword(payload.newpassword)}, synchronize_session=False)
        db.commit()
        
    return generalResponse(message= "Change Password successfully", data=None)

@router.delete("/delete")
async def delete_account(db: Session = Depends(get_db), get_current_user: int = Depends(get_current_user)):
    query = db.query(DB_Mentor_Users).filter(DB_Mentor_Users.id == get_current_user.user_id)

    if query.first() == None:
       return generalResponse(message="profile was not found", data=None)
   
    query.delete()
    db.commit()
    return generalResponse(message="Profile deleted successfully", data=None)