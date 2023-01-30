from fastapi import Request, Depends, APIRouter
from sqlalchemy.orm import Session
from app.utils.database import get_db
from app.utils.validation import validateLanguageHeader
from app.models.database.db_messages import DB_Messages, DB_Chat, SendedFrom
from app.models.database.client.db_client_user import DB_Client_Users
from app.models.database.mentor.db_mentor_user import DB_Mentor_Users
from app.models.respond.general import generalResponse
from app.utils.oauth2 import get_current_user
from app.models.schemas.message import Message

router = APIRouter(
    prefix="/messages",
    tags=["Messages"]
)

@router.get("/client")
async def get_messages_client(request: Request, db: Session = Depends(get_db), get_current_user: int = Depends(get_current_user)):
    myHeader = validateLanguageHeader(request)
    query = db.query(DB_Messages.id, DB_Messages.client_id, DB_Messages.mentor_id, 
                     DB_Mentor_Users.suffixe_name, DB_Mentor_Users.first_name, DB_Mentor_Users.last_name, DB_Mentor_Users.profile_img
                     ).filter(DB_Messages.client_id == get_current_user.user_id)\
                         .join(DB_Mentor_Users, DB_Mentor_Users.id == DB_Messages.mentor_id, isouter=True).all()
    return generalResponse(message="list of messages return successfully", data=query)

@router.get("/mentor")
async def get_messages_mentor(request: Request, db: Session = Depends(get_db), get_current_user: int = Depends(get_current_user)):
    myHeader = validateLanguageHeader(request)
    query = db.query(DB_Messages.id, DB_Messages.client_id, DB_Messages.mentor_id, 
                     DB_Client_Users.first_name, DB_Client_Users.last_name, DB_Client_Users.profile_img
                     ).filter(DB_Messages.mentor_id == get_current_user.user_id)\
                         .join(DB_Client_Users, DB_Client_Users.id == DB_Messages.client_id, isouter=True).all()
   
    return generalResponse(message="list of messages return successfully", data=query)

@router.get("/chat")
async def get_chat_mentor(message_id: int,request: Request, db: Session = Depends(get_db), get_current_user: int = Depends(get_current_user)):
    myHeader = validateLanguageHeader(request)
    query = db.query(DB_Chat).filter(DB_Chat.message_id == message_id).all()
    return generalResponse(message="list of messages return successfully", data=query)

@router.post("/client")
async def send_messages_client(payload: Message,request: Request, db: Session = Depends(get_db), get_current_user: int = Depends(get_current_user)):
    myHeader = validateLanguageHeader(request)
    payload.sendit = SendedFrom.client
    obj = DB_Chat(**payload.dict())
    db.add(obj) 
    db.commit()
    return generalResponse(message="messages send successfully", data=None)

@router.post("/mentor")
async def send_messages_mentor(payload: Message,request: Request, db: Session = Depends(get_db), get_current_user: int = Depends(get_current_user)):
    myHeader = validateLanguageHeader(request)
    payload.sendit = SendedFrom.mentor
    obj = DB_Chat(**payload.dict())
    db.add(obj) 
    db.commit()
    return generalResponse(message="messages send successfully", data=None)