import calendar
from app.models.respond.general import generalResponse
from sqlalchemy.orm import Session
from fastapi import Request, Depends, APIRouter, HTTPException, status
from app.models.schemas.attorney_account import AttorneyFilter, ReviewsResponse, AttorneyDetailsResponse
from app.utils.average import getAverage
from app.utils.database import get_db
from app.models.database.attorney.db_attorney_user import DB_Attorney_Users
from app.models.database.attorney.db_attorney_review import DB_Attorney_Review
from app.models.database.customer.db_customer_user import DB_Customer_Users
from app.models.database.db_category import DB_Categories
from app.models.database.db_country import DB_Countries
from app.models.database.db_appointment import DB_Appointments, AppointmentsState
from app.utils.validation import validateLanguageHeader
from datetime import datetime, timedelta

router = APIRouter(
    prefix="/attorney-details",
    tags=["Account"]
)

@router.get("/")
async def get_attorney_account_details(id :int ,request: Request, db: Session = Depends(get_db)):
    language = validateLanguageHeader(request).language
    
    attorney_info = get_attorney_info(db, id, language)
                     
    if attorney_info == None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="profile was not found")
   
    list_of_reviews = get_reviews(db, attorney_info.id, language)
    rate_avg = getAverage([review.stars for review in list_of_reviews])

    attorney_details_response = create_attorney_details_response(attorney_info, rate_avg, list_of_reviews)
    
    return generalResponse(message="Profile return successfully", data= attorney_details_response)

@router.get("/attorney-available")
def get_nearest_attorney_available(catId :int, request: Request, db: Session = Depends(get_db)):
    language = validateLanguageHeader(request).language
    attorneys = fetch_attorneys(db, catId, language)
   
    if not attorneys:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No profiles under this category")
    
    list_of_attorneys: list[AttorneyFilter] = []
    hour = 0
    
    while len(list_of_attorneys) <= 7:
        hour = hour + 1
        booking_time = (datetime.now() + timedelta(hours=hour))
        currentTimeDayName = calendar.day_name[booking_time.weekday()]

        for attorney in attorneys:
            if (booking_time).hour in get_working_hours(attorney,currentTimeDayName):
                obj = AttorneyFilter(id = attorney.id, 
                                suffixe_name = attorney.suffixe_name, 
                                first_name = attorney.first_name, 
                                last_name = attorney.last_name, 
                                gender = attorney.gender, 
                                profile_img = attorney.profile_img, 
                                hour_rate = attorney.hour_rate,
                                currency = attorney.currency,
                                country_code = attorney.country_code,
                                currency_code = attorney.currency_code,
                                languages = attorney.speaking_language,
                                country_name = attorney.country_name,
                                country_flag = attorney.flag_image,
                                date = booking_time.strftime('%Y-%m-%d'), 
                                day = currentTimeDayName,
                                working_hours = get_working_hours(attorney,currentTimeDayName),                             
                                number_of_reviewers = 0,
                                rate = 0)
                list_of_attorneys.append(obj)

        for attorney in list_of_attorneys:
            # check if attorney avaliable in this time
            if (booking_time).hour in attorney.working_hours:
                query_of_reservations = db.query(DB_Appointments.attorney_id, DB_Appointments.date_from, DB_Appointments.date_to, DB_Appointments.state
                            ).filter(
                                DB_Appointments.attorney_id == attorney.id, 
                                DB_Appointments.state == AppointmentsState.active
                            ).all()  
                # check if attorney dont have any other appointment in this time
                if (query_of_reservations != []):
                    for reservations in query_of_reservations:
                        if reservations["date_from"] <= booking_time <= reservations["date_to"]:
                            list_of_attorneys.remove(attorney)

    indexOfRating = 0
    for attorney in list_of_attorneys:
        review_query = db.query(DB_Attorney_Review.id, DB_Attorney_Review.customers_id, DB_Attorney_Review.attorney_id, DB_Attorney_Review.stars, 
                             ).filter(DB_Attorney_Review.attorney_id == attorney.id).all()
            
        list_of_attorneys[indexOfRating].rate = getAverage([review.stars for review in review_query])
        list_of_attorneys[indexOfRating].number_of_reviewers = len(review_query)

        indexOfRating = indexOfRating + 1

    return generalResponse(message="Profiles return successfully", data=list_of_attorneys)
           
#############################################################################################

def get_attorney_info(db, attorney_id, language):
    
    country_name_column = DB_Countries.name_arabic if language == "ar" else DB_Countries.name_english
    country_currency_column = DB_Countries.currency_arabic if language == "ar" else DB_Countries.currency_english
    category_name_column = DB_Categories.name_arabic if language == "ar" else DB_Categories.name_english

    return db.query(DB_Attorney_Users.id, 
                        DB_Attorney_Users.suffixe_name, 
                        DB_Attorney_Users.first_name, 
                        DB_Attorney_Users.last_name, 
                        DB_Attorney_Users.gender,
                        DB_Attorney_Users.bio,
                        DB_Attorney_Users.speaking_language, 
                        DB_Attorney_Users.hour_rate, 
                        DB_Attorney_Users.working_hours_saturday, 
                        DB_Attorney_Users.working_hours_sunday,
                        DB_Attorney_Users.working_hours_monday, 
                        DB_Attorney_Users.working_hours_tuesday, 
                    DB_Attorney_Users.working_hours_wednesday, 
                    DB_Attorney_Users.working_hours_thursday, 
                    DB_Attorney_Users.working_hours_friday,
                    DB_Attorney_Users.free_call, 
                    DB_Attorney_Users.profile_img, 
                    DB_Attorney_Users.date_of_birth, 
                    DB_Attorney_Users.experience_since,
                    DB_Attorney_Users.country_id, 
                    DB_Categories.id.label("category_ID"),
                    category_name_column.label("category_name"),
                    country_name_column.label("country_name"),
                    country_currency_column.label("currency"),
                    DB_Countries.flag_image,
                    DB_Countries.country_code, 
                    DB_Countries.currency_code
                    ).join(DB_Categories, DB_Categories.id == DB_Attorney_Users.category_id, isouter=True
                    ).join(DB_Countries, DB_Countries.id == DB_Attorney_Users.country_id, isouter=True
                    ).filter(DB_Attorney_Users.id == attorney_id, 
                             DB_Attorney_Users.blocked == False, 
                             DB_Attorney_Users.published == True).first()

