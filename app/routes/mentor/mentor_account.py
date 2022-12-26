from datetime import datetime, timedelta
import calendar
from app.models.respond.general import generalResponse
from sqlalchemy.orm import Session
from fastapi import Request, Depends, APIRouter
from app.models.schemas.mentor.mentor_account import InstantMentor, MentorDetailsResponse, ReviewsResponse
from app.utils.average import getAverage
from app.utils.database import get_db
from app.models.database.mentor.db_mentor_user import DB_Mentor_Users, DB_Mentor_Review
from app.models.database.client.db_client_user import DB_Client_Users
from app.models.database.db_category import DB_Categories
from app.models.database.db_country import DB_Countries
from app.models.database.db_majors import DB_Majors
from app.models.database.db_appointment import DB_Mentors_Reservations
from app.utils.oauth2 import get_current_user
from app.utils.validation import validateLanguageHeader


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
                    DB_Mentor_Users.hour_rate_by_JD, DB_Mentor_Users.working_hours_saturday, DB_Mentor_Users.working_hours_sunday,
                    DB_Mentor_Users.working_hours_monday, DB_Mentor_Users.working_hours_tuesday,
                    DB_Mentor_Users.working_hours_wednesday, DB_Mentor_Users.working_hours_thursday, DB_Mentor_Users.working_hours_friday,
                    DB_Mentor_Users.gender, DB_Mentor_Users.profile_img, DB_Mentor_Users.date_of_birth,
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
                                          hour_rate_by_JD = query["hour_rate_by_JD"], 
                                          gender = query["gender"], 
                                          profile_img = query["profile_img"], 
                                          date_of_birth = query["date_of_birth"], 
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
    
@router.get("/appointment")
async def get_mentorAppointment(id :int , request: Request, db: Session = Depends(get_db), get_current_user: int = Depends(get_current_user)):
    myHeader = validateLanguageHeader(request)
    query = db.query(DB_Mentors_Reservations.mentor_id, DB_Mentors_Reservations.date
                     ).filter(DB_Mentors_Reservations.mentor_id == id).filter(DB_Mentors_Reservations.date > datetime.datetime.now()).all()
    return generalResponse(message="list of appointments return successfully", data=query)


