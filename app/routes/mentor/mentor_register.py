from fastapi import Request, Depends ,APIRouter, File, UploadFile, Form, HTTPException, status
from pydantic import EmailStr
from sqlalchemy.orm import Session
from app.utils.generate import generateAPIKey, generateActvationCode
from app.utils.validation import validateLanguageHeader
from app.utils.database import get_db
from app.models.database.mentor.db_mentor_user import DB_Mentor_Users
from app.models.database.db_country import DB_Countries
from app.models.schemas.mentor.mentor_account import  RegisterMentorAccountModel, UpdateMentorAccountInfoModel

from app.utils.oauth2 import get_current_user
from app.utils.validation import validateLanguageHeader
from app.models.respond.general import generalResponse
from app.utils.oauth2 import verifyPassword, hashingPassword

router = APIRouter(
    prefix="/mentor",
    tags=["Account"]
)

@router.post("/register")
async def register_mentor(request: Request,suffixe_name: str = Form(None),
            first_name: str = Form(None), last_name: str = Form(None),
            country_id: int = Form(None), gender: int = Form(None),
            mobile_number: str = Form(None), date_of_birth: str = Form(None),
            bio: str = Form(None), category_id: int = Form(None),
            profile_img: UploadFile = File(None), id_img: UploadFile = File(None),
            cv: UploadFile = File(None), cert1: UploadFile = File(None), 
            cert2: UploadFile = File(None), cert3: UploadFile = File(None), 
            speaking_language: list[str] = [],app_version: str = File(None),
            working_hours_saturday: list[str] = [], 
            working_hours_sunday: list[str] = [],
            working_hours_monday: list[str] = [],
            working_hours_tuesday: list[str] = [],
            working_hours_wednesday: list[str] = [],
            working_hours_thursday: list[str] = [],
            working_hours_friday: list[str] = [], 
            majors: list[str] = [], hour_rate: float = Form(None), 
            referalCode: str = Form(None),
            push_token: str = Form(None), experience_since: str = Form(None),
            email: EmailStr = Form(None), password: str = Form(None),
                         db: Session = Depends(get_db)):
    
    myHeader = validateLanguageHeader(request)
    
    speaking_language = sortListOfString(speaking_language)
    majors = sortListOfString(majors)
    working_hours_saturday = sortListOfString(working_hours_saturday)
    working_hours_sunday = sortListOfString(working_hours_sunday)
    working_hours_monday = sortListOfString(working_hours_monday)
    working_hours_tuesday = sortListOfString(working_hours_tuesday)
    working_hours_wednesday = sortListOfString(working_hours_wednesday)
    working_hours_thursday = sortListOfString(working_hours_thursday)
    working_hours_friday = sortListOfString(working_hours_friday)

    payload = RegisterMentorAccountModel()
    
    payload.suffixe_name = validateField(suffixe_name, "suffixe_name")
    payload.first_name = validateField(first_name, "first_name")
    payload.last_name = validateField(last_name, "last_name")
    payload.country_id = validateField(country_id, "country_id")
    payload.gender = validateField(gender, "gender")
    payload.mobile_number = validateField(mobile_number, "mobile_number")
    payload.date_of_birth = validateField(date_of_birth, "date_of_birth")
    payload.majors = validateField(majors, "majors")
    # payload.profile_img = validateImageType(validateField(profile_img, "profile_img"), "profile_img") 
    # payload.id_img = validateImageType(validateField(id_img, "id_img"), "id_img") 
    payload.bio = validateField(bio, "bio")
    payload.category_id = validateField(category_id, "category_id")
    # payload.cv = validatePDFFileType(validateField(cv, "cv"), "cv")
    # payload.cert1 = cert1
    # payload.cert2 = cert2
    # payload.cert3 = cert3
    payload.speaking_language = validateField(speaking_language, "speaking_language")
    payload.working_hours_saturday = working_hours_saturday
    payload.working_hours_sunday = working_hours_sunday
    payload.working_hours_monday = working_hours_monday
    payload.working_hours_tuesday = working_hours_tuesday
    payload.working_hours_wednesday = working_hours_wednesday
    payload.working_hours_thursday = working_hours_thursday
    payload.working_hours_friday = working_hours_friday
    payload.hour_rate = validateField(hour_rate, "hour_rate")
    payload.referal_code = referalCode
    payload.email = validateField(email, "email")
    payload.password = hashingPassword(validateField(password, "password"))
    payload.app_version = validateField(app_version, "app_version")
    payload.experience_since = validateField(experience_since, "experience_since")
    payload.push_token = validateField(push_token, "push_token")
    payload.api_key = generateAPIKey()
    payload.invitation_code = generateActvationCode()

    query1 = db.query(DB_Mentor_Users).filter(DB_Mentor_Users.mobile_number == payload.mobile_number).first()
    query2 = db.query(DB_Mentor_Users).filter(DB_Mentor_Users.email == payload.email).first()

    if query1 != None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail= "User with this mobile number already exsist")
    if query2 != None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail= "User with this email already exsist")


    obj = DB_Mentor_Users(**payload.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
        
    return generalResponse(message= "Account Created successfully", data=None)


def sortListOfString(list: list[str]) -> list[str]:
    if (len(list) == 1):
        list = [item.strip() for item in list[0].split(',')]
        return list

def validateImageType(image: Form(None), imageName: str) -> Form(None):
    if image.content_type not in ["image/jpeg", "image/png", "image/jpg", "image/JPG"]:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail= imageName + " Format is not valid")
    else:
        return image
    
def validatePDFFileType(file: Form(None), fileName: str) -> Form(None):
    if file.content_type not in ['application/pdf', "application/vnd.openxmlformats-officedocument.wordprocessingml.document"]:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail= fileName + " Format is not valid")
    else:
        return file
    
def validateField(field: Form(None), fieldName: str) -> Form(None):
    if field is None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail= fieldName + " required")
    else:
        return field
    
