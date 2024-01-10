import calendar
from app.models.respond.general import generalResponse
from sqlalchemy.orm import Session
from fastapi import Request, Depends, APIRouter, HTTPException, status
from app.models.schemas.mentor_account import MentorDetailsResponse, MentorFilter, ReviewsResponse
from app.utils.average import getAverage
from app.utils.database import get_db
from app.models.database.mentor.db_mentor_user import DB_Mentor_Users
from app.models.database.mentor.db_mentor_review import DB_Mentor_Review
from app.models.database.client.db_client_user import DB_Client_Users
from app.models.database.db_category import DB_Categories
from app.models.database.db_country import DB_Countries
from app.models.database.db_majors import DB_Majors
from app.models.database.db_appointment import DB_Appointments, AppointmentsState
from app.utils.validation import validateLanguageHeader
from datetime import datetime, timedelta

router = APIRouter(
    prefix="/mentors-details",
    tags=["Account"]
)



@router.get("/")
async def get_mentor_account_details(id :int ,request: Request, db: Session = Depends(get_db)):
    language = validateLanguageHeader(request).language
    
    mentor_info = get_mentor_info(db, id, language)
                     
    if mentor_info == None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="profile was not found")
   
    list_of_reviews = get_reviews(db, mentor_info.id, language)
    majors_list = get_majors_named(db, mentor_info.majors, language)
    rate_avg = getAverage([review.stars for review in list_of_reviews])

    mentor_details_response = create_mentor_details_response(mentor_info, majors_list, rate_avg, list_of_reviews)
    
    return generalResponse(message="Profile return successfully", data= mentor_details_response)

@router.get("/mentor-available")
def get_nearest_mentor_available(catId :int, request: Request, db: Session = Depends(get_db)):
    language = validateLanguageHeader(request).language
    # //TODO : this API not working as expected , i am still not sure , it need alot of testing and refactoring
    mentors = fetch_mentors(db, catId, language)
   
    if not mentors:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No profiles under this category")
    
    list_of_mentors: list[MentorFilter] = []
    hour = 0
    
    while hour < 48:
        booking_time = (datetime.utcnow() + timedelta(hours=hour))
        currentTimeDayName = calendar.day_name[booking_time.weekday()]
        for mentor in mentors:
            obj = MentorFilter(id = mentor.id, 
                                suffixe_name = mentor.suffixe_name, 
                                first_name = mentor.first_name, 
                                last_name = mentor.last_name, 
                                gender = mentor.gender, 
                                profile_img = mentor.profile_img, 
                                hour_rate = mentor.hour_rate,
                                bio = mentor.bio, 
                                currency = mentor.currency,
                                languages = mentor.speaking_language,
                                country_name = mentor.country_name,
                                country_flag = mentor.flag_image,
                                date = booking_time.strftime('%Y-%m-%d'), 
                                day = currentTimeDayName,
                                working_hours = get_working_hours(mentor,currentTimeDayName),                             
                                number_of_reviewers = 0,
                                rate = 0)
            
            
                
            list_of_mentors.append(obj)
 
        indexOfReservations = 0
        list_of_mentors_to_be_deleted: list[MentorFilter] = []
        for mentor in list_of_mentors:
            if (booking_time).hour in mentor.working_hours:
                list_of_mentors[indexOfReservations].hour = booking_time.hour 
                query_of_reservations = db.query(DB_Appointments.mentor_id, DB_Appointments.date_from, DB_Appointments.date_to, DB_Appointments.state
                            ).filter(
                                DB_Appointments.mentor_id == mentor.id, 
                                DB_Appointments.state == AppointmentsState.active
                            ).all()          
                if (query_of_reservations != []):
                    for reservations in query_of_reservations:
                        if reservations["date_from"] <= booking_time <= reservations["date_to"]:
                            list_of_mentors_to_be_deleted.append(mentor)
                      
                else:
                    list_of_mentors_to_be_deleted.append(mentor)
                
            indexOfReservations = indexOfReservations + 1

        for mentor in list_of_mentors_to_be_deleted:
            list_of_mentors.remove(mentor)

        indexOfRating = 0
        for mentor in list_of_mentors:
            review_query = db.query(DB_Mentor_Review.id, DB_Mentor_Review.client_id, DB_Mentor_Review.mentor_id, DB_Mentor_Review.stars, 
                             ).filter(DB_Mentor_Review.mentor_id == mentor.id).all()
            
            list_of_mentors[indexOfRating].rate = getAverage([review.stars for review in review_query])
            indexOfRating = indexOfRating + 1

        if list_of_mentors != []:
            
            respond_mentor = list_of_mentors[0]
            for mentor in list_of_mentors:
                if mentor.rate > respond_mentor.rate:
                    respond_mentor = mentor
            print(hour)
            return generalResponse(message="Profiles return successfully", data=respond_mentor)
        else:
            hour += 1
           
