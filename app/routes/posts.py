
from fastapi import Request, Depends, APIRouter, status, HTTPException
from sqlalchemy.orm import Session
from app.models.database.db_versions import DB_Versions
from app.models.schemas.leads import ListLeads
from app.models.schemas.notifications import Notifications
from app.models.database.db_terms import DB_Terms
from app.models.database.db_leads import DB_Leads
from app.models.database.client.db_client_user import DB_Client_Users
from app.models.database.mentor.db_mentor_user import DB_Mentor_Users
from app.models.database.db_notifications import DB_Notifications
from app.models.respond.general import generalResponse
from app.utils.database import get_db
from app.utils.generate import generateRequestId
from app.utils.oauth2 import get_current_user
from app.utils.validation import validateLanguageHeader
from typing import Optional

router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)

@router.get("/")
async def get_Posts(request: Request, db: Session = Depends(get_db), get_current_user: int = Depends(get_current_user), limit: int = 10, skip: int = 0, search: Optional[str] = ""):
    myHeader = validateLanguageHeader(request)
    
    data = db.query(DB_Notifications.id, DB_Notifications.title_english.label(
        "title"), DB_Notifications.content_english.label(
        "content")).filter(DB_Notifications.receiver_id == id).filter(DB_Notifications.title_english.contains(search)).limit(limit).offset(skip).all()
    if (myHeader.language == "ar"):
        data = db.query(DB_Notifications.id, DB_Notifications.title_arabic.label(
            "title"), DB_Notifications.content_arabic.label(
            "content")).filter(DB_Notifications.receiver_id == id).filter(DB_Notifications.title_arabic.contains(search)).limit(limit).offset(skip).all()
    return generalResponse(message="list of notifications return successfully", data=data)
