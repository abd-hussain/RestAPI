from fastapi import Depends ,APIRouter, Request, Form, File, UploadFile, HTTPException, status
from sqlalchemy.orm import Session
from app.models.database.db_category import DB_Categories
from app.utils.validation import validateFileType, validateLanguageHeader
from app.utils.database import get_db
from app.models.database.mentor.db_mentor_user import DB_Mentor_Users

from app.utils.oauth2 import get_current_user
from app.models.respond.general import generalResponse

router = APIRouter(
    prefix="/mentor-account",
    tags=["Account"]
)

@router.get("/exp-info")
async def get_account_experinace(request: Request, db: Session = Depends(get_db), get_current_user: int = Depends(get_current_user)):
    myHeader = validateLanguageHeader(request)

    query = db.query(DB_Mentor_Users.cv, 
                     DB_Mentor_Users.cert1, DB_Mentor_Users.cert2, DB_Mentor_Users.cert3,
                     DB_Mentor_Users.majors, DB_Mentor_Users.experience_since,
                     DB_Categories.name_english.label("category_name"))\
                         .filter(DB_Mentor_Users.id == get_current_user.user_id).first()
    if (myHeader.language == "ar"):
        query = db.query(DB_Mentor_Users.cv, 
                     DB_Mentor_Users.cert1, DB_Mentor_Users.cert2, DB_Mentor_Users.cert3,
                     DB_Mentor_Users.majors, DB_Mentor_Users.experience_since,
                     DB_Categories.name_arabic.label("category_name"))\
                         .filter(DB_Mentor_Users.id == get_current_user.user_id).first()
                         
    if query == None:
       return generalResponse(message="profile was not found", data=None)

    return generalResponse(message="Profile return successfully", data=query)

@router.put("/exp-info")
async def update_account_experinace(experience_since: str = Form(None), majors:list[int] = [],
                         cv: UploadFile = File(default=None), 
                         cert1: UploadFile = File(default=None), 
                         cert2: UploadFile = File(default=None),
                         cert3: UploadFile = File(default=None),
                         db: Session = Depends(get_db), get_current_user: int = Depends(get_current_user)):

    query = db.query(DB_Mentor_Users).filter(DB_Mentor_Users.id == get_current_user.user_id)
    
    if experience_since != None:
        query.update({"experience_since" : experience_since}, synchronize_session=False)
    if majors != None:
        query.update({"majors" : majors}, synchronize_session=False)
        
    if cv is not None:
        fileExtension = validateFileType(cv, "cv")
        cv_file_location = f"static/mentorsCVs/{get_current_user.user_id}{fileExtension}"

        try:
            contents_cv = cv.file.read()
            with open(cv_file_location, 'wb+') as out_file:
                out_file.write(contents_cv)
                query.update({"cv" : f"{get_current_user.user_id}{fileExtension}"}, synchronize_session=False)
        except Exception:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="There was an error uploading the CV file")
        finally:
             cv.file.close()
             
    if cert1 is not None:
        cert1Extension = validateFileType(cert1, "cert1")
        cert1_file_location = f"static/mentorsCerts/{get_current_user.user_id}-cer1{cert1Extension}"

        try:
            contents_cert1 = cert1.file.read()
            with open(cert1_file_location, 'wb+') as out_file:
                out_file.write(contents_cert1)
                query.update({"cert1" : f"{get_current_user.user_id}-cer1{cert1Extension}"}, synchronize_session=False)
        except Exception:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="There was an error uploading the cert1 file")
        finally:
             cert1.file.close()
             
    if cert2 is not None:
        cert2Extension = validateFileType(cert2, "cert2")
        cert2_file_location = f"static/mentorsCerts/{get_current_user.user_id}-cer2{cert2Extension}"

        try:
            contents_cert2 = cert2.file.read()
            with open(cert2_file_location, 'wb+') as out_file:
                out_file.write(contents_cert2)
                query.update({"cert2" : f"{get_current_user.user_id}-cer2{cert2Extension}"}, synchronize_session=False)
        except Exception:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="There was an error uploading the cert2 file")
        finally:
             cert2.file.close()
             
    if cert3 is not None:
        cert3Extension = validateFileType(cert3, "cert3")
        cert3_file_location = f"static/mentorsCerts/{get_current_user.user_id}-cer3{cert3Extension}"

        try:
            contents_cert3 = cert3.file.read()
            with open(cert3_file_location, 'wb+') as out_file:
                out_file.write(contents_cert3)
                query.update({"cert3" : f"{get_current_user.user_id}-cer3{cert3Extension}"}, synchronize_session=False)
        except Exception:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="There was an error uploading the cert3 file")
        finally:
             cert3.file.close()

    db.commit()

    return generalResponse(message="Experiances updated successfully", data=None)