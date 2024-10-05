from app.models.schemas.report import Report
from app.models.respond.general import generalResponse
from sqlalchemy.orm import Session
from fastapi import Request, Depends ,APIRouter, Form, HTTPException, status,File, UploadFile
from app.utils.database import get_db
from app.models.database.db_issue_reported import DB_Issues_Reported
from app.utils.validation import validateImageType
from app.utils.time import current_milli_time
from app.utils.validation import validate_headers
from app.utils.validate_field import validateField

router = APIRouter(
    prefix="/report",
    tags=["Report"]
)

@router.post("/issue", status_code=status.HTTP_201_CREATED)
async def create_issue(request: Request, 
                       content: str = Form(None),
                       attach1:  UploadFile = File(default=None),
                       attach2: UploadFile = File(default=None),
                       attach3: UploadFile = File(default=None),
                       db: Session = Depends(get_db)):
    
    myHeader = validate_headers(request)
    
    lastId = db.query(DB_Issues_Reported).order_by(DB_Issues_Reported.id.desc()).first().id + 1

    payload = Report(id = lastId,
                     content =  validateField(content), 
                     api_key = myHeader.api_key)

    payload.attachment1 = save_attachment(attach1, REPORTS_DIR)
    payload.attachment2 = save_attachment(attach2, REPORTS_DIR)
    payload.attachment3 = save_attachment(attach3, REPORTS_DIR)
        
    obj = DB_Issues_Reported(**payload.dict())
    db.add(obj)
    db.commit()
    return generalResponse(message= "successfully created issue", data= None)

#############################################################################################

REPORTS_DIR = "static/reports/"
        
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
