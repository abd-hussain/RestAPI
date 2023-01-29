from fastapi import Request, Depends, APIRouter, HTTPException, status
from sqlalchemy.orm import Session
from app.utils.database import get_db
from app.utils.validation import validateLanguageHeader
from app.models.database.db_messages import DB_Messages, SendedFrom
from app.models.respond.general import generalResponse
from app.utils.oauth2 import get_current_user
from app.models.schemas.message import Message

router = APIRouter(
    prefix="/messages",
    tags=["Messages"]
)

@router.get("/client")
async def get_messages_client(mentor_id: int,request: Request, db: Session = Depends(get_db), get_current_user: int = Depends(get_current_user)):
    myHeader = validateLanguageHeader(request)
    query = db.query(DB_Messages).filter(DB_Messages.client_id == get_current_user.user_id).filter(
        DB_Messages.mentor_id == mentor_id).all()
    return generalResponse(message="list of messages return successfully", data=query)

@router.post("/client")
async def send_messages_client(payload: Message,request: Request, db: Session = Depends(get_db), get_current_user: int = Depends(get_current_user)):
    myHeader = validateLanguageHeader(request)
    payload.sendit = SendedFrom.client
    obj = DB_Messages(**payload.dict())
    db.add(obj) 
    db.commit()
    return generalResponse(message="messages send successfully", data=None)

@router.get("/mentor")
async def get_messages_mentor(client_id: int,request: Request, db: Session = Depends(get_db), get_current_user: int = Depends(get_current_user)):
    myHeader = validateLanguageHeader(request)
    query = db.query(DB_Messages).filter(DB_Messages.mentor_id == get_current_user.user_id).filter(
        DB_Messages.client_id == client_id).all()
    return generalResponse(message="list of messages return successfully", data=query)

@router.post("/mentor")
async def send_messages_mentor(payload: Message,request: Request, db: Session = Depends(get_db), get_current_user: int = Depends(get_current_user)):
    myHeader = validateLanguageHeader(request)
    payload.sendit = SendedFrom.mentor
    obj = DB_Messages(**payload.dict())
    db.add(obj) 
    db.commit()
    return generalResponse(message="messages send successfully", data=None)