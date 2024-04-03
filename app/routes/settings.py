
from fastapi import Request, Depends, APIRouter, status, HTTPException
from sqlalchemy.orm import Session
from app.models.schemas.leads import ListLeads
from app.models.database.db_leads import DB_Leads
from app.models.respond.general import generalResponse
from app.utils.database import get_db
from app.models.schemas.attorney_account import ChangePassword
from app.models.schemas.attorney_account import ForgotPassword
from app.models.database.attorney.db_attorney_user import DB_Attorney_Users
from app.models.database.customer.db_customer_user import DB_Customer_Users
from app.utils.oauth2 import verifyPassword
from app.utils.send_email import send_email
# from app.utils.firebase_notifications.notifications_manager import UserType, addNewNotification
from app.utils.oauth2 import get_current_user

router = APIRouter(
    prefix="/settings",
    tags=["Settings"]
)

@router.post("/leads", status_code=status.HTTP_201_CREATED)
async def upload_leads(payload: ListLeads, db: Session = Depends(get_db)):    
    
    existing_mobile_numbers = db.query(DB_Leads.mobile_number).filter(
        DB_Leads.mobile_number.in_([lead.mobile_number for lead in payload.list])
    ).all()
    
    existing_mobile_numbers_set = {number[0] for number in existing_mobile_numbers}
    new_leads = [DB_Leads(**lead.dict()) for lead in payload.list if lead.mobile_number not in existing_mobile_numbers_set]

    if new_leads:
        db.add_all(new_leads)
        db.commit()
    return generalResponse(message= "successfully created leads", data= None)

@router.post('/forgotpassword')
def forgotPassword(payload: ForgotPassword, db: Session = Depends(get_db)):
    
    attorney_user = db.query(DB_Attorney_Users).filter(DB_Attorney_Users.email == payload.email)
    customer_user = db.query(DB_Customer_Users).filter(DB_Customer_Users.email == payload.email)
    
    if not attorney_user.first() and not customer_user.first():
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="User not found")
    
    if attorney_user.first():
        send_email(payload.email, attorney_user.first().password)
        
    if customer_user.first():
        send_email(payload.email, customer_user.first().password)
    
    return generalResponse(message= "Email send successfully", data=None)

        
@router.put("/changepassword")
async def change_password(payload: ChangePassword, db: Session = Depends(get_db), 
                          current_user: int = Depends(get_current_user)):
    
    if payload.userType == "attorney":
        user_model = DB_Attorney_Users
    elif payload.userType == "customer":
        user_model = DB_Customer_Users
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Invalid user type")
        
    user = db.query(user_model).filter(user_model.id == current_user.user_id).first()

    if not user or not verifyPassword(payload.oldpassword, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")
    
    if payload.newpassword:
        user.password = payload.newpassword
        db.commit()
        # addNewNotification(user_type=UserType.Attorney,
        #                                 user_id=current_user.user_id,
        #                                 currentLanguage=myHeader.language,
        #                                 db=db,
        #                                 title_english="Change Password",
        #                                 title_arabic="تغيير كلمة المرور",
        #                                 content_english="Your Password change successfully",
        #                                 content_arabic="تم تغيير كلمة المرور الخاصة بك بنجاح")
        return generalResponse(message="Password changed successfully", data=None)
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="New password is required")

@router.delete("/delete")
async def delete_account(userType: str, db: Session = Depends(get_db), 
                         current_user: int = Depends(get_current_user)):
    
    if userType == "attorney":
        user_model = DB_Attorney_Users
    elif userType == "customer":
        user_model = DB_Customer_Users
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Invalid user type")
    
    user = db.query(user_model).filter(user_model.id == current_user.user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    db.delete(user)
    db.commit()

    return generalResponse(message="Profile deleted successfully", data=None)