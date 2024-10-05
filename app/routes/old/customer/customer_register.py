# from fastapi import Request, Depends ,APIRouter, Form, HTTPException, status,File, UploadFile
# from sqlalchemy.orm import Session
# from app.utils.generate import generateAPIKey, generateActvationCode
# from app.utils.database import get_db
# from app.models.database.customer.db_customer_user import DB_Customer_Users
# from app.models.schemas.attorney_account import  RegisterCustomerAccountModel
# from app.utils.firebase_notifications.notifications_manager import addNewNotification, UsersType
# from app.models.respond.general import generalResponse
# from app.utils.oauth2 import hashingPassword
# from app.utils.validation import validateLanguageHeader
# from app.utils.add_point import add_points_to_referer
# from app.utils.validate_field import validateField
# from app.utils.file_upload import handle_file_upload

# router = APIRouter(
#     prefix="/customer/register",
#     tags=["Customer"]
# )

# @router.post("/")
# async def register_customer(request: Request, 
#     first_name: str = Form(None),
#     last_name: str = Form(None),
#     mobile_number: str = Form(None),
#         email: str = Form(None),
#         password: str = Form(None),
#             gender: int = Form(None),
#             referral_code: str = Form(None),
#             profile_img: UploadFile = File(default=None), 
#             date_of_birth: str = Form(None),
#             push_token: str = Form(None),
#             app_version: str = Form(None),
#             country_id: int = Form(None),
#             db: Session = Depends(get_db)):
    
#     myHeader = validateLanguageHeader(request)
    
#     validate_existing_user(email, mobile_number, db)

#     lastId = db.query(DB_Customer_Users).order_by(DB_Customer_Users.id.desc()).first().id + 1

#     payload = RegisterCustomerAccountModel(id=lastId,
#                                         first_name = validateField(first_name), 
#                                         last_name = validateField(last_name),
#                                         mobile_number = validateField(mobile_number),
#                                         email = validateField(email),
#                                         password = hashingPassword(validateField(password)),
#                                         gender = validateField(gender),
#                                         allow_notifications = True,
#                                         invitation_code = generateActvationCode(),
#                                         app_version = validateField(app_version), 
#                                         api_key = generateAPIKey(),
#                                         date_of_birth = validateField(date_of_birth),
#                                         push_token = push_token,
#                                         country_id = validateField(country_id),
#                                         )
#     if profile_img is not None:
#         handle_file_upload(profile_img, 'profile_img', lastId, payload)
             
#     obj = DB_Customer_Users(**payload.dict())
#     db.add(obj)
#     db.commit()
#     db.refresh(obj)

#     if push_token != None:
#         add_new_notification(myHeader.language, lastId, db)
        
#     if referral_code != None:
#         add_points_to_referer(referral_code = referral_code, 
#                           new_attorney_or_customer_id = lastId, 
#                           db = db)
        
#     return generalResponse(message= "Account Created successfully", data=None)

# #############################################################################################

# def validate_existing_user(email, mobile_number, db):
#     if db.query(DB_Customer_Users).filter(DB_Customer_Users.email == email).first():
#         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="User with this email already exists")
#     if db.query(DB_Customer_Users).filter(DB_Customer_Users.mobile_number == mobile_number).first():
#         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="User with this Mobile already exists")
    
# def add_new_notification(language, lastId, db):
#     addNewNotification(user_type = UsersType.customer,
#                                         user_id = lastId,
#                                         currentLanguage = language,
#                                         db = db,
#                                         title_english = "Account Registered Successfully",
#                                         title_arabic = "تم تسجيل الحساب بنجاح",
#                                         content_english = "Welcome To LegalzHub Applications, we are here to hear from you so if you have any suggestions or issues please contact us from the account screen",
#                                         content_arabic = "مرحبًا بك في تطبيقات LegalzHub، نحن هنا لنسمع منك، لذا إذا كان لديك أي اقتراحات أو مشكلات، فيرجى الاتصال بنا من شاشة الحساب"
#                                         )