#############################################################################################

def get_mentor_info(db, mentor_id, language):
    
    country_name_column = DB_Countries.name_arabic if language == "ar" else DB_Countries.name_english
    country_currency_column = DB_Countries.currency_arabic if language == "ar" else DB_Countries.currency_english
    category_name_column = DB_Categories.name_arabic if language == "ar" else DB_Categories.name_english

    return db.query(DB_Mentor_Users.id, 
                        DB_Mentor_Users.suffixe_name, 
                        DB_Mentor_Users.first_name, 
                        DB_Mentor_Users.last_name, 
                        DB_Mentor_Users.gender,
                        DB_Mentor_Users.bio,
                        DB_Mentor_Users.speaking_language, 
                        DB_Mentor_Users.majors,
                        DB_Mentor_Users.hour_rate, 
                        DB_Mentor_Users.working_hours_saturday, 
                        DB_Mentor_Users.working_hours_sunday,
                        DB_Mentor_Users.working_hours_monday, 
                        DB_Mentor_Users.working_hours_tuesday, 
                    DB_Mentor_Users.working_hours_wednesday, 
                    DB_Mentor_Users.working_hours_thursday, 
                    DB_Mentor_Users.working_hours_friday,
                    DB_Mentor_Users.free_call, 
                    DB_Mentor_Users.profile_img, 
                    DB_Mentor_Users.date_of_birth, 
                    DB_Mentor_Users.experience_since,
                    DB_Mentor_Users.country_id, 
                    category_name_column.label("category_name"),
                    country_name_column.label("country_name"),
                    country_currency_column.label("currency"),
                    DB_Countries.flag_image
                    ).join(DB_Categories, DB_Categories.id == DB_Mentor_Users.category_id, isouter=True
                    ).join(DB_Countries, DB_Countries.id == DB_Mentor_Users.country_id, isouter=True
                    ).filter(DB_Mentor_Users.id == mentor_id, 
                             DB_Mentor_Users.blocked == False, 
                             DB_Mentor_Users.published == True).first()

def get_majors_named(db, mentor_info_majors, language):
    majors_list = []
    major_query = db.query(DB_Majors.id, DB_Majors.name_english, DB_Majors.name_arabic).all()
    for mentor_majors in mentor_info_majors:
        for majors in major_query:
            if majors.id == mentor_majors:
                majer_name = majors.name_arabic if language == "ar" else majors.name_english
                value = majer_name
                majors_list.append(value)
    return majors_list

def get_reviews(db, mentor_id, language):
    review_query = db.query(DB_Mentor_Review.id,
                            DB_Mentor_Review.client_id,
                            DB_Mentor_Review.mentor_id, 
                            DB_Mentor_Review.stars, 
                            DB_Mentor_Review.comment, 
                            DB_Mentor_Review.mentor_response, 
                            DB_Mentor_Review.created_at,
                            DB_Client_Users.profile_img,
                            DB_Client_Users.first_name, 
                            DB_Client_Users.last_name,
                            DB_Countries.flag_image
                            ).join(
                                DB_Client_Users, DB_Client_Users.id == DB_Mentor_Review.client_id, isouter=True
                            ).join(
                                DB_Countries, DB_Countries.id == DB_Client_Users.country_id, isouter=True
                            ).filter(
                                DB_Mentor_Review.mentor_id == mentor_id).all()
                            
    list_of_reviews: list[ReviewsResponse] = []      
    for review in review_query:
        list_of_reviews.append(ReviewsResponse(id=review.id, 
                                            mentor_id=review.mentor_id,
                                            client_first_name = review.first_name, 
                                                client_last_name = review.last_name, 
                                                client_profile_img = review.profile_img, 
                                                stars = review.stars, 
                                                comments = review.comment,
                                                mentor_response = review.mentor_response,
                                                flag_image = review.flag_image,
                                                created_at = review.created_at))
    return list_of_reviews

