from fastapi import Request, Depends, status ,APIRouter, HTTPException, File, UploadFile, Form
from sqlalchemy.orm import Session
from app.utils.validation import validateLanguageHeader
from app.utils.database import get_db
from app.models.database.mentor.db_mentor_user import DB_Mentor_Users
from app.models.schemas.working_hours import WorkingHoursRequest
from app.models.database.db_event import DB_Events, EventState, DB_Events_Appointments
from app.models.respond.general import generalResponse
from app.models.schemas.home import MentorHomeResponse, Event
from app.models.schemas.story import StoryPayload
from app.utils.oauth2 import get_current_user
from sqlalchemy import func
from datetime import datetime
from app.utils.time import current_milli_time


router = APIRouter(
    prefix="/mentor-prop",
    tags=["Mentor-Properties"]
)


@router.get("/working_hours")
async def get_working_hours(request: Request, db: Session = Depends(get_db), get_current_user: int = Depends(get_current_user)):
    myHeader = validateLanguageHeader(request)
    
    query = db.query(DB_Mentor_Users.id, DB_Mentor_Users.working_hours_saturday, DB_Mentor_Users.working_hours_sunday,
                     DB_Mentor_Users.working_hours_monday, DB_Mentor_Users.working_hours_tuesday,
                      DB_Mentor_Users.working_hours_wednesday, DB_Mentor_Users.working_hours_thursday, DB_Mentor_Users.working_hours_friday,
                      ).filter(DB_Mentor_Users.id == get_current_user.user_id).first()
        
    return generalResponse(message="List of Working Hours", data= query)

@router.put("/working_hours")
async def update_working_hours(payload: WorkingHoursRequest, request: Request, db: Session = Depends(get_db), get_current_user: int = Depends(get_current_user)):
    myHeader = validateLanguageHeader(request)
    query = db.query(DB_Mentor_Users).filter(DB_Mentor_Users.id == get_current_user.user_id)

    if query.first() == None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid User")
    
    if payload.dayName == "saturday":
        query.update({"working_hours_saturday" : payload.working_hours}, synchronize_session=False)
    elif payload.dayName == "sunday":
        query.update({"working_hours_sunday" : payload.working_hours}, synchronize_session=False)
    elif payload.dayName == "monday":
        query.update({"working_hours_monday" : payload.working_hours}, synchronize_session=False)
    elif payload.dayName == "tuesday":
        query.update({"working_hours_tuesday" : payload.working_hours}, synchronize_session=False)
    elif payload.dayName == "wednesday":
        query.update({"working_hours_wednesday" : payload.working_hours}, synchronize_session=False)
    elif payload.dayName == "thursday":
        query.update({"working_hours_thursday" : payload.working_hours}, synchronize_session=False)
    elif payload.dayName == "friday":
        query.update({"working_hours_friday" : payload.working_hours}, synchronize_session=False)
    else:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"day name is wrong")
        
    db.commit()
    
    return generalResponse(message="Working Hours updated successfully", data=None)
    