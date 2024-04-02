from fastapi import Depends, Request, APIRouter, HTTPException, status
from sqlalchemy.orm import Session
from app.models.database.db_country import DB_Countries
from app.utils.database import get_db
from app.models.database.db_appointment import DB_Appointments, AppointmentsState
from app.models.database.customer.db_customer_user import DB_Customer_Users
from app.utils.oauth2 import get_current_user
from app.models.respond.general import generalResponse
from app.models.schemas.comment_appointment import AppointmentComment
from app.models.schemas.payment_report import Payment
from app.models.database.db_payments import DB_Attorney_Payments, PaymentStatus
from datetime import datetime
from app.utils.agora.my_interface import generateTokenAttorney
from app.utils.firebase_notifications.notifications_manager import addNewNotification
from app.utils.validation import validateLanguageHeader

router = APIRouter(
    prefix="/attorney-appointment",
    tags=["Attorney"]
)    
    
@router.get("/")
async def get_attorney_appointment(db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):    
    
    appointments = get_appointments_query(db, current_user.user_id).all()
    
    return generalResponse(message="List of appointments returned successfully", data=appointments)

@router.get("/active")
async def get_attorney_active_appointment(db: Session = Depends(get_db), current_user: int = Depends(get_current_user)): 
   
    appointments = get_appointments_query(db, current_user.user_id, AppointmentsState.active).all()
    
    return generalResponse(message="List of Active appointments returned successfully", data=appointments)

@router.post("/cancel")
async def cancel_appointment(id: int, request: Request, db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
    myHeader = validateLanguageHeader(request)
    
    appointment = get_db_appointment(db, id, current_user.user_id, AppointmentsState.active)
    raise_http_exception_if_none(appointment, "Appointment ID not valid or cannot be canceled")

    
    appointment.state = AppointmentsState.attorney_cancel
    db.commit()
    
    # //TODO
    # addNewNotification(user_type=UserType.Attorney,
    #                     user_id=current_user.user_id,
    #                     currentLanguage=myHeader.language,
    #                     db=db,
    #                     title_english="Appointment canceled successfully",
    #                     title_arabic="تم إلغاء الموعد بنجاح",
    #                     content_english="canceling appointment will not cost you any thing and will not added to the payment screen",
    #                     content_arabic="إلغاء الموعد لن يكلفك شيئا ولن يضاف إلى شاشة الدفع")
    
    return generalResponse(message="Appointment canceled successfully", data=None)

@router.put("/join-call")
async def attorney_join_appointment(id: int, channel_name: str, db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
    appointment = get_db_appointment(db, id, current_user.user_id)
    raise_http_exception_if_none(appointment, "Appointment ID not valid")
    
    callToken = generateTokenAttorney(channel_name)
    
    appointment.attorney_join_call = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    db.commit()
    return generalResponse(message="attorney joined appointment successfully", data=callToken)

@router.put("/end-call")
async def attorney_endup_appointment(id: int, db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
    
    appointment = get_db_appointment(db, id, current_user.user_id)
    raise_http_exception_if_none(appointment, "Appointment ID not valid")
    
    if appointment.customers_join_call is None:
        appointment.state = AppointmentsState.customers_miss

    add_payment_to_attorney(appointment_id=id, db=db)
                                                            
    appointment.attorney_date_of_close = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    db.commit()
    
    return generalResponse(message="Attorney ended appointment successfully", data=None)


@router.post("/comment")
async def add_comment_to_appointment(payload: AppointmentComment, db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
   
    appointment = get_db_appointment(db, payload.id, current_user.user_id)
    raise_http_exception_if_none(appointment, "Appointment ID not valid")
    
    appointment.note_from_attorney = payload.comment
    db.commit()
    return generalResponse(message="Attorney added comment to appointment successfully", data=None)

#############################################################################################

def get_db_appointment(db: Session, appointment_id: int, attorney_id: int, state: AppointmentsState = None):
    query = db.query(DB_Appointments).filter(DB_Appointments.id == appointment_id, DB_Appointments.attorney_id == attorney_id)
    if state:
        query = query.filter(DB_Appointments.state == state)
    return query.first()

def raise_http_exception_if_none(entity, message: str):
    if entity is None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=message)
    
def get_appointments_query(db: Session, attorney_id: int, state: AppointmentsState = None):
    query = db.query(DB_Appointments).filter(DB_Appointments.attorney_id == attorney_id)
    
    query = db.query(DB_Appointments.id, DB_Appointments.date_from, DB_Appointments.date_to,
                      DB_Appointments.customers_id, DB_Appointments.attorney_id, 
                      DB_Appointments.appointment_type, DB_Appointments.channel_id, 
                      DB_Appointments.note_from_attorney, DB_Appointments.note_from_customers,
                      DB_Appointments.price, DB_Appointments.total_price, DB_Appointments.state,
                      DB_Appointments.attorney_join_call, DB_Appointments.customers_join_call,
                      DB_Appointments.attorney_date_of_close, DB_Appointments.customers_date_of_close,
                      DB_Appointments.currency_english, DB_Appointments.currency_arabic,
                      DB_Appointments.is_free, DB_Appointments.attorney_hour_rate,
                      DB_Appointments.discount_id,
                      DB_Customer_Users.profile_img, DB_Customer_Users.first_name, DB_Customer_Users.last_name,
                      DB_Customer_Users.gender, DB_Customer_Users.date_of_birth, DB_Customer_Users.country_id,
                      DB_Countries.flag_image
                     ).join(DB_Customer_Users, DB_Customer_Users.id == DB_Appointments.customers_id, isouter=True)\
                         .join(DB_Countries, DB_Countries.id == DB_Customer_Users.country_id, isouter=True).filter(
                             DB_Appointments.attorney_id == attorney_id)
    
    if state:
        query = query.filter(DB_Appointments.state == state)
    return query
    
def add_payment_to_attorney(appointment_id, db):
    
    attorney_id = db.query(DB_Appointments.attorney_id).filter(DB_Appointments.id == appointment_id).scalar()
    obj = Payment(attorney_id=attorney_id, appointment_id=appointment_id, status=PaymentStatus.pending)
    
    parsedObj = DB_Attorney_Payments(**obj.dict())
    db.add(parsedObj)
    db.commit()