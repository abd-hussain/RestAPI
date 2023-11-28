from fastapi import Request, Depends, APIRouter, HTTPException, status
from sqlalchemy.orm import Session
from app.models.database.db_country import DB_Countries
from app.utils.database import get_db
from app.models.database.db_appointment import DB_Appointments, AppointmentsState
from app.models.database.client.db_client_user import DB_Client_Users
from app.utils.oauth2 import get_current_user
from app.models.respond.general import generalResponse
from app.models.schemas.comment_appointment import AppointmentComment

router = APIRouter(
    prefix="/mentor-appointment",
    tags=["Appointment"]
)
    
@router.get("/")
async def get_mentorAppointment(db: Session = Depends(get_db), get_current_user: int = Depends(get_current_user)):    
    query = db.query(DB_Appointments.id, DB_Appointments.date_from, DB_Appointments.date_to,
                      DB_Appointments.client_id, DB_Appointments.mentor_id, 
                      DB_Appointments.appointment_type, DB_Appointments.channel_id, 
                      DB_Appointments.note_from_mentor, DB_Appointments.note_from_client,
                      DB_Appointments.price_before_discount, DB_Appointments.price_after_discount, DB_Appointments.state,
                      DB_Client_Users.profile_img, DB_Client_Users.first_name, DB_Client_Users.last_name,
                      DB_Client_Users.gender, DB_Client_Users.date_of_birth, DB_Client_Users.country_id,DB_Countries.flag_image
                     ).join(DB_Client_Users, DB_Client_Users.id == DB_Appointments.client_id, isouter=True)\
                         .join(DB_Countries, DB_Countries.id == DB_Client_Users.country_id, isouter=True).filter(
                         DB_Appointments.mentor_id == get_current_user.user_id).all()
    
    return generalResponse(message="list of appointments return successfully", data=query)

@router.post("/cancel")
async def cancelAppointment(id: int, db: Session = Depends(get_db), get_current_user: int = Depends(get_current_user)):
    query = db.query(DB_Appointments).filter(DB_Appointments.id == id).filter(DB_Appointments.mentor_id == get_current_user.user_id
                                                                              ).filter(DB_Appointments.state == AppointmentsState.active)
    if query.first() is None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="appoitment id not valid")
    
    query.update({"state" : AppointmentsState.mentor_cancel}, synchronize_session=False)
    db.commit()
    return generalResponse(message="appoitment canceled successfuly", data=None)
        
@router.post("/compleated")
async def compleateAppointment(id: int, db: Session = Depends(get_db), get_current_user: int = Depends(get_current_user)):
    query = db.query(DB_Appointments).filter(DB_Appointments.id == id).filter(DB_Appointments.mentor_id == get_current_user.user_id
                                                                              ).filter(DB_Appointments.state == AppointmentsState.active)
    if query.first() is None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="appoitment id not valid")
    
    query.update({"state" : AppointmentsState.completed}, synchronize_session=False)
    db.commit()
    return generalResponse(message="appoitment compleated successfuly", data=None)


@router.post("/comment")
async def add_comment_to_Appointment(payload: AppointmentComment, request: Request, db: Session = Depends(get_db), get_current_user: int = Depends(get_current_user)):
    query = db.query(DB_Appointments).filter(DB_Appointments.id == payload.id).filter(DB_Appointments.mentor_id == get_current_user.user_id)
    
    if query.first() is None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="appoitment id not valid")
    
    query.update({"note_from_mentor" : payload.comment}, synchronize_session=False)
    db.commit()
    return generalResponse(message="appoitment compleated successfuly", data=None)