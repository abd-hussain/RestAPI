from datetime import datetime, timedelta
import calendar
from app.models.respond.general import generalResponse
from sqlalchemy.orm import Session
from fastapi import Request, Depends, APIRouter
from app.models.schemas.mentor.mentor_account import MentorDetailsResponse, MentorFilter, ReviewsResponse
from app.utils.average import getAverage
from app.utils.database import get_db
from app.models.database.mentor.db_mentor_user import DB_Mentor_Users, DB_Mentor_Review
from app.models.database.client.db_client_user import DB_Client_Users
from app.models.database.db_category import DB_Categories
from app.models.database.db_country import DB_Countries
from app.models.database.db_majors import DB_Majors
from app.models.database.db_appointment import DB_Appointments, AppointmentsState
from app.utils.oauth2 import get_current_user
from app.utils.validation import validateLanguageHeader


router = APIRouter(
    prefix="/mentors-details",
    tags=["Account"]
)

@router.get("/")
async def get_account(id :int , request: Request, db: Session = Depends(get_db)):
    myHeader = validateLanguageHeader(request)
    query = db.query(DB_Mentor_Users.id, DB_Mentor_Users.suffixe_name, 
                     DB_Mentor_Users.first_name, DB_Mentor_Users.last_name, DB_Mentor_Users.bio,
                    DB_Mentor_Users.speaking_language, DB_Mentor_Users.majors,
                    DB_Mentor_Users.hour_rate, DB_Mentor_Users.working_hours_saturday, DB_Mentor_Users.working_hours_sunday,
                    DB_Mentor_Users.working_hours_monday, DB_Mentor_Users.working_hours_tuesday, 
                    DB_Mentor_Users.working_hours_wednesday, DB_Mentor_Users.working_hours_thursday, DB_Mentor_Users.working_hours_friday,
                    DB_Mentor_Users.gender, DB_Mentor_Users.profile_img, DB_Mentor_Users.date_of_birth, DB_Mentor_Users.experience_since,
                    DB_Mentor_Users.country_id, DB_Categories.name_english.label("category_english"), DB_Categories.name_arabic.label("category_arabic"),
                    DB_Countries.name_english.label("country_english"), DB_Countries.name_arabic.label("country_arabic"), DB_Countries.flag_image.label("country_flag")
                    ).join(DB_Categories, DB_Categories.id == DB_Mentor_Users.category_id, isouter=True).join(DB_Countries, DB_Countries.id == DB_Mentor_Users.country_id, isouter=True).filter(DB_Mentor_Users.id == id).first()
                     
    if query == None:
       return generalResponse(message="profile was not found", data=None)
   
    majors_list = []
    major_query = db.query(DB_Majors.id, DB_Majors.name_english, DB_Majors.name_arabic).all()
    review_query =  db.query(DB_Mentor_Review.id, DB_Mentor_Review.client_id, DB_Mentor_Review.mentor_id, DB_Mentor_Review.stars, 
                             DB_Mentor_Review.comment, DB_Mentor_Review.created_at, 
                             DB_Client_Users.first_name.label("client_first_name"), 
                             DB_Client_Users.last_name.label("client_last_name"),
                             DB_Client_Users.profile_img.label("client_profile_img"),
                             ).join(DB_Client_Users, DB_Client_Users.id == DB_Mentor_Review.client_id, isouter=True).all()
    
    for item in query["majors"]:
        for major in major_query:
            if major["id"] == item:
                value = major["name_english"]
                if (myHeader.language == "ar"):
                    value = major["name_arabic"]
                majors_list.append(value)
    
    list_of_stars: list[float] = []
    list_of_reviews: list[ReviewsResponse] = []      
    rate_avg = 0
    for review in review_query:
         if review["mentor_id"] == id:
                list_of_stars.append(review["stars"])
                list_of_reviews.append(ReviewsResponse(id = review["id"], mentor_id = review["mentor_id"],
                                                    client_first_name = review["client_first_name"], client_last_name = review["client_last_name"], 
                                                    client_profile_img = review["client_profile_img"], 
                                                    stars = review["stars"], comments = review["comment"], 
                                                    created_at = review["created_at"]))
    rate_avg = getAverage(list_of_stars)   
    
    mentor_dtails = MentorDetailsResponse(suffixe_name = query["suffixe_name"], 
                                          first_name = query["first_name"], 
                                          last_name = query["last_name"], 
                                          bio = query["bio"], 
                                          speaking_language = query["speaking_language"], 
                                          hour_rate = query["hour_rate"], 
                                          gender = query["gender"], 
                                          profile_img = query["profile_img"], 
                                          date_of_birth = query["date_of_birth"], 
                                          experience_since = query["experience_since"], 
                                          category_name = query["category_arabic"] if (myHeader.language == "ar") else query["category_english"], 
                                          country = query["country_arabic"] if (myHeader.language == "ar") else query["country_english"], 
                                          country_flag = query["country_flag"], 
                                          total_rate = rate_avg, 
                                          major = majors_list,
                                          working_hours_saturday = query["working_hours_saturday"],
                                          working_hours_sunday = query["working_hours_sunday"],
                                          working_hours_monday = query["working_hours_monday"],
                                          working_hours_tuesday = query["working_hours_tuesday"],
                                          working_hours_wednesday = query["working_hours_wednesday"],
                                          working_hours_thursday = query["working_hours_thursday"],
                                          working_hours_friday = query["working_hours_friday"],
                                          reviews = list_of_reviews)
    
    return generalResponse(message="Profile return successfully", data= mentor_dtails)
    

