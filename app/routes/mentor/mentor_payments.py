from fastapi import Depends, Request, APIRouter, HTTPException, status
from app.utils.database import get_db
from sqlalchemy.orm import Session
from app.models.respond.general import generalResponse
from app.utils.oauth2 import get_current_user
from app.models.database.db_payments import DB_Mentor_Payments, DB_Mentor_PaymentsـReports
from app.models.schemas.payment_report import PaymentReport
from app.models.database.db_appointment import DB_Appointments
from app.models.database.client.db_client_user import DB_Client_Users
from app.models.database.mentor.db_mentor_user import DB_Mentor_Users
from app.utils.firebase_notifications.notifications_manager import UserType, addNewNotification
from app.models.database.db_country import DB_Countries
from app.utils.validation import validateLanguageHeader

router = APIRouter(
    prefix="/mentor-payments",
    tags=["Mentor-Payments"]
)

@router.get("/")
async def get_mentor_payments(request: Request, db: Session = Depends(get_db), get_current_user: int = Depends(get_current_user)):
    myHeader = validateLanguageHeader(request)

    currency_name_field = DB_Appointments.currency_english if myHeader.language == "en" else DB_Appointments.currency_arabic

    query = db.query(DB_Mentor_Payments.id, 
                     DB_Mentor_Payments.mentor_id,
                     DB_Mentor_Payments.appointment_id, 
                     DB_Mentor_Payments.status.label("payment_status"),
                     DB_Mentor_Payments.created_at, 
                     DB_Mentor_PaymentsـReports.message.label("payment_reported_message"),
                     DB_Appointments.client_id, 
                     DB_Appointments.appointment_type,
                     DB_Appointments.date_from.label("appointment_date_from"), 
                     DB_Appointments.date_to.label("appointment_date_to"),
                     DB_Appointments.state.label("appointment_state"), 
                     DB_Appointments.is_free.label("appointment_is_free"),
                     DB_Appointments.price.label("appointment_price"), 
                     DB_Appointments.discounted_price.label("appointment_discounted_price"),
                     currency_name_field.label("currency"),
                     DB_Appointments.mentor_hour_rate, 
                     DB_Appointments.note_from_client,
                     DB_Appointments.note_from_mentor, 
                     DB_Appointments.discount_id.label("appointment_discount_id"),
                     DB_Client_Users.first_name.label("client_first_name"), 
                     DB_Client_Users.last_name.label("client_last_name"),
                     DB_Client_Users.profile_img.label("client_profile_img"), 
                     DB_Client_Users.country_id.label("client_country_id"),
                     DB_Countries.flag_image.label("client_flag_img"),           
                     ).join(DB_Mentor_PaymentsـReports, DB_Mentor_PaymentsـReports.payment_id == DB_Mentor_Payments.id, isouter=True
                    ).join(DB_Appointments, DB_Appointments.id == DB_Mentor_Payments.appointment_id, isouter=True
                    ).join(DB_Client_Users, DB_Client_Users.id ==  DB_Appointments.client_id, isouter=True
                    ).join(DB_Countries, DB_Countries.id ==  DB_Client_Users.country_id, isouter=True
                    ).join(DB_Mentor_Users, DB_Mentor_Users.id ==  DB_Mentor_Payments.mentor_id, isouter=True
                    ).filter(DB_Mentor_Payments.mentor_id == get_current_user.user_id).all()
        
    return generalResponse(message="List of Mentor Payments", data= query)

@router.post("/report", status_code=status.HTTP_201_CREATED)
async def mentor_report_payment(request: Request, payload: PaymentReport,
                                db: Session = Depends(get_db), 
                                current_user: int = Depends(get_current_user)):
    
    myHeader = validateLanguageHeader(request)
    
    existing_report = db.query(DB_Mentor_PaymentsـReports).filter(DB_Mentor_PaymentsـReports.payment_id == payload.payment_id).first()

    if existing_report is not None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Payment already reported")
    
    payload.mentor_id = current_user.user_id

    report = DB_Mentor_PaymentsـReports(**payload.dict())
    db.add(report)
    db.commit()
    
    addNewNotification(user_type=UserType.Mentor,
                        user_id=current_user.user_id,
                        currentLanguage=myHeader.language,
                        db=db,
                        title_english="Payment Reported Successfully",
                                        title_arabic="تم الإبلاغ عن الدفعه بنجاح",
                                        content_english="We will review the payment details and get back to you very soon",
                                        content_arabic="سنراجع تفاصيل الدفع ونرد عليك قريبًا")
    
    return generalResponse(message="payment reported successfuly", data=None)