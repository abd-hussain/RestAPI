# from fastapi import Depends ,APIRouter, File, UploadFile, Form, HTTPException, status
# from sqlalchemy.orm import Session
# from app.utils.database import get_db
# from app.models.database.attorney.db_attorney_user import DB_Attorney_Users
# from app.models.database.db_country import DB_Countries
# from app.utils.oauth2 import get_current_user
# from app.models.respond.general import generalResponse
# from app.utils.validate_field import validateField
# from app.utils.file_upload import edit_file_uploaded

# router = APIRouter(
#     prefix="/attorney-account",
#     tags=["Attorney"]
# )

# @router.get("/info")
# async def get_account_info(db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):

#     query = db.query(DB_Attorney_Users.profile_img, DB_Attorney_Users.mobile_number, 
#                      DB_Attorney_Users.suffixe_name, DB_Attorney_Users.first_name, 
#                      DB_Attorney_Users.last_name, DB_Attorney_Users.date_of_birth,
#                      DB_Attorney_Users.email, DB_Attorney_Users.bio,
#                      DB_Attorney_Users.gender,
#                      DB_Attorney_Users.speaking_language, DB_Attorney_Users.country_id, 
#                      DB_Attorney_Users.invitation_code, DB_Attorney_Users.id_img,
#                      DB_Countries).join(DB_Countries, DB_Attorney_Users.country_id == DB_Countries.id, isouter=True)\
#                         .filter(DB_Attorney_Users.id == current_user.user_id).first()

#     if query == None:
#         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="profile was not found")

#     return generalResponse(message="Profile return successfully", data=query)

# @router.put("/info")
# async def update_account_info(suffixe_name: str = Form(None), 
#                               first_name: str = Form(None),
#                               last_name: str = Form(None),
#                               gender: int = Form(None),
#                                 date_of_birth: str = Form(None),
#                                 bio: str = Form(None),
#                                 country_id: int = Form(None), 
#                                     speaking_language:list[str] = ["en", "hi"],
#                                         profile_img: UploadFile = File(default=None), 
#                                         id_img: UploadFile = File(default=None),
#                                             db: Session = Depends(get_db), 
#                                             current_user: int = Depends(get_current_user)):

#     query = db.query(DB_Attorney_Users).filter(DB_Attorney_Users.id == current_user.user_id).first()
    
#     if query == None:
#         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="profile was not found")

#     query.suffixe_name = validateField(suffixe_name)
#     query.first_name = validateField(first_name)
#     query.last_name = validateField(last_name)
#     query.date_of_birth = validateField(date_of_birth)
#     query.gender = validateField(gender)
#     query.bio = validateField(bio)
#     query.speaking_language = validateField(speaking_language)
#     query.country_id = validateField(country_id)

#     if profile_img is not None:
#         query.profile_img = edit_file_uploaded(validateField(profile_img), 'profile_img', current_user.user_id)
        
#     if id_img is not None:
#         query.id_img = edit_file_uploaded(validateField(id_img), 'id_img', current_user.user_id)
   
#     db.commit()

#     return generalResponse(message="Profile updated successfully", data=None)






          

            
            

