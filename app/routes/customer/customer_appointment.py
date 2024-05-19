from fastapi import Request, Depends, APIRouter, HTTPException, status
from sqlalchemy.orm import Session
from app.models.schemas.appointment import AppointmentRequest
from app.utils.database import get_db
from app.models.database.db_appointment import DB_Appointments, AppointmentsState
from app.models.database.attorney.db_attorney_user import DB_Attorney_Users
from app.utils.firebase_notifications.notifications_manager import addNewNotification, UsersType
from app.utils.generate import generateChannelName
from app.utils.oauth2 import get_current_user
from app.utils.validation import validateLanguageHeader
from datetime import datetime
from app.models.respond.general import generalResponse
from app.models.database.db_category import DB_Categories
from app.models.schemas.comment_appointment import AppointmentComment
from app.utils.agora.my_interface import generateTokenCustomer
from app.models.database.db_country import DB_Countries


router = APIRouter(
    prefix="/customer-appointment",
    tags=["Customer"]
)

@router.get("/specific-attorney-appointments")
async def get_specific_attorney_appointments(id :int, db: Session = Depends(get_db)):
    query = db.query(DB_Appointments.date_from, DB_Appointments.date_to, 
                     ).filter(DB_Appointments.attorney_id == id, 
                              DB_Appointments.state == AppointmentsState.active,
                              DB_Appointments.date_from > datetime.utcnow()
                                ).filter(DB_Attorney_Users.blocked == False,
                                DB_Attorney_Users.published == True
                                ).all()
                     
    return generalResponse(message="list of appointments return successfully", data=query)