@router.get("/mentor-avaliable")
def get_mentorAvaliable(catId :int, request: Request, db: Session = Depends(get_db)):
    myHeader = validateLanguageHeader(request)
    
    speaking_language = "English"
    if (myHeader.language == "ar"):
        speaking_language = "العربية"
        
    respond_mentor = None 
    list_of_mentors: list[MentorFilter] = []
    query_of_mentors_depend_on_category =  db.query(DB_Mentor_Users, DB_Mentor_Users.id, DB_Mentor_Users.gender, DB_Mentor_Users.suffixe_name,
                            DB_Mentor_Users.suffixe_name, DB_Mentor_Users.first_name, DB_Mentor_Users.last_name,
                            DB_Mentor_Users.profile_img, DB_Mentor_Users.hour_rate, DB_Mentor_Users.bio,
                            DB_Mentor_Users.experience_since,
                            DB_Mentor_Users.working_hours_saturday, DB_Mentor_Users.working_hours_sunday,
                            DB_Mentor_Users.working_hours_monday, DB_Mentor_Users.working_hours_tuesday, 
                            DB_Mentor_Users.working_hours_wednesday,DB_Mentor_Users.working_hours_thursday, 
                            DB_Mentor_Users.working_hours_friday,DB_Mentor_Users.speaking_language
                            ).filter(DB_Mentor_Users.category_id == catId
                            ).filter(DB_Mentor_Users.blocked == False).all()

    hour = 0

    while hour < 48:
        booking_time = (datetime.now() + timedelta(hours=hour))
        currentTimeDayName = calendar.day_name[booking_time.weekday()]
        for mentor in query_of_mentors_depend_on_category:
            if speaking_language in mentor["speaking_language"]:
                obj = MentorFilter(id = mentor["id"], gender =  mentor["gender"], suffixe_name = mentor["suffixe_name"], 
                               first_name = mentor["first_name"], last_name = mentor["last_name"], 
                               profile_img = mentor["profile_img"], hour_rate = mentor["hour_rate"],
                               bio = mentor["bio"], working_hours = [], day = currentTimeDayName, hour = 0)
        
                if (currentTimeDayName == "Saturday"):
                    obj.working_hours = mentor["working_hours_saturday"]
                elif currentTimeDayName == "Sunday":
                    obj.working_hours = mentor["working_hours_sunday"]
                elif (currentTimeDayName == "Monday"):
                    obj.working_hours = mentor["working_hours_monday"]
                elif (currentTimeDayName == "Tuesday"):
                    obj.working_hours = mentor["working_hours_tuesday"]
                elif (currentTimeDayName == "Wednesday"):
                    obj.working_hours = mentor["working_hours_wednesday"]
                elif (currentTimeDayName == "Thursday"):
                    obj.working_hours = mentor["working_hours_thursday"]
                elif (currentTimeDayName == "Friday"):
                    obj.working_hours = mentor["working_hours_friday"]
                
                list_of_mentors.append(obj)
 
        indexOfReservations = 0
        list_of_mentors_to_be_deleted: list[MentorFilter] = []
        for mentor in list_of_mentors:
            if (booking_time).hour in mentor.working_hours:
                list_of_mentors[indexOfReservations].hour = booking_time.hour 

                query_of_reservations = db.query(DB_Appointments.mentor_id, DB_Appointments.date_from, DB_Appointments.date_to, DB_Appointments.state
                            ).filter(DB_Appointments.mentor_id == mentor.id
                            ).filter(DB_Appointments.state == AppointmentsState.active).all()          
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
            list_of_stars: list[float] = []
            review_query = db.query(DB_Mentor_Review.id, DB_Mentor_Review.client_id, DB_Mentor_Review.mentor_id, DB_Mentor_Review.stars, 
                             ).filter(DB_Mentor_Review.mentor_id == mentor.id).all()
            for review in review_query:
                list_of_stars.append(review["stars"])
            
        
            list_of_mentors[indexOfRating].rate = getAverage(list_of_stars)
            indexOfRating = indexOfRating + 1
    
        if list_of_mentors != []:
            respond_mentor = list_of_mentors[0]
            for mentor in list_of_mentors:
                if mentor.rate > respond_mentor.rate:
                    respond_mentor = mentor
                    
            return generalResponse(message="Profiles return successfully", data=respond_mentor)
        else:
            hour += 1
           

    

