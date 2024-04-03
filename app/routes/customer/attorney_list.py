
from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from app.models.schemas.attorney_account import AttorneyObjForListResponse
from app.utils.average import getAverage
from app.utils.database import get_db
from app.utils.validation import validateLanguageHeader
from app.models.respond.general import generalResponse
from app.models.database.attorney.db_attorney_user import DB_Attorney_Users
from app.models.database.attorney.db_attorney_review import DB_Attorney_Review
from app.models.database.db_category import DB_Categories
from app.models.database.db_country import DB_Countries

router = APIRouter(
    prefix="/attorney-list",
    tags=["Attorney"]
)

@router.get("/")
async def get_accounts_depend_on_category_id(categories_id :int ,request: Request, db: Session = Depends(get_db)):
    myHeader = validateLanguageHeader(request)
    
    country_name_column = DB_Countries.name_arabic if myHeader.language == "ar" else DB_Countries.name_english
    country_currency_column = DB_Countries.currency_arabic if myHeader.language == "ar" else DB_Countries.currency_english
    category_name_column = DB_Categories.name_arabic if myHeader.language == "ar" else DB_Categories.name_english

    attorneys = db.query(DB_Attorney_Users.id, 
                        DB_Attorney_Users.suffixe_name, 
                        DB_Attorney_Users.first_name, 
                        DB_Attorney_Users.last_name, 
                        DB_Attorney_Users.gender, 
                        DB_Attorney_Users.hour_rate, 
                        DB_Attorney_Users.speaking_language,
                        DB_Attorney_Users.profile_img, 
                        DB_Attorney_Users.experience_since,
                        country_name_column.label("country_name"), 
                        DB_Countries.flag_image,
                        country_currency_column.label("currency"),
                        category_name_column.label("category_name")
                        ).join(
                            DB_Categories, DB_Categories.id == DB_Attorney_Users.category_id, isouter=True
                        ).join(
                            DB_Countries, DB_Countries.id == DB_Attorney_Users.country_id, isouter=True
                        ).filter(
                            DB_Attorney_Users.category_id == categories_id,
                            DB_Attorney_Users.blocked == False,
                            DB_Attorney_Users.published == True
                        ).all()
    
    review_query = db.query(
        DB_Attorney_Review.attorney_id,
        DB_Attorney_Review.stars
    ).all()
    
    
    response_list = []
                
    for attorney in attorneys:
        attorney_reviews = [review.stars for review in review_query if review.attorney_id == attorney.id]
        rate_avg = getAverage(attorney_reviews) if attorney_reviews else 0
        number_of_reviews = len(attorney_reviews)

        response_list.append(AttorneyObjForListResponse(
            id=attorney.id,
            category_name=attorney.country_name,
            suffixe_name=attorney.suffixe_name,
            first_name=attorney.first_name,
            last_name=attorney.last_name,
            rate=rate_avg,
            gender=attorney.gender,
            currency=attorney.currency,
            hour_rate=attorney.hour_rate,
            experience_since=attorney.experience_since,
            languages=attorney.speaking_language,
            country_name=attorney.country_name,
            country_flag=attorney.flag_image,
            number_of_reviewers=number_of_reviews,
            profile_img=attorney.profile_img
        ))
 
    return generalResponse(message="attorneys return successfully", data=response_list)