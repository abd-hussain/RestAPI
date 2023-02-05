from fastapi import Request, Depends ,APIRouter, File, UploadFile, Form, HTTPException, status
from sqlalchemy.orm import Session
from app.utils.validation import validateLanguageHeader
from app.utils.database import get_db
from app.models.database.mentor.db_mentor_user import DB_Mentor_Users
from app.models.database.db_country import DB_Countries
from app.models.schemas.mentor.mentor_account import UpdateMentorAccountInfoModel
from app.utils.generate import generateRequestId
from app.models.schemas.mentor.mentor_account import MentorChangePassword

from app.utils.oauth2 import get_current_user
from app.utils.validation import validateLanguageHeader
from app.models.respond.general import generalResponse
from app.utils.oauth2 import verifyPassword, hashingPassword

router = APIRouter(
    prefix="/mentor-account",
    tags=["Account"]
)

@router.get("/info")
async def get_account(request: Request, db: Session = Depends(get_db), get_current_user: int = Depends(get_current_user)):
    myHeader = validateLanguageHeader(request)
    query = db.query(DB_Mentor_Users.profile_img, DB_Mentor_Users.mobile_number, 
                     DB_Mentor_Users.suffixe_name, DB_Mentor_Users.date_of_birth, 
                     DB_Mentor_Users.first_name, DB_Mentor_Users.email, 
                     DB_Mentor_Users.last_name,DB_Mentor_Users.gender,
                     DB_Mentor_Users.speaking_language, DB_Mentor_Users.country_id, 
                     DB_Countries,
                     DB_Mentor_Users.referal_code,DB_Mentor_Users.id_img).join(DB_Countries, DB_Mentor_Users.country_id == DB_Countries.id, isouter=True)\
                         .filter(DB_Mentor_Users.id == get_current_user.user_id)

    if query.first() == None:
       return generalResponse(message="profile was not found", data=None)
    
    return generalResponse(message="Profile return successfully", data=query.first())

@router.delete("/delete")
async def delete_account(request: Request, db: Session = Depends(get_db), get_current_user: int = Depends(get_current_user)):
    myHeader = validateLanguageHeader(request)
    query = db.query(DB_Mentor_Users).filter(DB_Mentor_Users.id == get_current_user.user_id)

    if query.first() == None:
       return generalResponse(message="profile was not found", data=None)
   
    query.delete()
    db.commit()
    return generalResponse(message="Profile deleted successfully", data=None)


@router.put("/change-password")
async def update_password(request: Request,payload: MentorChangePassword,
                         db: Session = Depends(get_db), get_current_user: int = Depends(get_current_user)):
    myHeader = validateLanguageHeader(request)
    query = db.query(DB_Mentor_Users).filter(DB_Mentor_Users.id == get_current_user.user_id)

    if not verifyPassword(payload.oldpassword, query.first().password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")
    if payload.newpassword != None:
        query.update({"password" : hashingPassword(payload.newpassword)}, synchronize_session=False)
        db.commit()
        
    return generalResponse(message= "Change Password successfully", data=None)

@router.put("/info")
async def update_account(request: Request,suffixe_name: str = Form(None), first_name: str = Form(None),last_name: str = Form(None),
                         email: str = Form(None), mobile_number: str = Form(None),
                         gender: int = Form(None),date_of_birth: str = Form(None),
                         country_id: int = Form(None), speaking_language: list[str] = Form(None),
                         profile_picture: UploadFile = File(default=None), id_image: UploadFile = File(default=None),
                         db: Session = Depends(get_db), get_current_user: int = Depends(get_current_user)):
    myHeader = validateLanguageHeader(request)
    query = db.query(DB_Mentor_Users).filter(DB_Mentor_Users.id == get_current_user.user_id)
    
    payload = UpdateMentorAccountInfoModel(suffixe_name = suffixe_name, first_name = first_name, last_name = last_name, 
                                    email = email, mobile_number = mobile_number, date_of_birth = date_of_birth, 
                                    country_id = country_id, gender = gender, speaking_language = speaking_language)
    
    if payload.suffixe_name != None:
        query.update({"suffixe_name" : payload.suffixe_name}, synchronize_session=False)
    if payload.first_name != None:
        query.update({"first_name" : payload.first_name}, synchronize_session=False)
    if payload.last_name != None:
        query.update({"last_name" : payload.last_name}, synchronize_session=False)
    if payload.mobile_number != None:
        query.update({"mobile_number" : payload.mobile_number}, synchronize_session=False)
    if payload.email != None:
        query.update({"email" : payload.email}, synchronize_session=False)
    if payload.date_of_birth != None:
        query.update({"date_of_birth" : payload.date_of_birth}, synchronize_session=False)
    if payload.country_id != None:
        query.update({"country_id" : payload.country_id}, synchronize_session=False)
    if payload.gender != None:
        query.update({"gender" : payload.gender}, synchronize_session=False)
    if payload.speaking_language != None:
        query.update({"speaking_language" : payload.speaking_language}, synchronize_session=False)
        
    if profile_picture is not None:
        if profile_picture.content_type not in ["image/jpeg", "image/png", "image/jpg", "image/JPG"]:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail={"message": f"Profile Image Format is not valid", "request_id": generateRequestId()})
        
        profile_file_location = f"static/mentorsImg/{get_current_user.user_id}.png"
        try:
            contents_profile = profile_picture.file.read()
            with open(profile_file_location, 'wb+') as out_file:
                out_file.write(contents_profile)
                query.update({"profile_img" : profile_file_location}, synchronize_session=False)
        except Exception:
            return {"message": "There was an error uploading the file"}
        finally:
            profile_picture.file.close()
    if id_image is not None:
        if id_image.content_type not in ["image/jpeg", "image/png", "image/jpg", "image/JPG"]:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail={"message": f"Id Image Format is not valid", "request_id": generateRequestId()})
        id_file_location = f"static/Ids/{get_current_user.user_id}.png"
        try:
            contents_ids = profile_picture.file.read()
            with open(id_file_location, 'wb+') as out_file:
                out_file.write(contents_ids)
                query.update({"profile_img" : id_file_location}, synchronize_session=False)
        except Exception:
            return {"message": "There was an error uploading the file"}
        finally:
            profile_picture.file.close()
   
    db.commit()
    
    newQuery = db.query(DB_Mentor_Users.profile_img, DB_Mentor_Users.mobile_number, 
                     DB_Mentor_Users.suffixe_name, DB_Mentor_Users.date_of_birth, 
                     DB_Mentor_Users.first_name, DB_Mentor_Users.email, 
                     DB_Mentor_Users.last_name,DB_Mentor_Users.gender,
                     DB_Mentor_Users.speaking_language, DB_Mentor_Users.country_id, 
                     DB_Countries,
                     DB_Mentor_Users.referal_code,DB_Mentor_Users.id_img).join(DB_Countries, DB_Mentor_Users.country_id == DB_Countries.id, isouter=True)\
                         .filter(DB_Mentor_Users.id == get_current_user.user_id)
    return generalResponse(message="Profile updated successfully", data=newQuery.first())
