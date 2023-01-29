from fastapi import Request, Depends, APIRouter, HTTPException, status
from sqlalchemy.orm import Session
from app.utils.database import get_db
from app.utils.validation import validateLanguageHeader
from app.models.database.db_event import DB_Events, DB_Events_Appointments, EventState
from app.models.respond.general import generalResponse
from app.models.database.mentor.db_mentor_user import DB_Mentor_Users
from app.models.database.db_category import DB_Categories
from app.utils.oauth2 import get_current_user

router = APIRouter(
    prefix="/messages",
    tags=["Messages"]
)