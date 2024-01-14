from fastapi import Request, Depends ,APIRouter, HTTPException, status
from sqlalchemy.orm import Session
from app.utils.database import get_db
from app.models.database.mentor.db_mentor_user import DB_Mentor_Users
from app.models.database.mentor.db_mentor_review import DB_Mentor_Review
from app.models.schemas.mentor_account import MentorChangePassword
from app.models.schemas.mentor_account import MentorForgotPassword
from app.utils.oauth2 import get_current_user
from app.models.respond.general import generalResponse
from app.utils.oauth2 import verifyPassword
from app.utils.send_email import send_email
from app.utils.firebase_notifications.notifications_manager import UserType, addNewNotification
from app.utils.validation import validateLanguageHeader
from app.models.database.client.db_client_user import DB_Client_Users
from app.models.database.db_country import DB_Countries
from app.models.database.db_appointment import DB_Appointments, AppointmentsState

router = APIRouter(
    prefix="/mentor-settings",
    tags=["Account"]
)

@router.get('/review')
def getMentorReview(db: Session = Depends(get_db), 
                         current_user: int = Depends(get_current_user)):
    
    query = db.query(DB_Mentor_Review.id, DB_Mentor_Review.client_id, DB_Mentor_Review.stars, 
                      DB_Mentor_Review.comment, DB_Mentor_Review.mentor_response, 
                      DB_Mentor_Review.created_at,
                      DB_Client_Users.profile_img, DB_Client_Users.first_name, DB_Client_Users.last_name,
                      DB_Client_Users.country_id, DB_Countries.flag_image
                     ).join(DB_Client_Users, DB_Client_Users.id == DB_Mentor_Review.client_id, isouter=True)\
                         .join(DB_Countries, DB_Countries.id == DB_Client_Users.country_id, isouter=True).filter(
                         DB_Mentor_Review.mentor_id == current_user.user_id).all()
   
    return generalResponse(message= "All reviews return successfully", data=query)


@router.put('/review-response')
def getMentorReview(id: int, response: str, db: Session = Depends(get_db), 
                         current_user: int = Depends(get_current_user)):
    

    review = db.query(DB_Mentor_Review).filter(DB_Mentor_Review.id == id, DB_Mentor_Review.mentor_id == current_user.user_id).first()
    
    if review is None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Review Not Exsist")
    
    review.mentor_response = response
    db.commit()
   
    return generalResponse(message= "Review updated successfully", data=None)

@router.post('/forgotpassword')
def forgotPassword(payload: MentorForgotPassword, db: Session = Depends(get_db)):
    user = db.query(DB_Mentor_Users).filter(DB_Mentor_Users.email == payload.email)
    if not user.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    send_email(payload.email, user.first().password)
    return generalResponse(message= "Email send successfully", data=None)

@router.put("/change-password")
async def change_password(request: Request, payload: MentorChangePassword,
                         db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
    myHeader = validateLanguageHeader(request)
    user = db.query(DB_Mentor_Users).filter(DB_Mentor_Users.id == current_user.user_id)

    if not user.first() or not verifyPassword(payload.oldpassword, user.first().password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")
    
    if payload.newpassword:
        user.password = payload.newpassword
        db.commit()
        
        # if not user.push_token or not user.push_token == "":
        #     addNewNotification(user_type=UserType.Mentor,
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
async def delete_account(db: Session = Depends(get_db), 
                         current_user: int = Depends(get_current_user)):
    
    user = db.query(DB_Mentor_Users).filter(DB_Mentor_Users.id == current_user.user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    db.delete(user)
    db.commit()

    return generalResponse(message="Profile deleted successfully", data=None)