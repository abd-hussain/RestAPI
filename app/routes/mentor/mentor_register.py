from fastapi import Request, Depends ,APIRouter, Form, HTTPException, status,File, UploadFile
from sqlalchemy.orm import Session
from app.utils.generate import generateAPIKey, generateActvationCode
from app.utils.database import get_db
from app.models.database.mentor.db_mentor_user import DB_Mentor_Users
from app.models.schemas.mentor_account import  RegisterMentorAccountModel
from app.utils.firebase_notifications.notifications_manager import UserType, addNewNotification
from app.models.respond.general import generalResponse
from app.utils.oauth2 import hashingPassword
from app.utils.validation import validateLanguageHeader
from app.utils.add_point import add_points_to_referer
from app.utils.validate_field import validateField
from app.utils.file_upload import handle_file_upload

router = APIRouter(
    prefix="/mentor",
    tags=["Account"]
)

@router.post("/register")
async def register_mentor(request: Request, 
    suffixe_name: str = Form(None),
    first_name: str = Form(None),
    last_name: str = Form(None),
    date_of_birth: str = Form(None),
    gender: int = Form(None),
    bio: str = Form(None),
        email: str = Form(None),
        password: str = Form(None),
        mobile_number: str = Form(None),
            push_token: str = Form(None),
            app_version: str = Form(None),
            category_id: int = Form(None),
            hour_rate: str = Form(None), 
            iban: str = Form(None),
            experience_since: str = Form(None),
            country_id: int = Form(None),
            referral_code: str = Form(None),
                majors:list[int] = Form(None),
                working_hours_saturday:list[str] = [],
                working_hours_sunday:list[str] = [],
                working_hours_monday:list[str] = [],
                working_hours_tuesday:list[str] = [],
                working_hours_wednesday:list[str] = [],
                working_hours_thursday:list[str] = [],
                working_hours_friday:list[str] = [],
                speaking_language:list[str] = ["en", "hi"],
                    profile_img: UploadFile = File(default=None), 
                    id_img: UploadFile = File(default=None),
                    cv: UploadFile = File(default=None), 
                    cert1: UploadFile = File(default=None), 
                    cert2: UploadFile = File(default=None),
                    cert3: UploadFile = File(default=None),
                        db: Session = Depends(get_db)):
    
    myHeader = validateLanguageHeader(request)
    
    validate_existing_user(email, mobile_number, db)

    lastId = db.query(DB_Mentor_Users).order_by(DB_Mentor_Users.id.desc()).first().id + 1
    
    payload = RegisterMentorAccountModel(id=lastId,
                                        suffixe_name = validateField(suffixe_name),
                                        first_name = validateField(first_name), 
                                        last_name = validateField(last_name),
                                        gender = validateField(gender),
                                        invitation_code = generateActvationCode(),
                                        api_key = generateAPIKey(),
                                        password = hashingPassword(validateField(password)),
                                        date_of_birth = validateField(date_of_birth),
                                        bio = validateField(bio),
                                        email = validateField(email),
                                        mobile_number = validateField(mobile_number),
                                        push_token = push_token,
                                        app_version = validateField(app_version), 
                                        experience_since = validateField(experience_since),
                                        category_id = validateField(category_id), 
                                        hour_rate = validateField(hour_rate),
                                        country_id = validateField(country_id),
                                        speaking_language = validateField(speaking_language),
                                        majors = majors,
                                        iban = iban,
                                        working_hours_saturday = working_hours_saturday,
                                        working_hours_sunday = working_hours_sunday,
                                        working_hours_monday = working_hours_monday,
                                        working_hours_tuesday = working_hours_tuesday,
                                        working_hours_wednesday = working_hours_wednesday,
                                        working_hours_thursday = working_hours_thursday,
                                        working_hours_friday = working_hours_friday,
                                        )

    if profile_img is not None:
        handle_file_upload(profile_img, 'profile_img', lastId, payload)
    
    if id_img is not None:
        handle_file_upload(id_img, 'id_img', lastId, payload)
        
    if cv is not None:
        handle_file_upload(cv, 'cv', lastId, payload)

    if cert1 is not None:
        handle_file_upload(cert1, 'cert1', lastId, payload)
        
    if cert2 is not None:
        handle_file_upload(cert2, 'cert2', lastId, payload)
        
    if cert3 is not None:
        handle_file_upload(cert3, 'cert3', lastId, payload)
             
    obj = DB_Mentor_Users(**payload.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)

    if push_token != None:
        add_new_notification(myHeader.language, lastId, db)
        
    
    add_points_to_referer(referral_code = referral_code, 
                          new_mentor_client_id = lastId, 
                          db = db)
        
    return generalResponse(message= "Account Created successfully", data=None)

#############################################################################################

def validate_existing_user(email, mobile_number, db):
    if db.query(DB_Mentor_Users).filter(DB_Mentor_Users.email == email).first():
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="User with this email already exists")
    if db.query(DB_Mentor_Users).filter(DB_Mentor_Users.mobile_number == mobile_number).first():
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="User with this Mobile already exists")
    
def add_new_notification(language, lastId, db):
    addNewNotification(user_type = UserType.Mentor,
                                        user_id = lastId,
                                        currentLanguage = language,
                                        db = db,
                                        title_english = "Account Registered Successfully",
                                        title_arabic = "تم تسجيل الحساب بنجاح",
                                        content_english = "Welcome To LegalzHub Applications, we are here to hear from you so if you have any suggestions or issues please contact us from the account screen",
                                        content_arabic = "مرحبًا بك في تطبيقات LegalzHub، نحن هنا لنسمع منك، لذا إذا كان لديك أي اقتراحات أو مشكلات، فيرجى الاتصال بنا من شاشة الحساب"
                                        )