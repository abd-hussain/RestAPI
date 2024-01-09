from fastapi import Depends, APIRouter, HTTPException, status
from sqlalchemy.orm import Session
from app.utils.database import get_db
from app.models.database.mentor.db_mentor_user import DB_Mentor_Users, FreeCallTypes
from app.utils.oauth2 import get_current_user
from app.models.respond.general import generalResponse

router = APIRouter(
    prefix="/hour-rate",
    tags=["Account"]
)

@router.get("/freeCall")
async def get_free_call_type(db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):

    user = get_user_by_id(current_user.user_id, db)

    if not user:
        return not_found_response()

    return generalResponse(message="Free Call Type returned successfully", data=user.free_call)

@router.put("/freeCall")
async def update_free_call_type(type: str, db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
    user = get_user_by_id(current_user.user_id, db)
    if not user:
        return not_found_response()

    if type in FreeCallTypes.__members__:
        user.free_call = getattr(FreeCallTypes, type)
        db.commit()
    else:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Wrong Type")

    return generalResponse(message="Free Call Type updated successfully", data=None)

@router.get("/")
async def get_hour_rate_and_iban(db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):

    user = get_user_by_id(current_user.user_id, db)
    if not user:
        return not_found_response()

    return generalResponse(message="hour_rate & IBAN return successfully", data={"hour_rate": user.hour_rate, "iban": user.iban})

@router.put("/")
async def update_hour_rate_and_iban(hour_rate: str, iban: str,
                         db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
  
    user = get_user_by_id(current_user.user_id, db)
    if not user:
        return not_found_response()

    if hour_rate is not None:
        user.hour_rate = hour_rate
    if iban is not None:
        user.iban = iban
    db.commit()
        
    return generalResponse(message="Hour rate and IBAN updated successfully", data=None)


#############################################################################################

def get_user_by_id(user_id: int, db: Session):
    return db.query(DB_Mentor_Users).filter(DB_Mentor_Users.id == user_id).first()

def not_found_response():
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Profile was not found")

