from fastapi import Request, Depends ,APIRouter
from sqlalchemy.orm import Session
from app.utils.validation import validateLanguageHeader
from app.utils.database import get_db
from app.models.database.mentor.db_mentor_user import DB_Mentor_Users
from app.models.database.db_country import DB_Countries

from app.utils.oauth2 import get_current_user
from app.utils.validation import validateLanguageHeader
from app.models.respond.general import generalResponse

router = APIRouter(
    prefix="/mentor-account",
    tags=["Account"]
)

@router.get("/info")
async def get_account(request: Request, db: Session = Depends(get_db), get_current_user: int = Depends(get_current_user)):
    myHeader = validateLanguageHeader(request)
    query = db.query(DB_Mentor_Users.profile_img, DB_Mentor_Users.mobile_number, 
                     DB_Mentor_Users.suffixe_name, DB_Mentor_Users.date_of_birth, 
                     DB_Mentor_Users.first_name, DB_Mentor_Users.email, 
                     DB_Mentor_Users.last_name,DB_Mentor_Users.gender,
                     DB_Mentor_Users.speaking_language, DB_Mentor_Users.country_id, 
                     DB_Countries,
                     DB_Mentor_Users.referal_code,DB_Mentor_Users.id_img).join(DB_Countries, DB_Mentor_Users.country_id == DB_Countries.id, isouter=True)\
                         .filter(DB_Mentor_Users.id == get_current_user.user_id)

    if query.first() == None:
       return generalResponse(message="profile was not found", data=None)
    
    return generalResponse(message="Profile return successfully", data=query.first())

@router.delete("/delete")
async def delete_account(request: Request, db: Session = Depends(get_db), get_current_user: int = Depends(get_current_user)):
    myHeader = validateLanguageHeader(request)
    query = db.query(DB_Mentor_Users).filter(DB_Mentor_Users.id == get_current_user.user_id)

    if query.first() == None:
       return generalResponse(message="profile was not found", data=None)
   
    query.delete()
    db.commit()
    return generalResponse(message="Profile deleted successfully", data=None)