def get_reviews(db, attorney_id, language):
    review_query = db.query(DB_Attorney_Review.id,
                            DB_Attorney_Review.customers_id,
                            DB_Attorney_Review.attorney_id, 
                            DB_Attorney_Review.stars, 
                            DB_Attorney_Review.comment, 
                            DB_Attorney_Review.attorney_response, 
                            DB_Attorney_Review.created_at,
                            DB_Customer_Users.profile_img,
                            DB_Customer_Users.first_name, 
                            DB_Customer_Users.last_name,
                            DB_Countries.flag_image
                            ).join(
                                DB_Customer_Users, DB_Customer_Users.id == DB_Attorney_Review.customers_id, isouter=True
                            ).join(
                                DB_Countries, DB_Countries.id == DB_Customer_Users.country_id, isouter=True
                            ).filter(
                                DB_Attorney_Review.attorney_id == attorney_id).all()
                            
    list_of_reviews: list[ReviewsResponse] = []      
    for review in review_query:
        list_of_reviews.append(ReviewsResponse(id=review.id, 
                                            attorney_id=review.attorney_id,
                                            customer_first_name = review.first_name, 
                                                customer_last_name = review.last_name, 
                                                customer_profile_img = review.profile_img, 
                                                stars = review.stars, 
                                                comments = review.comment,
                                                attorney_response = review.attorney_response,
                                                flag_image = review.flag_image,
                                                created_at = review.created_at))
    return list_of_reviews

def create_attorney_details_response(attorney_info, rate_avg, list_of_reviews):
 return AttorneyDetailsResponse(id = attorney_info.id,
                            suffixe_name = attorney_info.suffixe_name, 
                            first_name = attorney_info.first_name, 
                            last_name = attorney_info.last_name, 
                            gender = attorney_info.gender, 
                            bio = attorney_info.bio, 
                            speaking_language = attorney_info.speaking_language, 
                            hour_rate = attorney_info.hour_rate, 
                            free_call = attorney_info.free_call,
                            currency = attorney_info.currency,
                            currency_code = attorney_info.currency_code,
                            country_code = attorney_info.country_code,
                            profile_img = attorney_info.profile_img, 
                            date_of_birth = attorney_info.date_of_birth, 
                            experience_since = attorney_info.experience_since, 
                            category_name = attorney_info.category_name,
                            category_id = attorney_info.category_ID,
                            country = attorney_info.country_name,
                            country_flag = attorney_info.flag_image, 
                            total_rate = rate_avg, 
                            working_hours_saturday = attorney_info.working_hours_saturday,
                            working_hours_sunday = attorney_info.working_hours_sunday,
                            working_hours_monday = attorney_info.working_hours_monday,
                            working_hours_tuesday = attorney_info.working_hours_tuesday,
                            working_hours_wednesday = attorney_info.working_hours_wednesday,
                            working_hours_thursday = attorney_info.working_hours_thursday,
                            working_hours_friday = attorney_info.working_hours_friday,
                            reviews = list_of_reviews
                            )
 
def fetch_attorneys(db, catId, language):
    country_name_column = DB_Countries.name_arabic if language == "ar" else DB_Countries.name_english
    country_currency_column = DB_Countries.currency_arabic if language == "ar" else DB_Countries.currency_english

    return db.query(DB_Attorney_Users.id,
                    DB_Attorney_Users.suffixe_name,
                    DB_Attorney_Users.first_name,
                    DB_Attorney_Users.last_name,
                    DB_Attorney_Users.gender,
                    DB_Attorney_Users.profile_img,
                    DB_Attorney_Users.hour_rate,
                    DB_Attorney_Users.bio,
                    DB_Attorney_Users.speaking_language,
                    DB_Attorney_Users.working_hours_saturday, 
                    DB_Attorney_Users.working_hours_sunday,
                    DB_Attorney_Users.working_hours_monday, 
                    DB_Attorney_Users.working_hours_tuesday, 
                    DB_Attorney_Users.working_hours_wednesday, 
                    DB_Attorney_Users.working_hours_thursday, 
                    DB_Attorney_Users.working_hours_friday,
                    country_name_column.label("country_name"),
                    country_currency_column.label("currency"),
                    DB_Countries.flag_image,
                    DB_Countries.country_code, 
                    DB_Countries.currency_code,
                    ).join(
                    DB_Countries, DB_Countries.id == DB_Attorney_Users.country_id, isouter=True
                    ).filter(
                        DB_Attorney_Users.category_id == catId, 
                        DB_Attorney_Users.blocked == False, 
                        DB_Attorney_Users.published == True
                        ).all()
                    
def get_working_hours(attorney, day):
    working_hours_mapping = {
        "Saturday": attorney.working_hours_saturday,
        "Sunday": attorney.working_hours_sunday,
        "Monday": attorney.working_hours_monday,
        "Tuesday": attorney.working_hours_tuesday,
        "Wednesday": attorney.working_hours_wednesday,
        "Thursday": attorney.working_hours_thursday,
        "Friday": attorney.working_hours_friday,
    }
    return working_hours_mapping.get(day)