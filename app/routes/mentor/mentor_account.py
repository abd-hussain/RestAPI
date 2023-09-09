from fastapi import Depends ,APIRouter, File, UploadFile, Form
from sqlalchemy.orm import Session
from app.utils.validation import validateImageType
from app.utils.database import get_db
from app.models.database.mentor.db_mentor_user import DB_Mentor_Users
from app.models.database.db_country import DB_Countries

from app.utils.oauth2 import get_current_user
from app.models.respond.general import generalResponse

router = APIRouter(
    prefix="/mentor-account",
    tags=["Account"]
)

@router.get("/info")
async def get_account(db: Session = Depends(get_db), get_current_user: int = Depends(get_current_user)):

    query = db.query(DB_Mentor_Users.profile_img, DB_Mentor_Users.mobile_number, 
                     DB_Mentor_Users.suffixe_name, DB_Mentor_Users.first_name, 
                     DB_Mentor_Users.last_name, DB_Mentor_Users.date_of_birth,
                     DB_Mentor_Users.email, DB_Mentor_Users.bio,
                     DB_Mentor_Users.gender,
                     DB_Mentor_Users.speaking_language, DB_Mentor_Users.country_id, 
                     DB_Mentor_Users.referal_code,DB_Mentor_Users.id_img,
                     DB_Countries).join(DB_Countries, DB_Mentor_Users.country_id == DB_Countries.id, isouter=True)\
                        .filter(DB_Mentor_Users.id == get_current_user.user_id).first()

    if query == None:
       return generalResponse(message="profile was not found", data=None)

    return generalResponse(message="Profile return successfully", data=query)

@router.put("/info")
async def update_account(suffixe_name: str = Form(None), first_name: str = Form(None),last_name: str = Form(None),
                         gender: int = Form(None),date_of_birth: str = Form(None),
                         bio: str = Form(None),
                         country_id: int = Form(None), speaking_language:list[str] = ["en", "hi"],
                         profile_picture: UploadFile = File(default=None), id_image: UploadFile = File(default=None),
                         db: Session = Depends(get_db), get_current_user: int = Depends(get_current_user)):

    query = db.query(DB_Mentor_Users).filter(DB_Mentor_Users.id == get_current_user.user_id)
        
    if suffixe_name != None:
        query.update({"suffixe_name" : suffixe_name}, synchronize_session=False)
    if first_name != None:
        query.update({"first_name" : first_name}, synchronize_session=False)
    if last_name != None:
        query.update({"last_name" : last_name}, synchronize_session=False)
    if date_of_birth != None:
        query.update({"date_of_birth" : date_of_birth}, synchronize_session=False)
    if gender != None:
        query.update({"gender" : gender}, synchronize_session=False)
    if bio != None:
        query.update({"bio" : bio}, synchronize_session=False)
    if speaking_language != None:
        query.update({"speaking_language" : speaking_language}, synchronize_session=False)
    if country_id != None:
        query.update({"country_id" : country_id}, synchronize_session=False)
                
    if profile_picture is not None:
        imageExtension = validateImageType(profile_picture, "profile_picture")
        
        profile_file_location = f"static/mentorsImg/{get_current_user.user_id}{imageExtension}"
        try:
            contents_profile = profile_picture.file.read()
            with open(profile_file_location, 'wb+') as out_file:
                out_file.write(contents_profile)
                query.update({"profile_img" : f"{get_current_user.user_id}{imageExtension}"}, synchronize_session=False)
        except Exception:
            return {"message": "There was an error uploading the file"}
        finally:
            profile_picture.file.close()
            
    if id_image is not None:
        imageExtension = validateImageType(id_image, "id_image")

        id_file_location = f"static/mentorsIDs/{get_current_user.user_id}.png"
        try:
            contents_ids = id_image.file.read()
            with open(id_file_location, 'wb+') as out_file:
                out_file.write(contents_ids)
                query.update({"id_img" : f"{get_current_user.user_id}{imageExtension}"}, synchronize_session=False)
        except Exception:
            return {"message": "There was an error uploading the file"}
        finally:
            id_image.file.close()
   
    db.commit()

    return generalResponse(message="Profile updated successfully", data=None)






          

            
            

