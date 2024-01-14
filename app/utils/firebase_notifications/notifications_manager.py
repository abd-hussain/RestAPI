from app.models.database.client.db_client_user import DB_Client_Users
from app.models.database.db_notifications import DB_Notifications
from app.models.database.mentor.db_mentor_user import DB_Mentor_Users
from app.models.schemas.new_notifications import NewNotification
from app.utils.firebase_notifications.handler import send_push_notification_mentor, send_push_notification_client
from enum import Enum
from sqlalchemy.orm import Session

class UserType(Enum):
    Mentor = 1
    Client = 2
    
def addNewNotification(user_type : UserType,
    user_id: int,
    currentLanguage: str,
    title_english : str,
    title_arabic : str,
    content_english : str,
    content_arabic : str,
    db: Session):
    
    user_model = DB_Mentor_Users if user_type == UserType.Mentor else DB_Client_Users
    push_notification_func = send_push_notification_mentor if user_type == UserType.Mentor else send_push_notification_client

    query = db.query(user_model.push_token).filter(user_model.id == user_id).first()
    
    user_token = query[0] if query else None
    
    payload = NewNotification(title_arabic=title_arabic, 
                              title_english=title_english, 
                              content_english=content_english, 
                              content_arabic=content_arabic,
                              mentor_owner_id=user_id if user_type == UserType.Mentor else None,
                              client_owner_id=user_id if user_type == UserType.Client else None)
    
    if user_token:
        if currentLanguage == "ar":
            push_notification_func(user_token, title_arabic, content_arabic)
        else:
            push_notification_func(user_token, title_english, content_english)
            
    obj = DB_Notifications(**payload.dict())
    db.add(obj)
    db.commit()