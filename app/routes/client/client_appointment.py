from fastapi import Request, Depends, APIRouter, HTTPException, status
from sqlalchemy.orm import Session
from app.models.schemas.appointment import AppointmentRequest
from app.utils.database import get_db
from app.models.database.db_appointment import DB_Appointments, AppointmentsState, AppointmentsType
from app.models.database.mentor.db_mentor_user import DB_Mentor_Users
from app.utils.generate import generateChannelName
from app.utils.oauth2 import get_current_user
from app.utils.validation import validateLanguageHeader
from datetime import datetime
from app.models.respond.general import generalResponse
from app.models.database.db_category import DB_Categories
from app.models.schemas.comment_appointment import AppointmentComment
from app.utils.agora.my_interface import generateTokenClient

# //TODO
router = APIRouter(
    prefix="/client-appointment",
    tags=["Appointment"]
)



@router.get("/mentor-appointment")
async def get_mentor_appointment(id :int , request: Request, db: Session = Depends(get_db)):
    myHeader = validateLanguageHeader(request)
    query = db.query(DB_Appointments).filter(DB_Appointments.mentor_id == id).filter(DB_Appointments.date_from > datetime.now()
                                                                                     ).filter(DB_Appointments.state == AppointmentsState.active).all()
    return generalResponse(message="list of appointments return successfully", data=query)
    
@router.get("/")
async def get_clientAppointment(request: Request, db: Session = Depends(get_db), get_current_user: int = Depends(get_current_user)):
    myHeader = validateLanguageHeader(request)
    
    if myHeader.language == "en" :
        query = db.query(DB_Appointments.id, DB_Appointments.date_from, DB_Appointments.date_to, 
                     DB_Appointments.client_id, DB_Appointments.mentor_id, DB_Appointments.appointment_type, 
                     DB_Appointments.price_before_discount, DB_Appointments.price_after_discount, DB_Appointments.state,
                     DB_Appointments.note_from_client, DB_Appointments.note_from_mentor, DB_Appointments.channel_id,
                     DB_Mentor_Users.profile_img, DB_Mentor_Users.suffixe_name, DB_Mentor_Users.first_name, DB_Mentor_Users.last_name, 
                     DB_Mentor_Users.category_id, DB_Categories.name_english.label("categoryName"), 
                     ).join(DB_Mentor_Users, DB_Mentor_Users.id == DB_Appointments.mentor_id, isouter=True
                     ).join(DB_Categories, DB_Categories.id == DB_Mentor_Users.category_id, isouter=True
                            ).filter(DB_Appointments.client_id == get_current_user.user_id
                                     ).all()
    else:
        query = db.query(DB_Appointments.id, DB_Appointments.date_from, DB_Appointments.date_to, 
                     DB_Appointments.client_id, DB_Appointments.mentor_id, DB_Appointments.appointment_type, 
                     DB_Appointments.price_before_discount, DB_Appointments.price_after_discount, DB_Appointments.state,
                     DB_Appointments.note_from_client, DB_Appointments.note_from_mentor, DB_Appointments.channel_id,
                     DB_Mentor_Users.profile_img, DB_Mentor_Users.suffixe_name, DB_Mentor_Users.first_name, DB_Mentor_Users.last_name, 
                     DB_Mentor_Users.category_id, DB_Categories.name_arabic.label("categoryName"), 
                     ).join(DB_Mentor_Users, DB_Mentor_Users.id == DB_Appointments.mentor_id, isouter=True
                     ).join(DB_Categories, DB_Categories.id == DB_Mentor_Users.category_id, isouter=True
                            ).filter(DB_Appointments.client_id == get_current_user.user_id
                                     ).all()
    
    return generalResponse(message="list of appointments return successfully", data=query)

@router.post("/cancel")
async def cancelAppointment(id: int, request: Request, db: Session = Depends(get_db), get_current_user: int = Depends(get_current_user)):
    myHeader = validateLanguageHeader(request)
    query = db.query(DB_Appointments).filter(DB_Appointments.id == id).filter(DB_Appointments.client_id == get_current_user.user_id
                                                                              ).filter(DB_Appointments.state == AppointmentsState.active)
    if query.first() is  None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="appoitment id not valid")
    
    
    query.update({"state" : AppointmentsState.client_cancel}, synchronize_session=False)
    db.commit()
    return generalResponse(message="appoitment canceled successfuly", data=None)
        


