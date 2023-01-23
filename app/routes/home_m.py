from fastapi import Request, Depends, status ,APIRouter, HTTPException
from sqlalchemy.orm import Session
from app.utils.validation import validateLanguageHeader
from app.utils.database import get_db
from app.models.database.db_client_banners import DB_Client_Banners
from app.models.database.db_story import DB_Stories, DB_StoryReports
from app.models.database.db_event import DB_Events, EventState, DB_EventReports, DB_Events_Appointments
from app.models.database.db_tips import DB_Tips, DB_TipsQuestions
from app.models.respond.general import generalResponse
from app.models.schemas.home import HomeResponse, Story, Event
from app.utils.oauth2 import get_current_user
from sqlalchemy import func
from datetime import datetime

router = APIRouter(
    prefix="/home_m",
    tags=["Home"]
)