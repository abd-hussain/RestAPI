
from fastapi import APIRouter, Depends, status, HTTPException, Request
from sqlalchemy.orm import Session
from app.models.schemas.mentor.mentor_account import MentorListResponse
from app.utils.database import get_db
from app.utils.validation import validateLanguageHeader
from app.models.respond.general import generalResponse
from app.models.database.mentor.db_mentor_user import DB_Mentor_Users
from app.models.database.db_category import DB_Categories


router = APIRouter(
    prefix="/mentor-list",
    tags=["Mentor"]
)


@router.get("/")
async def get_accounts(categories_id :int ,request: Request, db: Session = Depends(get_db)):
    myHeader = validateLanguageHeader(request)
    query = db.query(DB_Mentor_Users.id, DB_Mentor_Users.suffixe_name, 
                     DB_Mentor_Users.first_name, DB_Mentor_Users.last_name, 
                     DB_Mentor_Users.class_min, DB_Mentor_Users.hour_rate_by_JD, DB_Mentor_Users.rate, DB_Mentor_Users.gender, 
                     DB_Mentor_Users.blocked, DB_Mentor_Users.profile_img, DB_Mentor_Users.date_of_birth, 
                     DB_Mentor_Users.country_id, DB_Categories.name_english.label("category_name")).join(DB_Categories, 
                                                                                               DB_Categories.id == DB_Mentor_Users.category_id, isouter=True).filter(DB_Mentor_Users.category_id == categories_id).filter(DB_Mentor_Users.blocked == False).all()
    
    if query == []:
       return generalResponse(message="No Mentors Founded", data=None)
   
    if (myHeader.language == "ar"):
         query = db.query(DB_Mentor_Users.id, DB_Mentor_Users.suffixe_name, 
                     DB_Mentor_Users.first_name, DB_Mentor_Users.last_name, 
                     DB_Mentor_Users.class_min, DB_Mentor_Users.hour_rate_by_JD, DB_Mentor_Users.rate, DB_Mentor_Users.gender, 
                     DB_Mentor_Users.blocked, DB_Mentor_Users.profile_img, DB_Mentor_Users.date_of_birth, 
                     DB_Mentor_Users.country_id, DB_Categories.name_arabic.label("category_name")).join(DB_Categories, 
                                                                                               DB_Categories.id == DB_Mentor_Users.category_id, isouter=True).filter(DB_Mentor_Users.category_id == categories_id).filter(DB_Mentor_Users.blocked == False).all()
    

    obj = MentorListResponse(list = query)

    return generalResponse(message="Mentors return successfully", data=obj.list)