@router.get("/")
async def get_customer_appointments(request: Request, db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
    myHeader = validateLanguageHeader(request)
    category_column = DB_Categories.name_arabic if myHeader.language == "ar" else DB_Categories.name_english
    currency_column = DB_Appointments.currency_arabic if myHeader.language == "ar" else DB_Appointments.currency_english
    country_column = DB_Countries.name_arabic if myHeader.language == "ar" else DB_Countries.name_english

    query = db.query(DB_Appointments.id, 
                     DB_Appointments.date_from, 
                     DB_Appointments.date_to, 
                     DB_Appointments.attorney_id, 
                     DB_Appointments.appointment_type, 
                     DB_Appointments.state,
                     DB_Appointments.discount_id,
                     DB_Appointments.is_free,
                     DB_Appointments.price,
                     DB_Appointments.total_price,
                     currency_column.label("currency"), 
                     DB_Appointments.attorney_hour_rate,
                     DB_Appointments.note_from_customers, 
                     DB_Appointments.note_from_attorney, 
                     DB_Appointments.channel_id,
                     
                     DB_Attorney_Users.profile_img, 
                     DB_Attorney_Users.suffixe_name, 
                     DB_Attorney_Users.first_name, 
                     DB_Attorney_Users.last_name, 
                     DB_Attorney_Users.gender,
                     DB_Attorney_Users.speaking_language,
                     DB_Countries.flag_image,
                     country_column.label("countryName"), 
                     category_column.label("categoryName"), 
                     ).join(DB_Attorney_Users, DB_Attorney_Users.id == DB_Appointments.attorney_id, isouter=True
                     ).join(DB_Categories, DB_Categories.id == DB_Attorney_Users.category_id, isouter=True
                     ).join(DB_Countries, DB_Countries.id == DB_Attorney_Users.country_id, isouter=True
                     ).filter(DB_Appointments.customers_id == current_user.user_id,
                                DB_Attorney_Users.blocked == False,
                                DB_Attorney_Users.published == True
                     ).all()
    
    return generalResponse(message="list of appointments return successfully", data=query)


@router.get("/active")
async def get_customer_active_appointments(request: Request, db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
    myHeader = validateLanguageHeader(request)
    category_column = DB_Categories.name_arabic if myHeader.language == "ar" else DB_Categories.name_english
    currency_column = DB_Appointments.currency_arabic if myHeader.language == "ar" else DB_Appointments.currency_english
    country_column = DB_Countries.name_arabic if myHeader.language == "ar" else DB_Countries.name_english

    query = db.query(DB_Appointments.id, 
                     DB_Appointments.date_from, 
                     DB_Appointments.date_to, 
                     DB_Appointments.attorney_id, 
                     DB_Appointments.appointment_type, 
                     DB_Appointments.state,
                     DB_Appointments.discount_id,
                     DB_Appointments.is_free,
                     DB_Appointments.price,
                     DB_Appointments.total_price,
                     currency_column.label("currency"), 
                     DB_Appointments.attorney_hour_rate,
                     DB_Appointments.note_from_customers, 
                     DB_Appointments.note_from_attorney, 
                     DB_Appointments.channel_id,
                     
                     DB_Attorney_Users.profile_img, 
                     DB_Attorney_Users.suffixe_name, 
                     DB_Attorney_Users.first_name, 
                     DB_Attorney_Users.last_name, 
                     DB_Attorney_Users.gender,
                     DB_Attorney_Users.speaking_language,
                     DB_Countries.flag_image,
                     country_column.label("countryName"), 
                     category_column.label("categoryName"), 
                     ).join(DB_Attorney_Users, DB_Attorney_Users.id == DB_Appointments.attorney_id, isouter=True
                     ).join(DB_Categories, DB_Categories.id == DB_Attorney_Users.category_id, isouter=True
                     ).join(DB_Countries, DB_Countries.id == DB_Attorney_Users.country_id, isouter=True
                     ).filter(DB_Appointments.customers_id == current_user.user_id,
                                DB_Attorney_Users.blocked == False,
                                DB_Attorney_Users.published == True,
                                DB_Appointments.state == AppointmentsState.active
                     ).all()
    
    return generalResponse(message="list of active appointments return successfully", data=query)

@router.post("/cancel")
async def cancel_appointment(id: int, request: Request, db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
    myHeader = validateLanguageHeader(request)
    
    appointment = get_db_appointment(db, id, current_user.user_id, AppointmentsState.active)
    raise_http_exception_if_none(appointment, "Appointment ID not valid or cannot be canceled")

    
    appointment.state = AppointmentsState.customers_cancel
    db.commit()
    
    addNewNotification(user_type=UsersType.customer,
                        user_id=current_user.user_id,
                        currentLanguage=myHeader.language,
                        db=db,
                        title_english="Appointment canceled successfully",
                        title_arabic="تم إلغاء الموعد بنجاح",
                        content_english="canceling appointment will will cost you 50/100 of the call charged",
                        content_arabic="سيكلفك إلغاء الموعد 50/100 من تكلفة المكالمة")
    
    return generalResponse(message="Appointment canceled successfully", data=None)

@router.put("/join-call")
async def customer_join_appointment(id: int, channel_name: str, db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
    
    appointment = get_db_appointment(db, id, current_user.user_id)
    raise_http_exception_if_none(appointment, "Appointment ID not valid")

    callToken = generateTokenCustomer(channel_name)
    appointment.customers_join_call = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

    db.commit()
    return generalResponse(message="customer joined appointment successfully", data=callToken)

@router.put("/end-call")
async def customer_endup_appointment(id: int, db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
    
    appointment = get_db_appointment(db, id, current_user.user_id)
    raise_http_exception_if_none(appointment, "Appointment ID not valid")
            
    if appointment.attorney_join_call is None:
        appointment.state = AppointmentsState.attorney_miss
                                 
    appointment.customers_date_of_close = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    db.commit()
    
    return generalResponse(message="customer end appoitment successfuly", data=None)

@router.post("/comment")
async def add_comment_to_appointment(payload: AppointmentComment, request: Request, db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):

    appointment = get_db_appointment(db, payload.id, current_user.user_id)
    raise_http_exception_if_none(appointment, "Appointment ID not valid")

    appointment.note_from_customers = payload.comment
    db.commit()
    return generalResponse(message="Customer added comment to appointment successfully", data=None)

@router.post("/book")
async def book_appointment(payload: AppointmentRequest, db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
    
    dateFrom = datetime(payload.date_from.year, payload.date_from.month, payload.date_from.day, payload.date_from.hour, payload.date_from.min)
    dateTo = datetime(payload.date_to.year, payload.date_to.month, payload.date_to.day, payload.date_to.hour, payload.date_to.min)
    
    if dateFrom <= datetime.utcnow():
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="dateFrom not valid")
    
    if dateFrom >= dateTo:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="dateTime not valid from > to")

    appointments_query = db.query(DB_Appointments)
    
    country_query = db.query(DB_Countries.id, DB_Countries.currency_english, 
                         DB_Countries.currency_arabic).filter(DB_Countries.id == payload.country_id).first()
    
    attorney_appointments_query = appointments_query.filter(DB_Appointments.attorney_id == payload.attorney_id
                                    ).filter(DB_Appointments.state == AppointmentsState.active).all()
    
    customer_appointments_query = appointments_query.filter(DB_Appointments.customers_id == current_user.user_id
                                    ).filter(DB_Appointments.state == AppointmentsState.active).all()
        
    if attorney_appointments_query != []:
        for app in attorney_appointments_query:
            if (dateFrom >= app.date_from and dateFrom <= app.date_to) or (dateTo <= app.date_to and dateTo >= app.date_from):
                raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="attorney already have appointment in that date")
    
    if customer_appointments_query != []:
        for app in customer_appointments_query:
            if (dateFrom >= app.date_from and dateFrom <= app.date_to) or (dateTo <= app.date_to and dateTo >= app.date_from):
                raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="customer already have appointment in that date")

    obj = DB_Appointments(**{"attorney_id" : payload.attorney_id, 
                            "customers_id" : current_user.user_id,
                            "date_from" : dateFrom, 
                            "date_to" : dateTo, 
                            "discount_id" : payload.discount_id,
                            "is_free" : payload.is_free,
                            "price" : payload.price,
                            "total_price" : payload.total_price,
                            "currency_english" : country_query.currency_english,
                            "currency_arabic" :country_query.currency_arabic,
                            "attorney_hour_rate" : payload.attorney_hour_rate,
                            "note_from_customers" : payload.note,
                            "appointment_type" : payload.type,
                            "payment_type" : payload.payment,
                            "state" : AppointmentsState.active,
                            "channel_id" : generateChannelName()}) 
    db.add(obj)
    db.commit()
    return generalResponse(message="appoitment booked successfuly", data=None)

#############################################################################################

def get_db_appointment(db: Session, appointment_id: int, customers_id: int, state: AppointmentsState = None):
    query = db.query(DB_Appointments).filter(DB_Appointments.id == appointment_id, DB_Appointments.customers_id == customers_id)
    if state:
        query = query.filter(DB_Appointments.state == state)
    return query.first()


def raise_http_exception_if_none(entity, message: str):
    if entity is None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=message)