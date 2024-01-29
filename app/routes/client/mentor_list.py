
from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from app.models.schemas.mentor_account import MentorObjForListResponse
from app.utils.average import getAverage
from app.utils.database import get_db
from app.utils.validation import validateLanguageHeader
from app.models.respond.general import generalResponse
from app.models.database.mentor.db_mentor_user import DB_Mentor_Users
from app.models.database.mentor.db_mentor_review import DB_Mentor_Review
from app.models.database.db_category import DB_Categories
from app.models.database.db_country import DB_Countries

router = APIRouter(
    prefix="/mentor-list",
    tags=["Mentor"]
)

@router.get("/")
async def get_accounts_depend_on_category_id(categories_id :int ,request: Request, db: Session = Depends(get_db)):
    myHeader = validateLanguageHeader(request)
    
    country_name_column = DB_Countries.name_arabic if myHeader.language == "ar" else DB_Countries.name_english
    country_currency_column = DB_Countries.currency_arabic if myHeader.language == "ar" else DB_Countries.currency_english
    category_name_column = DB_Categories.name_arabic if myHeader.language == "ar" else DB_Categories.name_english

    mentors = db.query(DB_Mentor_Users.id, 
                        DB_Mentor_Users.suffixe_name, 
                        DB_Mentor_Users.first_name, 
                        DB_Mentor_Users.last_name, 
                        DB_Mentor_Users.gender, 
                        DB_Mentor_Users.hour_rate, 
                        DB_Mentor_Users.speaking_language,
                        DB_Mentor_Users.profile_img, 
                        DB_Mentor_Users.experience_since,
                        country_name_column.label("country_name"), 
                        DB_Countries.flag_image,
                        country_currency_column.label("currency"),
                        category_name_column.label("category_name")
                        ).join(
                            DB_Categories, DB_Categories.id == DB_Mentor_Users.category_id, isouter=True
                        ).join(
                            DB_Countries, DB_Countries.id == DB_Mentor_Users.country_id, isouter=True
                        ).filter(
                            DB_Mentor_Users.category_id == categories_id,
                            DB_Mentor_Users.blocked == False,
                            DB_Mentor_Users.published == True
                        ).all()
    
    review_query = db.query(
        DB_Mentor_Review.mentor_id,
        DB_Mentor_Review.stars
    ).all()
    
    
    response_list = []
                
    for mentor in mentors:
        mentor_reviews = [review.stars for review in review_query if review.mentor_id == mentor.id]
        rate_avg = getAverage(mentor_reviews) if mentor_reviews else 0
        number_of_reviews = len(mentor_reviews)

        response_list.append(MentorObjForListResponse(
            id=mentor.id,
            category_name=mentor.country_name,
            suffixe_name=mentor.suffixe_name,
            first_name=mentor.first_name,
            last_name=mentor.last_name,
            rate=rate_avg,
            currency=mentor.currency,
            hour_rate=mentor.hour_rate,
            languages=mentor.speaking_language,
            country_name=mentor.country_name,
            country_flag=mentor.flag_image,
            number_of_reviewers=number_of_reviews,
            profile_img=mentor.profile_img
        ))
 
    return generalResponse(message="Mentors return successfully", data=response_list)