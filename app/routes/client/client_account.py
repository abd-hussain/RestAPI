from app.models.respond.general import generalResponse
from sqlalchemy.orm import Session
from fastapi import Request, Depends, APIRouter
from app.utils.database import get_db
from app.models.database.client.db_client_user import DB_Client_Users
from app.utils.oauth2 import get_current_user
from app.utils.validation import validateLanguageHeader
from app.utils.generate import generateinvetationCode
from app.models.schemas.client.client_account import UpdateClientAccountModel


router = APIRouter(
    prefix="/client-account",
    tags=["Account"]
)

@router.get("/")
async def get_account(request: Request, db: Session = Depends(get_db), get_current_user: int = Depends(get_current_user)):
    myHeader = validateLanguageHeader(request)
    query = db.query(DB_Client_Users).filter(DB_Client_Users.id == get_current_user.user_id)

    if query.first() == None:
       return generalResponse(message="profile was not found", data=None)

    return generalResponse(message="Profile return successfully", data=query.first())
    
@router.put("/update")
async def update_account(payload: UpdateClientAccountModel , request: Request, db: Session = Depends(get_db), get_current_user: int = Depends(get_current_user)):
    myHeader = validateLanguageHeader(request)
    query = db.query(DB_Client_Users).filter(DB_Client_Users.id == get_current_user.user_id)
    
    if query.first() == None:
       return generalResponse(message="profile was not found", data=None)
   
    if query["invitation_code"] == "" :
        query.update({"invitation_code" : generateinvetationCode()}, synchronize_session=False)
 
    if payload.first_name != None:
        query.update({"first_name" : payload.first_name}, synchronize_session=False)
    if payload.last_name != None:
        query.update({"last_name" : payload.last_name}, synchronize_session=False)
    if payload.mobile_number != None:
        query.update({"mobile_number" : payload.mobile_number}, synchronize_session=False)
    if payload.email != None:
        query.update({"email" : payload.email}, synchronize_session=False)
    if payload.gender != None:
        query.update({"gender" : payload.gender}, synchronize_session=False)
    if payload.referal_code != None:
        query.update({"referal_code" : payload.referal_code}, synchronize_session=False)
    if payload.profile_img != None:
        query.update({"profile_img" : payload.profile_img}, synchronize_session=False)
    if payload.os_type != None:
        query.update({"os_type" : payload.os_type}, synchronize_session=False)
    if payload.device_type_name != None:
        query.update({"device_type_name" : payload.device_type_name}, synchronize_session=False)
    if payload.os_version != None:
        query.update({"os_version" : payload.os_version}, synchronize_session=False)
    if payload.app_version != None:
        query.update({"app_version" : payload.app_version}, synchronize_session=False)
    if payload.date_of_birth != None:
        query.update({"date_of_birth" : payload.date_of_birth}, synchronize_session=False)
    if payload.country_id != None:
        query.update({"country_id" : payload.country_id}, synchronize_session=False)
    if payload.allow_notifications != None:
        query.update({"allow_notifications" : payload.allow_notifications}, synchronize_session=False)
        
    db.commit()
    return generalResponse(message="Profile updated successfully", data=query.first())


   