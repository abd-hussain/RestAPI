# from app.models.database.customer.db_customer_user import DB_Customer_Users
# from app.models.database.db_notifications import DB_Notifications
# from app.models.database.attorney.db_attorney_user import DB_Attorney_Users
# from app.models.database.db_banner import UsersType
# from app.models.schemas.new_notifications import NewNotification
# from app.utils.firebase_notifications.handler import send_push_notification
# from sqlalchemy.orm import Session

    
# def addNewNotification(user_type : UsersType,
#     user_id: int,
#     currentLanguage: str,
#     title_english : str,
#     title_arabic : str,
#     content_english : str,
#     content_arabic : str,
#     db: Session):
        
#     user_model = DB_Attorney_Users if user_type == UsersType.attorney else DB_Customer_Users
#     query = db.query(user_model.push_token).filter(user_model.id == user_id).first()
    
#     user_token = query[0] if query else None
        
#     if user_token:
#         if currentLanguage == "ar":
#             send_push_notification(user_token, title_arabic, content_arabic)
#         else:
#             send_push_notification(user_token, title_english, content_english)    


#     lastId = db.query(DB_Notifications).order_by(DB_Notifications.id.desc()).first().id + 1

#     payload = NewNotification(id=lastId,
#                               title_arabic=title_arabic, 
#                               title_english=title_english, 
#                               content_english=content_english, 
#                               content_arabic=content_arabic,
#                               attorney_owner_id=user_id if user_type == UsersType.attorney else None,
#                               customers_owner_id=user_id if user_type == UsersType.customer else None)

#     obj = DB_Notifications(**payload.dict())
#     db.add(obj)
#     db.commit()