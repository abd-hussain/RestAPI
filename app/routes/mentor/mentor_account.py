from app.models.respond.general import generalResponse
from sqlalchemy.orm import Session
from fastapi import Request, Depends, APIRouter
from app.models.schemas.mentor.mentor_account import MentorDetailsResponse
from app.utils.database import get_db
from app.models.database.mentor.db_mentor_user import DB_Mentor_Users
from app.models.database.db_category import DB_Categories
from app.models.database.db_country import DB_Countries
from app.models.database.db_majors import DB_Majors
from app.utils.oauth2 import get_current_user
from app.utils.validation import validateLanguageHeader
from app.utils.generate import generateActvationCode


router = APIRouter(
    prefix="/mentor-account",
    tags=["Account"]
)

@router.get("/")
async def get_account(id :int , request: Request, db: Session = Depends(get_db), get_current_user: int = Depends(get_current_user)):
    myHeader = validateLanguageHeader(request)
    query = db.query(DB_Mentor_Users.id, DB_Mentor_Users.suffixe_name, 
                     DB_Mentor_Users.first_name, DB_Mentor_Users.last_name, DB_Mentor_Users.bio,
                    DB_Mentor_Users.speaking_language, DB_Mentor_Users.majors,
                    DB_Mentor_Users.class_min, DB_Mentor_Users.hour_rate_by_JD, DB_Mentor_Users.rate, 
                    DB_Mentor_Users.gender, DB_Mentor_Users.profile_img, DB_Mentor_Users.date_of_birth,
                    DB_Mentor_Users.country_id, DB_Categories.name_english.label("category_name"), 
                    DB_Countries.name_english.label("country"), DB_Countries.flag_image.label("country_flag")
                    ).join(DB_Categories, DB_Categories.id == DB_Mentor_Users.category_id, isouter=True).join(DB_Countries, DB_Countries.id == DB_Mentor_Users.country_id, isouter=True).filter(DB_Mentor_Users.id == id).first()
                     
    if query == None:
       return generalResponse(message="profile was not found", data=None)
   
    if (myHeader.language == "ar"):
        query = db.query(DB_Mentor_Users.id, DB_Mentor_Users.suffixe_name, 
                    DB_Mentor_Users.first_name, DB_Mentor_Users.last_name, DB_Mentor_Users.bio,
                    DB_Mentor_Users.speaking_language, DB_Mentor_Users.majors,
                    DB_Mentor_Users.class_min, DB_Mentor_Users.hour_rate_by_JD, DB_Mentor_Users.rate, 
                    DB_Mentor_Users.gender, DB_Mentor_Users.profile_img, DB_Mentor_Users.date_of_birth,
                    DB_Mentor_Users.country_id, DB_Categories.name_arabic.label("category_name"), 
                    DB_Countries.name_arabic.label("country"), DB_Countries.flag_image.label("country_flag")
                    ).join(DB_Categories, DB_Categories.id == DB_Mentor_Users.category_id, isouter=True).join(DB_Countries, DB_Countries.id == DB_Mentor_Users.country_id, isouter=True).filter(DB_Mentor_Users.id == id).first()


    majors_list = []
    major_query = db.query(DB_Majors.id, DB_Majors.category_id, DB_Majors.name_english, DB_Majors.name_arabic)
    
    for item in query["majors"]:
        if (myHeader.language == "ar"):
            ll = major_query[item]["name_arabic"]
        else:
            ll = major_query[item]["name_english"]
        majors_list.append(ll)
    
    mentor_dtails = MentorDetailsResponse(suffixe_name = query["suffixe_name"], 
                                          first_name = query["first_name"], 
                                          last_name = query["last_name"], 
                                          bio = query["bio"], 
                                          speaking_language = query["speaking_language"], 
                                          class_min = query["class_min"], 
                                          hour_rate_by_JD = query["hour_rate_by_JD"], 
                                          gender = query["gender"], 
                                          profile_img = query["profile_img"], 
                                          date_of_birth = query["date_of_birth"], 
                                          category_name = query["category_name"], 
                                          country = query["country"], 
                                          country_flag = query["country_flag"], 
                                          rate = query["rate"], 
                                          major = majors_list)
    
    return generalResponse(message="Profile return successfully", data= mentor_dtails)
    
   