@router.post("/book")
async def bookAppointment(payload: AppointmentRequest, db: Session = Depends(get_db), get_current_user: int = Depends(get_current_user)):
    
    dateFrom = datetime(payload.dateFrom.year, payload.dateFrom.month, payload.dateFrom.day, payload.dateFrom.hour, payload.dateFrom.min)
    dateTo = datetime(payload.dateTo.year, payload.dateTo.month, payload.dateTo.day, payload.dateTo.hour, payload.dateTo.min)
    
    if dateFrom <= datetime.now():
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="dateTime not valid")
    
    if dateFrom >= dateTo:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="dateTime not valid from > to")

    appointments_query = db.query(DB_Appointments)
    
    filterd_appointments_query = appointments_query.filter(DB_Appointments.mentor_id == payload.mentorId
                                    ).filter(DB_Appointments.state == AppointmentsState.active).all()
    
    filterd_appointments_query2 = appointments_query.filter(DB_Appointments.client_id == get_current_user.user_id
                                    ).filter(DB_Appointments.state == AppointmentsState.active).all()
        
    if filterd_appointments_query != []:
        for apps in filterd_appointments_query2:
            if (dateFrom >= apps.date_from and dateFrom <= apps.date_to) or (dateTo <= apps.date_to and dateTo >= apps.date_from):
                raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="mentor already have appointment in that date")
    
    if filterd_appointments_query2 != []:
        for app in filterd_appointments_query2:
            if (dateFrom >= app.date_from and dateFrom <= app.date_to) or (dateTo <= app.date_to and dateTo >= app.date_from):
                raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="client already have appointment in that date")
    
    obj = DB_Appointments(**{"mentor_id" : payload.mentorId, 
                                     "client_id" : get_current_user.user_id, 
                                     "date_from" : dateFrom, "date_to" : dateTo, 
                                     "price_before_discount" : payload.priceBeforeDiscount, 
                                     "price_after_discount" : payload.priceAfterDiscount, 
                                     "state" : AppointmentsState.active,
                                     "note_from_client" : payload.note,
                                     "appointment_type" : AppointmentsType.schudule if payload.type == "schudule" else AppointmentsType.instant,
                                    "channel_id," : generateChannelName()}) 
    db.add(obj)
    db.commit()
    return generalResponse(message="appoitment booked successfuly", data=None)

@router.put("/join-call")
async def clientJoinAppointment(id: int, channelName: str, db: Session = Depends(get_db), get_current_user: int = Depends(get_current_user)):
    query = db.query(DB_Appointments).filter(DB_Appointments.id == id).filter(DB_Appointments.client_id == get_current_user.user_id)

    if query.first() is None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="appoitment id not valid")
    
    callToken = generateTokenClient(channelName)

    query.update({"client_join_call" : datetime.now().strftime("%Y-%m-%d %H:%M:%S")}, synchronize_session=False)
    db.commit()
    return generalResponse(message="client join appoitment successfuly", data=callToken)

@router.put("/end-call")
async def clientEndAppointment(id: int, db: Session = Depends(get_db), get_current_user: int = Depends(get_current_user)):
    query = db.query(DB_Appointments).filter(DB_Appointments.id == id).filter(DB_Appointments.client_id == get_current_user.user_id)
    
    if query.first() is None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="appoitment id not valid")       
                                                             
    query.update({"client_date_of_close" : datetime.now().strftime("%Y-%m-%d %H:%M:%S")}, synchronize_session=False)
    
    if query.first().client_join_call is None:
        query.update({"state" : AppointmentsState.mentor_miss}, synchronize_session=False)
    
    db.commit()
    return generalResponse(message="client end appoitment successfuly", data=None)

@router.post("/comment")
async def add_comment_to_Appointment(payload: AppointmentComment, request: Request, db: Session = Depends(get_db), get_current_user: int = Depends(get_current_user)):
    myHeader = validateLanguageHeader(request)
    query = db.query(DB_Appointments).filter(DB_Appointments.id == payload.id).filter(DB_Appointments.client_id == get_current_user.user_id
                                                                              ).filter(DB_Appointments.state == AppointmentsState.active)
    if query.first() is None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="appoitment id not valid")
    
    query.update({"note_from_client" : payload.comment}, synchronize_session=False)
    db.commit()
    return generalResponse(message="appoitment compleated successfuly", data=None)