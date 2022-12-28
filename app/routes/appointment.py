from fastapi import Request, Depends, APIRouter
from sqlalchemy.orm import Session
from app.models.schemas.appointment import AppointmentRequest
from app.utils.database import get_db
from app.models.database.db_appointment import DB_Mentors_Reservations
from app.utils.oauth2 import get_current_user
from app.utils.validation import validateLanguageHeader
from datetime import datetime
from app.models.respond.general import generalResponse

router = APIRouter(
    prefix="/appointment",
    tags=["Appointment"]
)

@router.get("/mentor")
async def get_all_mentor_appointment(id :int , request: Request, db: Session = Depends(get_db), get_current_user: int = Depends(get_current_user)):
    myHeader = validateLanguageHeader(request)
    query = db.query(DB_Mentors_Reservations.mentor_id, DB_Mentors_Reservations.date
                     ).filter(DB_Mentors_Reservations.mentor_id == id).filter(DB_Mentors_Reservations.date > datetime.now()).all()
    return generalResponse(message="list of appointments return successfully", data=query)


@router.get("/client")
async def get_clientAppointment(request: Request, db: Session = Depends(get_db), get_current_user: int = Depends(get_current_user)):
    myHeader = validateLanguageHeader(request)
    query = db.query(DB_Mentors_Reservations.id, DB_Mentors_Reservations.client_id, DB_Mentors_Reservations.date
                     ).filter(DB_Mentors_Reservations.client_id == get_current_user.user_id).filter(DB_Mentors_Reservations.date > datetime.now()).all()
    return generalResponse(message="list of appointments return successfully", data=query)

@router.post("/book")
async def bookAppointment(payload: AppointmentRequest, request: Request, db: Session = Depends(get_db), get_current_user: int = Depends(get_current_user)):
    myHeader = validateLanguageHeader(request)
    
    date = datetime(payload.dateYear, payload.dateMonth, payload.dateDay, payload.dateHour, payload.dateMin)
    
    if date <= datetime.now():
        return generalResponse(message="dateTime not valid", data=None)

    appointments_query = db.query(DB_Mentors_Reservations)
    
    filterd_appointments_query = appointments_query.filter(DB_Mentors_Reservations.mentor_id == payload.mentorId).filter(DB_Mentors_Reservations.date >= date).all()
    for item in filterd_appointments_query:
        if item.date == date:
            return generalResponse(message="mentor already have appointment in that date", data=None)


    all_appointments_query = appointments_query.all()
    id = 1
    for item in all_appointments_query:
        id = id + 1
    
    obj = DB_Mentors_Reservations(**{"id" : id, "mentor_id" : payload.mentorId, "client_id" : get_current_user.user_id, "date" : date})
    db.add(obj)
    db.commit()
    return generalResponse(message="appoitment booked successfuly", data=None)