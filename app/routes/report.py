from app.models.schemas.report import Report
from app.models.respond.general import generalResponse
from sqlalchemy.orm import Session
from fastapi import Request, Depends, APIRouter, File, UploadFile, Form, HTTPException, status
from app.utils.database import get_db
from app.models.database import db_suggestion_reported, db_issue_reported
from app.models.database.client.db_client_user import DB_Client_Users
from app.models.database.mentor.db_mentor_user import DB_Mentor_Users
from app.utils.validation import validateLanguageHeader
from app.utils.time import current_milli_time

router = APIRouter(
    prefix="/report",
    tags=["Report"]
)

@router.post("/issue", status_code=status.HTTP_201_CREATED)
async def create_issue(request: Request,
                       content: str = Form(None),
                       client_user_id: int = Form(None),
                       mentor_user_id: int = Form(None),
                       attach1:  UploadFile = File(default=None),
                       attach2: UploadFile = File(default=None),
                       attach3: UploadFile = File(default=None),
                       db: Session = Depends(get_db)):
    
        payload = Report(content = content)
        if client_user_id != None:
            client_query = db.query(DB_Client_Users).filter(DB_Client_Users.id == client_user_id).first()
            if (client_query != None):
                 payload.client_owner_id = client_query.id
                 
        if mentor_user_id != None:
            mentor_query = db.query(DB_Mentor_Users).filter(DB_Mentor_Users.id == mentor_user_id).first()
            if (client_query != None):
                 payload.mentor_owner_id = mentor_query.id
            
        if attach1 is not None:
            validateImageType(attach1, "attach1")
            file1_location = getImageName()
            
            try:
                contents1 = attach1.file.read()
                with open(file1_location, 'wb+') as out_file1:
                    out_file1.write(contents1)
                    payload.attachment1 = file1_location
            except Exception:
                return {"message": "There was an error uploading the file"}
            finally:
                attach1.file.close()
            
        if attach2 is not None:
            validateImageType(attach2, "attach2")
            file2_location = getImageName()
            
            try:
                contents2 = attach2.file.read()
                with open(file2_location, 'wb+') as out_file2:
                    out_file2.write(contents2)
                    payload.attachment2 = file2_location
            except Exception:
                return {"message": "There was an error uploading the file"}
            finally:
                attach2.file.close()
                
        if attach3 is not None:
            validateImageType(attach3, "attach3")
            file3_location = getImageName()
            
            try:
                contents3 = attach3.file.read()
                with open(file3_location, 'wb+') as out_file3:
                    out_file3.write(contents3)
                    payload.attachment3 = file3_location
            except Exception:
                return {"message": "There was an error uploading the file"}
            finally:
                attach3.file.close()
                
        obj = db_issue_reported.DB_Issues_Reported(**payload.dict())
        db.add(obj)
        db.commit()
        return generalResponse(message= "successfully created issue", data= None)
        
@router.post("/suggestion", status_code=status.HTTP_201_CREATED)
def create_suggestion(request: Request,
                       content: str = Form(None),
                       client_user_id: int = Form(None),
                       mentor_user_id: int = Form(None),
                       attach1:  UploadFile = File(default=None),
                       attach2: UploadFile = File(default=None),
                       attach3: UploadFile = File(default=None),
                       db: Session = Depends(get_db)):  
    
    payload = Report(content = content)
    if client_user_id != None:
        client_query = db.query(DB_Client_Users).filter(DB_Client_Users.id == client_user_id).first()
        if (client_query != None):
            payload.client_owner_id = client_query.id
            
    if mentor_user_id != None:
        mentor_query = db.query(DB_Mentor_Users).filter(DB_Mentor_Users.id == mentor_user_id).first()
        if (client_query != None):
             payload.mentor_owner_id = mentor_query.id
                 
    if attach1 is not None:
        validateImageType(attach1, "attach1")
        file1_location = getImageName()
            
        try:
            contents1 = attach1.file.read()
            with open(file1_location, 'wb+') as out_file1:
                out_file1.write(contents1)
                payload.attachment1 = file1_location
        except Exception:
            return {"message": "There was an error uploading the file"}
        finally:
            attach1.file.close()
            
    if attach2 is not None:
        validateImageType(attach2, "attach2")
        file2_location = getImageName()
            
        try:
            contents2 = attach2.file.read()
            with open(file2_location, 'wb+') as out_file2:
                out_file2.write(contents2)
                payload.attachment2 = file2_location
        except Exception:
            return {"message": "There was an error uploading the file"}
        finally:
            attach2.file.close()
                
    if attach3 is not None:
        validateImageType(attach3, "attach3")
        file3_location = getImageName()
            
        try:
            contents3 = attach3.file.read()
            with open(file3_location, 'wb+') as out_file3:
                out_file3.write(contents3)
                payload.attachment3 = file3_location
        except Exception:
            return {"message": "There was an error uploading the file"}
        finally:
            attach3.file.close()

    obj = db_suggestion_reported.DB_Suggestion_Reported(**payload.dict())
    db.add(obj)
    db.commit()
    return generalResponse(message= "successfully created suggestion", data= None)


def getImageName() -> str:
    return f"static/suggestions/{current_milli_time()}.png"

def validateImageType(image: Form(None), imageName: str) -> Form(None):
    if image.content_type not in ["image/jpeg", "image/png", "image/jpg", "image/JPG"]:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail= imageName + " Format is not valid")
    else:
        return image