def create_mentor_details_response(mentor_info, majors_list, rate_avg, list_of_reviews):
 return MentorDetailsResponse(id = mentor_info.id,
                            suffixe_name = mentor_info.suffixe_name, 
                            first_name = mentor_info.first_name, 
                            last_name = mentor_info.last_name, 
                            gender = mentor_info.gender, 
                            bio = mentor_info.bio, 
                            speaking_language = mentor_info.speaking_language, 
                            major = majors_list,
                            hour_rate = mentor_info.hour_rate, 
                            free_call = mentor_info.free_call,
                            currency = mentor_info.currency,
                            profile_img = mentor_info.profile_img, 
                            date_of_birth = mentor_info.date_of_birth, 
                            experience_since = mentor_info.experience_since, 
                            category_name = mentor_info.category_name,
                            country = mentor_info.country_name,
                            country_flag = mentor_info.flag_image, 
                            total_rate = rate_avg, 
                            working_hours_saturday = mentor_info.working_hours_saturday,
                            working_hours_sunday = mentor_info.working_hours_sunday,
                            working_hours_monday = mentor_info.working_hours_monday,
                            working_hours_tuesday = mentor_info.working_hours_tuesday,
                            working_hours_wednesday = mentor_info.working_hours_wednesday,
                            working_hours_thursday = mentor_info.working_hours_thursday,
                            working_hours_friday = mentor_info.working_hours_friday,
                            reviews = list_of_reviews
                            )
 
def fetch_mentors(db, catId, language):
    country_name_column = DB_Countries.name_arabic if language == "ar" else DB_Countries.name_english
    country_currency_column = DB_Countries.currency_arabic if language == "ar" else DB_Countries.currency_english

    return db.query(DB_Mentor_Users.id,
                    DB_Mentor_Users.suffixe_name,
                    DB_Mentor_Users.first_name,
                    DB_Mentor_Users.last_name,
                    DB_Mentor_Users.gender,
                    DB_Mentor_Users.profile_img,
                    DB_Mentor_Users.hour_rate,
                    DB_Mentor_Users.bio,
                    DB_Mentor_Users.speaking_language,
                    DB_Mentor_Users.working_hours_saturday, 
                    DB_Mentor_Users.working_hours_sunday,
                    DB_Mentor_Users.working_hours_monday, 
                    DB_Mentor_Users.working_hours_tuesday, 
                    DB_Mentor_Users.working_hours_wednesday, 
                    DB_Mentor_Users.working_hours_thursday, 
                    DB_Mentor_Users.working_hours_friday,
                    country_name_column.label("country_name"),
                    country_currency_column.label("currency"),
                    DB_Countries.flag_image,
                    ).join(
                    DB_Countries, DB_Countries.id == DB_Mentor_Users.country_id, isouter=True
                    ).filter(DB_Mentor_Users.category_id == catId, 
                    DB_Mentor_Users.blocked == False, 
                    DB_Mentor_Users.published == True
                    ).all()
                    
def get_working_hours(mentor, day):
    working_hours_mapping = {
        "Saturday": mentor.working_hours_saturday,
        "Sunday": mentor.working_hours_sunday,
        "Monday": mentor.working_hours_monday,
        "Tuesday": mentor.working_hours_tuesday,
        "Wednesday": mentor.working_hours_wednesday,
        "Thursday": mentor.working_hours_thursday,
        "Friday": mentor.working_hours_friday,
    }
    return working_hours_mapping.get(day)