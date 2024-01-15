from fastapi import Depends, Request, APIRouter, HTTPException, status
from sqlalchemy.orm import Session
from app.utils.database import get_db
from app.models.database.mentor.db_mentor_user import DB_Mentor_Users, FreeCallTypes
from app.utils.oauth2 import get_current_user
from app.models.respond.general import generalResponse
from app.utils.validation import validateLanguageHeader
from app.models.database.db_country import DB_Countries

router = APIRouter(
    prefix="/hour-rate",
    tags=["Account"]
)

@router.get("/")
async def get_hour_rate_and_iban(request: Request, db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
    myHeader = validateLanguageHeader(request)

    country_currency = DB_Countries.currency_arabic if myHeader.language == "ar" else DB_Countries.currency_english

    user = db.query(DB_Mentor_Users.id, country_currency.label("currency"),
                    DB_Mentor_Users.hour_rate, DB_Mentor_Users.iban,
                    DB_Mentor_Users.free_call,
                    ).join(DB_Countries, DB_Countries.id == DB_Mentor_Users.country_id, isouter=True
                                           ).filter(DB_Mentor_Users.id == current_user.user_id).first()
    if not user:
        return not_found_response()

    return generalResponse(message="hour_rate & IBAN return successfully", 
                           data={"hour_rate": user.hour_rate, 
                                 "currency": user.currency, 
                                 "free_call": user.free_call, 
                                 "iban": user.iban})

@router.put("/")
async def update_hour_rate_and_iban(hour_rate: str, iban: str, free_type : int,
                         db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
  
    user = db.query(DB_Mentor_Users).filter(DB_Mentor_Users.id == current_user.user_id).first()
    if not user:
        return not_found_response()

    if hour_rate is not None:
        user.hour_rate = hour_rate
    if iban is not None:
        user.iban = iban
    if free_type is not None:
        if free_type == 1:
            user.free_call = FreeCallTypes.free_disabled
        elif free_type == 2:
            user.free_call = FreeCallTypes.free_15_min
        elif free_type == 3:
            user.free_call = FreeCallTypes.free_15_min_with_promocode
        else: 
            user.free_call = None
            
    # //TODO Send Push Notificaitin with promo code
            
    db.commit()
        
    return generalResponse(message="Hour rate and IBAN updated successfully", data=None)


#############################################################################################

def not_found_response():
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Profile was not found")

