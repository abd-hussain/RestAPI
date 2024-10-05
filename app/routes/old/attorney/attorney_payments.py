# from fastapi import Depends, Request, APIRouter, HTTPException, status
# from app.utils.database import get_db
# from sqlalchemy.orm import Session
# from app.models.respond.general import generalResponse
# from app.utils.oauth2 import get_current_user
# from app.models.database.db_payments import DB_Attorney_Payments, DB_Attorney_PaymentsـReports
# from app.models.schemas.payment_report import PaymentReport
# from app.models.database.db_appointment import DB_Appointments
# from app.models.database.customer.db_customer_user import DB_Customer_Users
# from app.models.database.attorney.db_attorney_user import DB_Attorney_Users
# from app.models.database.db_banner import UsersType
# from app.utils.firebase_notifications.notifications_manager import addNewNotification, UsersType
# from app.models.database.db_country import DB_Countries
# from app.utils.validation import validateLanguageHeader

# router = APIRouter(
#     prefix="/attorney-payments",
#     tags=["Attorney"]
# )

# @router.get("/")
# async def get_attorney_payments(request: Request, db: Session = Depends(get_db), get_current_user: int = Depends(get_current_user)):
#     myHeader = validateLanguageHeader(request)

#     currency_name_field = DB_Appointments.currency_english if myHeader.language == "en" else DB_Appointments.currency_arabic

#     query = db.query(DB_Attorney_Payments.id, 
#                      DB_Attorney_Payments.attorney_id,
#                      DB_Attorney_Payments.appointment_id, 
#                      DB_Attorney_Payments.status.label("payment_status"),
#                      DB_Attorney_Payments.created_at, 
#                      DB_Attorney_PaymentsـReports.message.label("payment_reported_message"),
#                      DB_Appointments.customers_id, 
#                      DB_Appointments.appointment_type,
#                      DB_Appointments.date_from.label("appointment_date_from"), 
#                      DB_Appointments.date_to.label("appointment_date_to"),
#                      DB_Appointments.state.label("appointment_state"), 
#                      DB_Appointments.is_free.label("appointment_is_free"),
#                      DB_Appointments.price.label("appointment_price"), 
#                      DB_Appointments.total_price.label("appointment_total_price"),
#                      currency_name_field.label("currency"),
#                      DB_Appointments.attorney_hour_rate, 
#                      DB_Appointments.note_from_customers,
#                      DB_Appointments.note_from_attorney, 
#                      DB_Appointments.discount_id.label("appointment_discount_id"),
#                      DB_Customer_Users.first_name.label("customer_first_name"), 
#                      DB_Customer_Users.last_name.label("customer_last_name"),
#                      DB_Customer_Users.profile_img.label("customer_profile_img"), 
#                      DB_Customer_Users.country_id.label("customer_country_id"),
#                      DB_Countries.flag_image.label("customer_flag_img"),           
#                      ).join(DB_Attorney_PaymentsـReports, DB_Attorney_PaymentsـReports.payment_id == DB_Attorney_Payments.id, isouter=True
#                     ).join(DB_Appointments, DB_Appointments.id == DB_Attorney_Payments.appointment_id, isouter=True
#                     ).join(DB_Customer_Users, DB_Customer_Users.id ==  DB_Appointments.customers_id, isouter=True
#                     ).join(DB_Countries, DB_Countries.id ==  DB_Customer_Users.country_id, isouter=True
#                     ).join(DB_Attorney_Users, DB_Attorney_Users.id ==  DB_Attorney_Payments.attorney_id, isouter=True
#                     ).filter(DB_Attorney_Payments.attorney_id == get_current_user.user_id).all()
        
#     return generalResponse(message="List of Attorney Payments", data= query)

# @router.post("/report", status_code=status.HTTP_201_CREATED)
# async def attorney_report_payment(request: Request, payload: PaymentReport,
#                                 db: Session = Depends(get_db), 
#                                 current_user: int = Depends(get_current_user)):
    
#     myHeader = validateLanguageHeader(request)
    
#     existing_report = db.query(DB_Attorney_PaymentsـReports).filter(DB_Attorney_PaymentsـReports.payment_id == payload.payment_id).first()

#     if existing_report is not None:
#         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Payment already reported")
    
#     payload.attorney_id = current_user.user_id

#     report = DB_Attorney_PaymentsـReports(**payload.dict())
#     db.add(report)
#     db.commit()
#     addNewNotification(user_type=UsersType.attorney,
#                         user_id=current_user.user_id,
#                         currentLanguage=myHeader.language,
#                         db=db,
#                         title_english="Payment Reported Successfully",
#                                         title_arabic="تم الإبلاغ عن الدفعه بنجاح",
#                                         content_english="We will review the payment details and get back to you very soon",
#                                         content_arabic="سنراجع تفاصيل الدفع ونرد عليك قريبًا")
    
#     return generalResponse(message="payment reported successfuly", data=None)