@router.get("/mentor-avaliable")
async def get_mentorAvaliableWithin60min(catId :int, hour :int, request: Request, db: Session = Depends(get_db), get_current_user: int = Depends(get_current_user)):
    myHeader = validateLanguageHeader(request)
    
    speaking_language = "English"
    
    if (myHeader.language == "ar"):
        speaking_language = "العربية"

    currentTimeDayname = calendar.day_name[datetime.now().weekday()]
    query_of_mentors_depend_on_category =  db.query(DB_Mentor_Users)
     
    if (currentTimeDayname == "Saturday"):
        query_of_mentors_depend_on_category = db.query(DB_Mentor_Users.id, DB_Mentor_Users.suffixe_name, 
                    DB_Mentor_Users.first_name, DB_Mentor_Users.last_name, DB_Mentor_Users.profile_img, 
                    DB_Mentor_Users.category_id, DB_Mentor_Users.speaking_language, DB_Mentor_Users.hour_rate_by_JD,
                    DB_Mentor_Users.working_hours_saturday.label("working_hour"))
    elif (currentTimeDayname == "Sunday"):
        query_of_mentors_depend_on_category = db.query(DB_Mentor_Users.id, DB_Mentor_Users.suffixe_name, 
                    DB_Mentor_Users.first_name, DB_Mentor_Users.last_name, DB_Mentor_Users.profile_img, 
                    DB_Mentor_Users.category_id, DB_Mentor_Users.speaking_language, DB_Mentor_Users.hour_rate_by_JD,
                    DB_Mentor_Users.working_hours_sunday.label("working_hour"))
    elif (currentTimeDayname == "Monday"):
        query_of_mentors_depend_on_category = db.query(DB_Mentor_Users.id, DB_Mentor_Users.suffixe_name, 
                    DB_Mentor_Users.first_name, DB_Mentor_Users.last_name, DB_Mentor_Users.profile_img, 
                    DB_Mentor_Users.category_id, DB_Mentor_Users.speaking_language, DB_Mentor_Users.hour_rate_by_JD,
                    DB_Mentor_Users.working_hours_monday.label("working_hour"))
    elif (currentTimeDayname == "Tuesday"):
        query_of_mentors_depend_on_category = db.query(DB_Mentor_Users.id, DB_Mentor_Users.suffixe_name, 
                    DB_Mentor_Users.first_name, DB_Mentor_Users.last_name, DB_Mentor_Users.profile_img, 
                    DB_Mentor_Users.category_id, DB_Mentor_Users.speaking_language, DB_Mentor_Users.hour_rate_by_JD,
                    DB_Mentor_Users.working_hours_tuesday.label("working_hour"))
    elif (currentTimeDayname == "Wednesday"):
        query_of_mentors_depend_on_category = db.query(DB_Mentor_Users.id, DB_Mentor_Users.suffixe_name, 
                    DB_Mentor_Users.first_name, DB_Mentor_Users.last_name, DB_Mentor_Users.profile_img, 
                    DB_Mentor_Users.category_id, DB_Mentor_Users.speaking_language, DB_Mentor_Users.hour_rate_by_JD,
                    DB_Mentor_Users.working_hours_wednesday.label("working_hour"))
    elif (currentTimeDayname == "Thursday"):
        query_of_mentors_depend_on_category = db.query(DB_Mentor_Users.id, DB_Mentor_Users.suffixe_name, 
                    DB_Mentor_Users.first_name, DB_Mentor_Users.last_name, DB_Mentor_Users.profile_img, 
                    DB_Mentor_Users.category_id, DB_Mentor_Users.speaking_language, DB_Mentor_Users.hour_rate_by_JD,
                    DB_Mentor_Users.working_hours_thursday.label("working_hour"))
    elif (currentTimeDayname == "Friday"):
        query_of_mentors_depend_on_category = db.query(DB_Mentor_Users.id, DB_Mentor_Users.suffixe_name, 
                    DB_Mentor_Users.first_name, DB_Mentor_Users.last_name, DB_Mentor_Users.profile_img, 
                    DB_Mentor_Users.category_id, DB_Mentor_Users.speaking_language, DB_Mentor_Users.hour_rate_by_JD,
                    DB_Mentor_Users.working_hours_friday.label("working_hour"))
            
    query_of_mentors_depend_on_category = query_of_mentors_depend_on_category.filter(DB_Mentor_Users.category_id == catId).all()
    
    review_query =  db.query(DB_Mentor_Review.id, DB_Mentor_Review.client_id, DB_Mentor_Review.mentor_id, DB_Mentor_Review.stars, 
                             ).join(DB_Client_Users, DB_Client_Users.id == DB_Mentor_Review.client_id, isouter=True).all()
    
    list_of_mentors: list[InstantMentor] = []

    for mentor in query_of_mentors_depend_on_category:
        if speaking_language in mentor["speaking_language"]:
            list_of_stars: list[float] = []
            listOfWorking_hour = mentor["working_hour"]
            for hour in listOfWorking_hour:
                if int((datetime.now() + timedelta(hours=hour)).hour) >= hour:
                    query_of_reservations = db.query(DB_Mentors_Reservations.mentor_id, DB_Mentors_Reservations.date
                            ).filter(DB_Mentors_Reservations.mentor_id == mentor["id"]).all()
                    if (query_of_reservations == []):
                        haveReservation = False
                    else:
                        haveReservation = False
                        for reservations in query_of_reservations:
                            if reservations["date"].date() == datetime.today().date():
                                haveReservation = True
                                
                    if (haveReservation == False):
                        for review in review_query:
                            if review["mentor_id"] == mentor["id"]:
                                list_of_stars.append(review["stars"])
              
                        list_of_mentors.append(InstantMentor(id = mentor["id"], suffixe_name = mentor["suffixe_name"], 
                                                             first_name = mentor["first_name"], last_name = mentor["last_name"], 
                                                             profile_img = mentor["profile_img"], hour_rate_by_JD = mentor["hour_rate_by_JD"],
                                                             rate = getAverage(list_of_stars)))
                            
   

    respond_mentor = None 
    if list_of_mentors != []:
        respond_mentor = list_of_mentors[0]
        for mentor in list_of_mentors:
            if mentor.rate > respond_mentor.rate:
                respond_mentor = mentor
        
                    
                      
    return generalResponse(message="Profiles return successfully", data=respond_mentor)
