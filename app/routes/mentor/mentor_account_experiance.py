from fastapi import Depends ,APIRouter, Request, Form, File, UploadFile, HTTPException, status
from sqlalchemy.orm import Session
from app.models.database.db_category import DB_Categories
from app.utils.validation import validateLanguageHeader
from app.utils.database import get_db
from app.models.database.mentor.db_mentor_user import DB_Mentor_Users
from app.utils.oauth2 import get_current_user
from app.models.respond.general import generalResponse
from app.utils.validate_field import validateField
from app.utils.file_upload import edit_file_uploaded

router = APIRouter(
    prefix="/mentor-account",
    tags=["Account"]
)
    
@router.get("/exp-info")
async def get_account_experinace(request: Request, db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
    myHeader = validateLanguageHeader(request)
    
    category_name_field = DB_Categories.name_english.label("category_name") if myHeader.language == "en" else DB_Categories.name_arabic.label("category_name")

    mentor_experience = db.query(DB_Mentor_Users.cv, 
                     DB_Mentor_Users.cert1, DB_Mentor_Users.cert2, DB_Mentor_Users.cert3,
                     DB_Mentor_Users.majors, DB_Mentor_Users.experience_since,
                     DB_Mentor_Users.category_id,
                     category_name_field)\
                         .join(DB_Categories, DB_Categories.id == DB_Mentor_Users.category_id, isouter=True)\
                         .filter(DB_Mentor_Users.id == current_user.user_id).first()
                         
    if mentor_experience == None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="profile was not found")

    return generalResponse(message="Profile Experiances return successfully", data=mentor_experience)

@router.put("/exp-info")
async def update_account_experinace(experience_since: str = Form(None), 
                                    majors:list[int] = [],
                                category_id: int = Form(None),
                                cv: UploadFile = File(default=None), 
                                cert1: UploadFile = File(default=None), 
                                cert2: UploadFile = File(default=None),
                                cert3: UploadFile = File(default=None),
                                    db: Session = Depends(get_db), 
                                    current_user: int = Depends(get_current_user)):


    query = db.query(DB_Mentor_Users).filter(DB_Mentor_Users.id == current_user.user_id).first()
    
    if query == None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="profile was not found")
   
    query.experience_since = validateField(experience_since)
    query.majors = validateField(majors)
    query.category_id = validateField(category_id)
    
    if cv is not None:
        query.cv = edit_file_uploaded(validateField(cv), 'cv', current_user.user_id)
    
    if cert1 is not None:
        query.cert1 = edit_file_uploaded(validateField(cert1), 'cert1', current_user.user_id)
    
    if cert2 is not None:
        query.cert2 = edit_file_uploaded(validateField(cert2), 'cert2', current_user.user_id)
    
    if cert3 is not None:
        query.cert3 = edit_file_uploaded(validateField(cert3), 'cert3', current_user.user_id)
             
    db.commit()

    return generalResponse(message="Experiances updated successfully", data=None)