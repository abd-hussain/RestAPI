# from fastapi import Depends ,APIRouter, Request, Form, File, UploadFile, HTTPException, status
# from sqlalchemy.orm import Session
# from app.models.database.db_category import DB_Categories
# from app.utils.validation import validateLanguageHeader
# from app.utils.database import get_db
# from app.models.database.attorney.db_attorney_user import DB_Attorney_Users
# from app.utils.oauth2 import get_current_user
# from app.models.respond.general import generalResponse
# from app.utils.validate_field import validateField
# from app.utils.file_upload import edit_file_uploaded

# router = APIRouter(
#     prefix="/attorney-account",
#     tags=["Attorney"]
# )
    
# @router.get("/exp-info")
# async def get_account_experinace(request: Request, db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
#     myHeader = validateLanguageHeader(request)
    
#     category_name_field = DB_Categories.name_english.label("category_name") if myHeader.language == "en" else DB_Categories.name_arabic.label("category_name")

#     attorney_experience = db.query(DB_Attorney_Users.cv, 
#                      DB_Attorney_Users.cert1, DB_Attorney_Users.cert2, DB_Attorney_Users.cert3,
#                      DB_Attorney_Users.experience_since,
#                      DB_Attorney_Users.category_id,
#                      category_name_field)\
#                          .join(DB_Categories, DB_Categories.id == DB_Attorney_Users.category_id, isouter=True)\
#                          .filter(DB_Attorney_Users.id == current_user.user_id).first()
                         
#     if attorney_experience == None:
#         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="profile was not found")

#     return generalResponse(message="Profile Experiances return successfully", data=attorney_experience)

# @router.put("/exp-info")
# async def update_account_experinace(experience_since: str = Form(None), 
#                                     category_id: int = Form(None),
#                                     cv: UploadFile = File(default=None), 
#                                     cert1: UploadFile = File(default=None), 
#                                     cert2: UploadFile = File(default=None),
#                                     cert3: UploadFile = File(default=None),
#                                     db: Session = Depends(get_db), 
#                                     current_user: int = Depends(get_current_user)):

#     query = db.query(DB_Attorney_Users).filter(DB_Attorney_Users.id == current_user.user_id).first()
    
#     if query == None:
#         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="profile was not found")
   
#     query.experience_since = validateField(experience_since)
#     query.category_id = validateField(category_id)
    
#     if cv is not None:
#         query.cv = edit_file_uploaded(validateField(cv), 'cv', current_user.user_id)
    
#     if cert1 is not None:
#         query.cert1 = edit_file_uploaded(validateField(cert1), 'cert1', current_user.user_id)
    
#     if cert2 is not None:
#         query.cert2 = edit_file_uploaded(validateField(cert2), 'cert2', current_user.user_id)
    
#     if cert3 is not None:
#         query.cert3 = edit_file_uploaded(validateField(cert3), 'cert3', current_user.user_id)
             
#     db.commit()

#     return generalResponse(message="Experiances updated successfully", data=None)