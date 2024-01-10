from app.models.respond.general import generalResponse
from sqlalchemy.orm import Session
from fastapi import Request, Depends, APIRouter, File, UploadFile, Form, HTTPException, status
from app.utils.database import get_db
from app.models.database.client.db_client_user import DB_Client_Users
from app.utils.oauth2 import get_current_user
from app.utils.validation import validateLanguageHeader
from app.utils.generate import generateActvationCode
from app.models.database.db_country import DB_Countries
from app.utils.add_point import add_points_to_referer
from app.utils.file_upload import edit_file_uploaded

router = APIRouter(
    prefix="/client-account",
    tags=["Account"]
)

@router.get("/")
async def get_account_info(request: Request, db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
    myHeader = validateLanguageHeader(request)

    country_column = DB_Countries.name_arabic if myHeader.language == "ar" else DB_Countries.name_english
    currency_column = DB_Countries.currency_arabic if myHeader.language == "ar" else DB_Countries.currency_english

    user = db.query(DB_Client_Users.id, DB_Client_Users.first_name, 
                     DB_Client_Users.last_name, DB_Client_Users.invitation_code, 
                     DB_Client_Users.profile_img, DB_Client_Users.points,
                     DB_Client_Users.mobile_number, DB_Client_Users.email,
                     DB_Client_Users.gender, DB_Client_Users.date_of_birth,
                     DB_Client_Users.allow_notifications, DB_Client_Users.country_id, 
                     DB_Countries.flag_image,
                     country_column.label("country_name"),
                     currency_column.label("currency"),
                     ).join(DB_Countries, DB_Client_Users.country_id == DB_Countries.id, isouter=True)\
                        .filter(DB_Client_Users.id == current_user.user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="profile was not found")

    return generalResponse(message="Profile return successfully", data=user)


@router.delete("/delete")
async def delete_account(db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
    user = db.query(DB_Client_Users).filter(DB_Client_Users.id == current_user.user_id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
   
    db.delete(user)
    db.commit()
    return generalResponse(message="Profile deleted successfully", data=None)

@router.put("/update")
async def update_account_info(first_name: str = Form(None),
                              last_name: str = Form(None),
                              gender: int = Form(None),
                        country_id: int = Form(None), 
                        referral_code: str = Form(None),
                        date_of_birth: str = Form(None),
                        profile_img: UploadFile = File(None), 
                        allow_notifications: bool = Form(None),
                        db: Session = Depends(get_db), 
                        current_user: int = Depends(get_current_user)):
    
    query_account = db.query(DB_Client_Users).filter(DB_Client_Users.id == current_user.user_id).first()
    
    if not query_account:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="profile was not found")
        
    if query_account.invitation_code is None:
        query_account.invitation_code = generateActvationCode()
        
    if first_name is not None:
        query_account.first_name = first_name
        
    if last_name is not None:
        query_account.last_name = last_name
        
    if gender is not None:
        query_account.gender = gender
        
    if country_id is not None:
        query_account.country_id = country_id
        
    if date_of_birth is not None:
        query_account.date_of_birth = date_of_birth
        
    if allow_notifications is not None:
        query_account.allow_notifications = allow_notifications

    if profile_img is not None:
        query_account.profile_img = edit_file_uploaded(profile_img, 
                                                       'client_profile_img', 
                                                       current_user.user_id)
    db.commit()
    
    add_points_to_referer(referral_code = referral_code, 
                          new_mentor_client_id = current_user.user_id, 
                          db = db)
    
    return generalResponse(message="Profile updated successfully", data=query_account)




