# from fastapi import Request, Depends ,APIRouter, HTTPException, status
# from app.models.database.customer.db_customer_user import DB_Customer_Users
# from app.models.database.attorney.db_attorney_user import DB_Attorney_Users
# from app.utils.database import get_db
# from sqlalchemy.orm import Session
# from typing import Optional
# from app.utils.oauth2 import get_current_user
# from app.utils.validation import validateLanguageHeader
# from app.models.database.db_notifications import DB_Notifications
# from app.models.respond.general import generalResponse

# router = APIRouter(
#     prefix="/notifications",
#     tags=["Notifications"]
# )

# @router.put("/register-token")
# async def update_push_notification_token(token: str, userType: str, db: Session = Depends(get_db), 
#                                          current_user: int = Depends(get_current_user)):
    
#     if userType == "attorney":
#         user_model = DB_Attorney_Users
#     elif userType == "customer":
#         user_model = DB_Customer_Users
#     else:
#         raise HTTPException(
#             status_code=status.HTTP_403_FORBIDDEN, detail="Invalid user type")

#     user = db.query(user_model).filter(user_model.id == current_user.user_id).first()
#     if user:
#         user.push_token = token
#         db.commit()
#         return generalResponse(message="Profile updated successfully", data=user)
#     else:
#         raise HTTPException(
#             status_code=status.HTTP_403_FORBIDDEN, detail="User not found")

# @router.get("/")
# async def get_Notifications(userType: str, request: Request, db: Session = Depends(get_db), current_user: int = Depends(get_current_user), limit: int = 10, skip: int = 0, search: Optional[str] = ""):
#     myHeader = validateLanguageHeader(request)

#     owner_id_column = DB_Notifications.attorney_owner_id if userType == "attorney" else DB_Notifications.customers_owner_id if userType == "customer" else None

#     if not owner_id_column:
#         raise HTTPException(
#             status_code=status.HTTP_403_FORBIDDEN, detail="Invalid user type")
    
#     title_column = DB_Notifications.title_arabic if myHeader.language == "ar" else DB_Notifications.title_english
#     content_column = DB_Notifications.content_arabic if myHeader.language == "ar" else DB_Notifications.content_english
    
#     data = db.query(DB_Notifications.id, title_column.label("title"), content_column.label("content"),
#                     DB_Notifications.created_at).filter(
#         owner_id_column == current_user.user_id, title_column.contains(search)
#     ).limit(limit).offset(skip).all()
    
#     return generalResponse(message="List of notifications returned successfully", data=data)
    
    