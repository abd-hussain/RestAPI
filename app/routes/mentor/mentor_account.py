from fastapi import Depends ,APIRouter, File, UploadFile, Form, HTTPException, status
from sqlalchemy.orm import Session
from app.utils.database import get_db
from app.models.database.mentor.db_mentor_user import DB_Mentor_Users
from app.models.database.db_country import DB_Countries
from app.utils.oauth2 import get_current_user
from app.models.respond.general import generalResponse
from app.utils.validate_field import validateField
from app.utils.file_upload import edit_file_uploaded

router = APIRouter(
    prefix="/mentor-account",
    tags=["Account"]
)

@router.get("/info")
async def get_account_info(db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):

    query = db.query(DB_Mentor_Users.profile_img, DB_Mentor_Users.mobile_number, 
                     DB_Mentor_Users.suffixe_name, DB_Mentor_Users.first_name, 
                     DB_Mentor_Users.last_name, DB_Mentor_Users.date_of_birth,
                     DB_Mentor_Users.email, DB_Mentor_Users.bio,
                     DB_Mentor_Users.gender,
                     DB_Mentor_Users.speaking_language, DB_Mentor_Users.country_id, 
                     DB_Mentor_Users.invitation_code, DB_Mentor_Users.id_img,
                     DB_Countries).join(DB_Countries, DB_Mentor_Users.country_id == DB_Countries.id, isouter=True)\
                        .filter(DB_Mentor_Users.id == current_user.user_id).first()

    if query == None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="profile was not found")

    return generalResponse(message="Profile return successfully", data=query)

@router.put("/info")
async def update_account_info(suffixe_name: str = Form(None), 
                              first_name: str = Form(None),
                              last_name: str = Form(None),
                                gender: int = Form(None),
                                date_of_birth: str = Form(None),
                                bio: str = Form(None),
                                country_id: int = Form(None), 
                                    speaking_language:list[str] = ["en", "hi"],
                                        profile_img: UploadFile = File(default=None), 
                                        id_img: UploadFile = File(default=None),
                                            db: Session = Depends(get_db), 
                                            current_user: int = Depends(get_current_user)):

    query = db.query(DB_Mentor_Users).filter(DB_Mentor_Users.id == current_user.user_id).first()
    
    if query == None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="profile was not found")

    query.suffixe_name = validateField(suffixe_name)
    query.first_name = validateField(first_name)
    query.last_name = validateField(last_name)
    query.date_of_birth = validateField(date_of_birth)
    query.gender = validateField(gender)
    query.bio = validateField(bio)
    query.speaking_language = validateField(speaking_language)
    query.country_id = validateField(country_id)

    query.profile_img = edit_file_uploaded(validateField(profile_img), 'profile_img', current_user.user_id)
    query.id_img = edit_file_uploaded(validateField(id_img), 'id_img', current_user.user_id)
   
    db.commit()

    return generalResponse(message="Profile updated successfully", data=None)






          

            
            

