from fastapi import Request, Depends, status, APIRouter, HTTPException
from sqlalchemy.orm import Session
from app.utils.database import get_db
from app.models.database.attorney.db_attorney_user import DB_Attorney_Users
from app.models.schemas.working_hours import WorkingHoursRequest
from app.models.respond.general import generalResponse
from app.utils.oauth2 import get_current_user

router = APIRouter(
    prefix="/working_hours",
    tags=["Attorney"]
)

@router.get("/")
async def get_working_hours(db: Session = Depends(get_db), get_current_user: int = Depends(get_current_user)):
    
    query = db.query(DB_Attorney_Users.working_hours_saturday, 
                        DB_Attorney_Users.working_hours_sunday,
                        DB_Attorney_Users.working_hours_monday,
                        DB_Attorney_Users.working_hours_tuesday,
                        DB_Attorney_Users.working_hours_wednesday, 
                        DB_Attorney_Users.working_hours_thursday, 
                        DB_Attorney_Users.working_hours_friday,
                            ).filter(DB_Attorney_Users.id == get_current_user.user_id).first()
        
    return generalResponse(message="List of Working Hours", data= query)

@router.put("/")
async def update_working_hours(payload: WorkingHoursRequest, db: Session = Depends(get_db), 
                               get_current_user: int = Depends(get_current_user)):
    
    working_hours_field = f"working_hours_{payload.dayName.lower()}"
    query = db.query(DB_Attorney_Users).filter(DB_Attorney_Users.id == get_current_user.user_id)

    user = query.first()
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid User")
    
    if hasattr(user, working_hours_field):
        query.update({working_hours_field: payload.working_hours}, synchronize_session=False)
        db.commit()
        return generalResponse(message="Working Hours updated successfully", data=None)
    else:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid day name")
    