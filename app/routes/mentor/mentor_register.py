from fastapi import Request, Depends ,APIRouter, Form, HTTPException, status,File, UploadFile
from sqlalchemy.orm import Session
from app.utils.generate import generateAPIKey, generateActvationCode
from app.utils.validation import validateFileType, validateImageType
from app.utils.database import get_db
from app.models.database.mentor.db_mentor_user import DB_Mentor_Users
from app.models.schemas.mentor_account import  RegisterMentorAccountModel

from app.models.respond.general import generalResponse
from app.utils.oauth2 import hashingPassword

router = APIRouter(
    prefix="/mentor",
    tags=["Account"]
)

@router.post("/register")
async def register_mentor(suffixe_name: str = Form(None),
                          first_name: str = Form(None),
                          last_name: str = Form(None),
                          gender: int = Form(None),
                          date_of_birth: str = Form(None),
                          bio: str = Form(None),
                          country_id: int = Form(None),
                          speaking_language:list[str] = ["en", "hi"],
                          experience_since: str = Form(None),
                          majors:list[str] = Form(None),
                          push_token: str = Form(None),
                          category_id: int = Form(None),
                          referal_code: str = Form(None),
                          app_version: str = Form(None),
                          hour_rate: str = Form(None),
                          password: str = Form(None),
                          email: str = Form(None),
                          mobile_number: str = Form(None),
                          working_hours_saturday:list[str] = [],
                          working_hours_sunday:list[str] = [],
                          working_hours_monday:list[str] = [],
                          working_hours_tuesday:list[str] = [],
                          working_hours_wednesday:list[str] = [],
                          working_hours_thursday:list[str] = [],
                          working_hours_friday:list[str] = [],
                          profile_img: UploadFile = File(default=None), 
                          id_img: UploadFile = File(default=None),
                          cv: UploadFile = File(default=None), 
                          cert1: UploadFile = File(default=None), 
                          cert2: UploadFile = File(default=None),
                          cert3: UploadFile = File(default=None),
       db: Session = Depends(get_db)):
    
    
    filterQuery1 = db.query(DB_Mentor_Users).filter(DB_Mentor_Users.email == email).first()
    filterQuery2 = db.query(DB_Mentor_Users).filter(DB_Mentor_Users.mobile_number == mobile_number).first()
    filterQuery3 = db.query(DB_Mentor_Users).order_by(DB_Mentor_Users.id.desc()).first()
    lastId = filterQuery3.id + 1
    if filterQuery1 != None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail= "User with this email already exsist")
    if filterQuery2 != None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail= "User with this Mobile already exsist")
    
    payload = RegisterMentorAccountModel()

    payload.id = lastId
    payload.suffixe_name = validateField(suffixe_name) 
    payload.first_name = validateField(first_name) 
    payload.last_name = validateField(last_name) 
    payload.gender = validateField(gender) 
    payload.invitation_code = generateActvationCode()
    payload.api_key = generateAPIKey()
    payload.password = hashingPassword(validateField(password))
    payload.date_of_birth = validateField(date_of_birth) 
    payload.bio = validateField(bio) 
    payload.email = validateField(email) 
    payload.mobile_number = validateField(mobile_number) 
    payload.push_token = push_token

    payload.app_version = validateField(app_version) 
    payload.experience_since = experience_since

    payload.category_id = validateField(category_id) 
    payload.hour_rate = validateField(hour_rate)
    payload.country_id = validateField(country_id)
    payload.speaking_language = validateField(speaking_language) 
    

    payload.referal_code = referal_code
    payload.working_hours_saturday = working_hours_saturday
    payload.working_hours_sunday = working_hours_sunday
    payload.working_hours_monday = working_hours_monday
    payload.working_hours_tuesday = working_hours_tuesday
    payload.working_hours_wednesday = working_hours_wednesday
    payload.working_hours_thursday = working_hours_thursday
    payload.working_hours_friday = working_hours_friday
    payload.majors = majors

    if profile_img is not None:
        imageExtension = validateImageType(profile_img, "profile_img")
        profile_file_location = f"static/mentorsImg/{lastId}{imageExtension}"
        try:
            contents_profile = profile_img.file.read()
            with open(profile_file_location, 'wb+') as out_file:
                out_file.write(contents_profile)
                payload.profile_img = f"{lastId}{imageExtension}"
        except Exception:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Error in uploading profile_img")
        finally:
            profile_img.file.close()
            
    if id_img is not None:
        imageExtension = validateImageType(id_img, "id_img")
        id_file_location = f"static/mentorsIDs/{lastId}.png"
        try:
            contents_ids = id_img.file.read()
            with open(id_file_location, 'wb+') as out_file:
                out_file.write(contents_ids)
                payload.id_img = f"{lastId}{imageExtension}"
        except Exception:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Error in uploading id_img")
        finally:
            id_img.file.close()

    if cv is not None:
        fileExtension = validateFileType(cv, "cv")
        cv_file_location = f"static/mentorsCVs/{lastId}{fileExtension}"
        try:
            contents_cv = cv.file.read()
            with open(cv_file_location, 'wb+') as out_file:
                out_file.write(contents_cv)
                payload.cv = f"{lastId}{fileExtension}"
        except Exception:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Error in uploading cv")
        finally:
             cv.file.close()
             
    if cert1 is not None:
        cert1Extension = validateFileType(cert1, "cert1")
        cert1_file_location = f"static/mentorsCerts/{lastId}-cer1{cert1Extension}"
        try:
            contents_cert1 = cert1.file.read()
            with open(cert1_file_location, 'wb+') as out_file:
                out_file.write(contents_cert1)
                payload.cert1 = f"{lastId}-cer1{cert1Extension}"
        except Exception:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Error in uploading cert1")
        finally:
             cert1.file.close()
             
    if cert2 is not None:
        cert2Extension = validateFileType(cert2, "cert2")
        cert2_file_location = f"static/mentorsCerts/{lastId}-cer2{cert2Extension}"
        try:
            contents_cert2 = cert2.file.read()
            with open(cert2_file_location, 'wb+') as out_file:
                out_file.write(contents_cert2)
                payload.cert2 = f"{lastId}-cer2{cert2Extension}"
        except Exception:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Error in uploading cert2")
        finally:
             cert2.file.close()
             
    if cert3 is not None:
        cert3Extension = validateFileType(cert3, "cert3")
        cert3_file_location = f"static/mentorsCerts/{lastId}-cer3{cert3Extension}"
        try:
            contents_cert3 = cert3.file.read()
            with open(cert3_file_location, 'wb+') as out_file:
                out_file.write(contents_cert3)
                payload.cert3 = f"{lastId}-cer3{cert3Extension}"
        except Exception:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Error in uploading cert3")
        finally:
             cert3.file.close()
             
    obj = DB_Mentor_Users(**payload.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    
    return generalResponse(message= "Account Created successfully", data=None)


def validateField(fild) -> any:
    if fild != None:
        return fild
    else :
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail= "filed missing")
