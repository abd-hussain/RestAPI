from app.models.respond.general import generalResponse
from sqlalchemy.orm import Session
from fastapi import Request, Depends, APIRouter, File, UploadFile, Form
from app.utils.database import get_db
from app.models.database.client.db_client_user import DB_Client_Users
from app.utils.oauth2 import get_current_user
from app.utils.validation import validateLanguageHeader
from app.utils.generate import generateActvationCode
from app.models.schemas.client.client_account import UpdateClientAccountModel
from pydantic import BaseModel, EmailStr, Field
from pydantic.types import SecretStr, constr
from pydantic.networks import EmailStr
from fastapi.encoders import jsonable_encoder

router = APIRouter(
    prefix="/client-account",
    tags=["Account"]
)

@router.get("/")
async def get_account(request: Request, db: Session = Depends(get_db), get_current_user: int = Depends(get_current_user)):
    myHeader = validateLanguageHeader(request)
    print(get_current_user.user_id)
    query = db.query(DB_Client_Users).filter(DB_Client_Users.id == get_current_user.user_id)

    if query.first() == None:
       return generalResponse(message="profile was not found", data=None)

    return generalResponse(message="Profile return successfully", data=query.first())
    
# @router.put("/update")
# async def update_account(payload: UpdateClientAccountModel , request: Request, db: Session = Depends(get_db), get_current_user: int = Depends(get_current_user)):
#     myHeader = validateLanguageHeader(request)
#     query = db.query(DB_Client_Users).filter(DB_Client_Users.id == get_current_user.user_id)
    
#     if query.first() == None:
#        return generalResponse(message="profile was not found", data=None)

#     if query.first().invitation_code is None:
#         query.update({"invitation_code" : generateActvationCode()}, synchronize_session=False)
 
#     if payload.first_name != None:
#         query.update({"first_name" : payload.first_name}, synchronize_session=False)
#     if payload.last_name != None:
#         query.update({"last_name" : payload.last_name}, synchronize_session=False)
#     if payload.mobile_number != None:
#         query.update({"mobile_number" : payload.mobile_number}, synchronize_session=False)
#     if payload.email != None:
#         query.update({"email" : payload.email}, synchronize_session=False)
#     if payload.gender != None:
#         query.update({"gender" : payload.gender}, synchronize_session=False)
#     if payload.referal_code != None:
#         query.update({"referal_code" : payload.referal_code}, synchronize_session=False)
#     if payload.profile_img != None:
#         query.update({"profile_img" : payload.profile_img}, synchronize_session=False)
#     if payload.os_type != None:
#         query.update({"os_type" : payload.os_type}, synchronize_session=False)
#     if payload.device_type_name != None:
#         query.update({"device_type_name" : payload.device_type_name}, synchronize_session=False)
#     if payload.os_version != None:
#         query.update({"os_version" : payload.os_version}, synchronize_session=False)
#     if payload.app_version != None:
#         query.update({"app_version" : payload.app_version}, synchronize_session=False)
#     if payload.date_of_birth != None:
#         query.update({"date_of_birth" : payload.date_of_birth}, synchronize_session=False)
#     if payload.country_id != None:
#         query.update({"country_id" : payload.country_id}, synchronize_session=False)
#     if payload.allow_notifications != None:
#         query.update({"allow_notifications" : payload.allow_notifications}, synchronize_session=False)
        
#     db.commit()
#     return generalResponse(message="Profile updated successfully", data=query.first())



@router.put("/update")
async def update_account(request: Request,first_name: str = Form(None),last_name: str = Form(None),email: str = Form(None),gender: int = Form(None),
                         country_id: int = Form(None), referal_code: str = Form(None),date_of_birth: str = Form(None),profile_picture: UploadFile = File(None), 
                         os_type: str = Form(""),device_type_name: str = Form(""),app_version: str = Form(""),
                         db: Session = Depends(get_db), get_current_user: int = Depends(get_current_user)):
    myHeader = validateLanguageHeader(request)
    query = db.query(DB_Client_Users).filter(DB_Client_Users.id == get_current_user.user_id)
    payload = UpdateClientAccountModel(first_name = first_name, last_name = last_name, email = email, date_of_birth = date_of_birth, 
                                     country_id = country_id, gender = gender, referal_code = referal_code, 
                                      os_type = os_type, device_type_name = device_type_name, app_version = app_version)
    
    if query.first().invitation_code is None:
        query.update({"invitation_code" : generateActvationCode()}, synchronize_session=False)

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
    # if profile_picture is not None:
    #     marketplace_domain = await get_request_source(request)
    #     upload_path = marketplace_domain + "/users/" + instance.username
    #     if not await upload_file(profile_picture, upload_path, settings.ALLOWED_IMAGE_TYPES, settings.FILE_SERVICE):
    #         raise HTTPException(detail=”file could not be uploaded”,status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    #     update_data[“profile_picture”] = upload_path + “/” + profile_picture.filename



