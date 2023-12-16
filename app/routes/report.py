from app.models.schemas.report import Report
from app.models.respond.general import generalResponse
from sqlalchemy.orm import Session
from fastapi import Request, Depends, APIRouter, File, UploadFile, Form, status
from app.utils.database import get_db
from app.models.database import db_suggestion_reported, db_issue_reported
from app.models.database.client.db_client_user import DB_Client_Users
from app.models.database.mentor.db_mentor_user import DB_Mentor_Users
from app.utils.validation import validateImageType
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
            my_int = int(client_user_id)
            client_query = db.query(DB_Client_Users).filter(DB_Client_Users.id == my_int).first()
            if (client_query != None):
                 payload.client_owner_id = client_query.id
                 
        if mentor_user_id != None:
            my_int = int(mentor_user_id)
            mentor_query = db.query(DB_Mentor_Users).filter(DB_Mentor_Users.id == my_int).first()
            if (client_query != None):
                 payload.mentor_owner_id = mentor_query.id
            
        if attach1 is not None:
            attach1Extension = validateImageType(attach1, "attach1")
            file1_location = getReportImageName(attach1Extension)
            
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
            attach2Extension = validateImageType(attach2, "attach2")
            file2_location = getReportImageName(attach2Extension)
            
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
            attach3Extension = validateImageType(attach3, "attach3")
            file3_location = getReportImageName(attach3Extension)
            
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
        my_int = int(client_user_id)
        client_query = db.query(DB_Client_Users).filter(DB_Client_Users.id == my_int).first()
        if (client_query != None):
            payload.client_owner_id = client_query.id
            
    if mentor_user_id != None:
        my_int = int(mentor_user_id)
        mentor_query = db.query(DB_Mentor_Users).filter(DB_Mentor_Users.id == my_int).first()
        if (client_query != None):
             payload.mentor_owner_id = mentor_query.id
                 
    if attach1 is not None:
        attach1Extension = validateImageType(attach1, "attach1")
        file1_location = getSuggestionsImageName(attach1Extension)
            
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
        attach2Extension = validateImageType(attach2, "attach2")
        file2_location = getSuggestionsImageName(attach2Extension)
            
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
        attach3Extension = validateImageType(attach3, "attach3")
        file3_location = getSuggestionsImageName(attach3Extension)
            
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


def getSuggestionsImageName(extinsion : str) -> str:
    return f"static/suggestions/{current_milli_time()}{extinsion}"

def getReportImageName(extinsion : str) -> str:
    return f"static/reports/{current_milli_time()}{extinsion}"
