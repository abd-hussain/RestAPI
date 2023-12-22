from app.models.database.client.db_client_user import DB_Client_Users
from app.models.database.db_notifications import DB_Notifications
from app.models.database.mentor.db_mentor_user import DB_Mentor_Users
from app.models.schemas.new_notifications import NewNotification
from app.utils.firebase_notifications.handler import send_push_notification_mentor, send_push_notification_client
from enum import Enum
from sqlalchemy.orm import Session
from app.utils.database import get_db
from fastapi import Depends

class UserType(Enum):
    Mentor = 1
    Client = 2

def addNewNotification(user_type : UserType, userId : int, title : str, body: str, db: Session = Depends(get_db)):
    
    payload = NewNotification(title_arabic = title, title_english = title, 
                              content_english = body, content_arabic = body)
    userToken = ""
    if user_type == UserType.Mentor:
        payload.mentor_owner_id = userId
        query = db.query(DB_Mentor_Users.push_token).filter(DB_Mentor_Users.id == userId).first()
        userToken = query[0] if query else None
        send_push_notification_mentor(userToken, title, body)
    else:
        payload.client_owner_id = userId
        query = db.query(DB_Client_Users.push_token).filter(DB_Client_Users.id == userId).first()
        userToken = query[0] if query else None
        send_push_notification_client(userToken, title, body)


    obj = DB_Notifications(**payload.dict())
    db.add(obj)
    db.commit()
 
