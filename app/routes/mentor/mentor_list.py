
from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from app.models.schemas.mentor.mentor_account import MentorObjForListResponse
from app.utils.average import getAverage
from app.utils.database import get_db
from app.utils.validation import validateLanguageHeader
from app.models.respond.general import generalResponse
from app.models.database.mentor.db_mentor_user import DB_Mentor_Users, DB_Mentor_Review
from app.models.database.db_category import DB_Categories
from sqlalchemy import func


router = APIRouter(
    prefix="/mentor-list",
    tags=["Mentor"]
)


@router.get("/")
async def get_accounts(categories_id :int ,request: Request, db: Session = Depends(get_db)):
    myHeader = validateLanguageHeader(request)
    query = db.query(DB_Mentor_Users.id, DB_Mentor_Users.suffixe_name, 
                     DB_Mentor_Users.first_name, DB_Mentor_Users.last_name, 
                     DB_Mentor_Users.class_min, DB_Mentor_Users.hour_rate_by_JD, 
                     DB_Mentor_Users.blocked, DB_Mentor_Users.profile_img,
                     DB_Categories.name_english, DB_Categories.name_arabic).join(DB_Categories, DB_Categories.id == DB_Mentor_Users.category_id, isouter=True)\
                    .filter(DB_Mentor_Users.category_id == categories_id).filter(DB_Mentor_Users.blocked == False).all()
    
    if query == []:
       return generalResponse(message="No Mentors Founded", data=None)
                                                                                               
    review_query =  db.query(DB_Mentor_Review.mentor_id, DB_Mentor_Review.stars).all()
                
    response_list =  []   
    for i in query:
        rate_avg = 0
        list_of_stars: list[float] = []             
        for review in review_query:
            if review["mentor_id"] == i["id"]:
                list_of_stars.append(review["stars"])
        rate_avg = getAverage(list_of_stars)   
        response_list.append(MentorObjForListResponse(id = i["id"], category_name = i["name_arabic"] if (myHeader.language == "ar") else  i["name_english"], 
                                             suffixe_name = i["suffixe_name"], first_name = i["first_name"], 
                                             last_name = i["last_name"], rate = rate_avg, 
                                             class_min = i["class_min"], hour_rate_by_JD = i["hour_rate_by_JD"], 
                                             profile_img = i["profile_img"]))
 
    return generalResponse(message="Mentors return successfully", data=response_list)