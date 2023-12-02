from fastapi import Request, Depends, APIRouter
from app.utils.database import get_db
from sqlalchemy.orm import Session
from typing import Optional
from app.utils.oauth2 import get_current_user
from app.utils.validation import validateLanguageHeader
from app.models.database.db_notifications import DB_Notifications
from app.models.respond.general import generalResponse
from app.models.database.mentor.db_mentor_user import DB_Mentor_Users

router = APIRouter(
    prefix="/notifications",
    tags=["Notifications"]
)

@router.put("/mentor-register-token")
async def update_push_notification_token(token: str, request: Request, db: Session = Depends(get_db), get_current_user: int = Depends(get_current_user)):
    myHeader = validateLanguageHeader(request)
    query = db.query(DB_Mentor_Users).filter(DB_Mentor_Users.id == get_current_user.user_id)
    query.update({"push_token" : token}, synchronize_session=False)
    db.commit()
    return generalResponse(message="Profile updated successfully", data=query.first())

@router.get("/mentor")
async def get_Notifications_for_mentor(request: Request, db: Session = Depends(get_db), get_current_user: int = Depends(get_current_user), limit: int = 10, skip: int = 0, search: Optional[str] = ""):
    myHeader = validateLanguageHeader(request)
   
    data = db.query(DB_Notifications.id, DB_Notifications.title_english.label(
        "title"), DB_Notifications.content_english.label(
        "content"), DB_Notifications.readed, DB_Notifications.created_at).filter(DB_Notifications.mentor_owner_id == get_current_user.user_id).filter(DB_Notifications.title_english.contains(search)).limit(limit).offset(skip).all()
    if (myHeader.language == "ar"):
        data = db.query(DB_Notifications.id, DB_Notifications.title_arabic.label(
            "title"), DB_Notifications.content_arabic.label(
            "content"), DB_Notifications.readed, DB_Notifications.created_at).filter(DB_Notifications.mentor_owner_id == get_current_user.user_id).filter(DB_Notifications.title_arabic.contains(search)).limit(limit).offset(skip).all()
    return generalResponse(message="list of notifications return successfully", data=data)