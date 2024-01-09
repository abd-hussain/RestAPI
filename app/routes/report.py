from app.models.schemas.report import Report
from app.models.respond.general import generalResponse
from sqlalchemy.orm import Session
from fastapi import HTTPException, Depends, APIRouter, File, UploadFile, Form, status
from app.utils.database import get_db
from app.models.database.db_suggestion_reported import DB_Suggestion_Reported
from app.models.database.db_issue_reported import DB_Issues_Reported
from app.models.database.client.db_client_user import DB_Client_Users
from app.models.database.mentor.db_mentor_user import DB_Mentor_Users
from app.utils.validation import validateImageType
from app.utils.time import current_milli_time

router = APIRouter(
    prefix="/report",
    tags=["Report"]
)

@router.post("/issue", status_code=status.HTTP_201_CREATED)
async def create_issue(content: str = Form(None),
                       client_user_id: str = Form(None),
                       mentor_user_id: str = Form(None),
                       attach1:  UploadFile = File(default=None),
                       attach2: UploadFile = File(default=None),
                       attach3: UploadFile = File(default=None),
                       db: Session = Depends(get_db)):
    
        payload = Report(content = content)
        payload.client_owner_id = process_user_id(client_user_id, db, DB_Client_Users)
        payload.mentor_owner_id = process_user_id(mentor_user_id, db, DB_Mentor_Users)
        payload.attachment1 = save_attachment(attach1, REPORTS_DIR)
        payload.attachment2 = save_attachment(attach2, REPORTS_DIR)
        payload.attachment3 = save_attachment(attach3, REPORTS_DIR)
                
        obj = DB_Issues_Reported(**payload.dict())
        db.add(obj)
        db.commit()
        return generalResponse(message= "successfully created issue", data= None)
        
@router.post("/suggestion", status_code=status.HTTP_201_CREATED)
def create_suggestion(content: str = Form(None),
                       client_user_id: str = Form(None),
                       mentor_user_id: str = Form(None),
                       attach1:  UploadFile = File(default=None),
                       attach2: UploadFile = File(default=None),
                       attach3: UploadFile = File(default=None),
                       db: Session = Depends(get_db)):  
    
    payload = Report(content = content)
    payload.client_owner_id = process_user_id(client_user_id, db, DB_Client_Users)
    payload.mentor_owner_id = process_user_id(mentor_user_id, db, DB_Mentor_Users)
    payload.attachment1 = save_attachment(attach1, SUGGESTIONS_DIR)
    payload.attachment2 = save_attachment(attach2, SUGGESTIONS_DIR)
    payload.attachment3 = save_attachment(attach3, SUGGESTIONS_DIR) 

    obj = DB_Suggestion_Reported(**payload.dict())
    db.add(obj)
    db.commit()
    return generalResponse(message= "successfully created suggestion", data= None)

#############################################################################################

SUGGESTIONS_DIR = "static/suggestions/"
REPORTS_DIR = "static/reports/"

def process_user_id(user_id: str, db: Session, model) -> int:
    if user_id is not None:
        int_id = int(user_id)
        query = db.query(model).filter(model.id == int_id).first()
        if query is not None:
            return int_id
        
def save_attachment(attachment: UploadFile, directory: str) -> str:
    if attachment is not None:
        extension = validateImageType(attachment, attachment.filename)
        file_location = get_image_name(extension, directory)
        try:
            with open(file_location, 'wb+') as out_file:
                out_file.write(attachment.file.read())
            return file_location
        except Exception as e:
            raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        finally:
            attachment.file.close()

def get_image_name(extension: str, directory: str) -> str:
    return f"{directory}{current_milli_time()}{extension}"
