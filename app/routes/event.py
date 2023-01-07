from fastapi import Request, Depends, APIRouter, HTTPException, status
from sqlalchemy.orm import Session
from app.utils.database import get_db
from app.utils.validation import validateLanguageHeader
from app.models.database.db_event import DB_Events, DB_Events_Appointments
from app.models.respond.general import generalResponse
from app.models.database.mentor.db_mentor_user import DB_Mentor_Users
from app.models.database.db_category import DB_Categories
from app.utils.oauth2 import get_current_user
from sqlalchemy import func
from app.models.schemas.home import Event


router = APIRouter(
    prefix="/event",
    tags=["Event"]
)

@router.get("/")
async def get_event_details(id :int ,request: Request, db: Session = Depends(get_db)):
    myHeader = validateLanguageHeader(request)

    if myHeader.language == "en" :
        query = db.query(DB_Events.image, DB_Events.owner_id, DB_Events.description, DB_Mentor_Users.id, 
                     DB_Mentor_Users.suffixe_name, DB_Mentor_Users.first_name, DB_Mentor_Users.last_name, 
                     DB_Events.max_number_of_attendance, DB_Events.date_to, DB_Events.state, 
                     DB_Events.title, DB_Events.date_from, 
                     DB_Events.price, DB_Mentor_Users.profile_img,DB_Mentor_Users.category_id,
                     DB_Categories.name_english.label("category_name")
                     ).join(DB_Categories, DB_Categories.id == DB_Mentor_Users.category_id, isouter=True).filter(DB_Events.id == id).first()
    else:
        query = db.query(DB_Events.image, DB_Events.owner_id, DB_Events.description, DB_Mentor_Users.id, 
                     DB_Mentor_Users.suffixe_name, DB_Mentor_Users.first_name, DB_Mentor_Users.last_name, 
                     DB_Events.max_number_of_attendance, DB_Events.date_to, DB_Events.state, 
                     DB_Events.title, DB_Events.date_from, 
                     DB_Events.price, DB_Mentor_Users.profile_img,DB_Mentor_Users.category_id,
                     DB_Categories.name_arabic.label("category_name")
                     ).join(DB_Categories, DB_Categories.id == DB_Mentor_Users.category_id, isouter=True).filter(DB_Events.id == id).first()
    if query is  None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail={"message": f"event id not valid"})
    
    idCount = 0
    for _ in db.query(DB_Events_Appointments).filter(DB_Events_Appointments.event_id == query["id"]).all():
        idCount = idCount + 1
    json = dict(query)
    json["joining_clients"] = idCount

    return generalResponse(message="Event return successfully", data=json)


@router.post("/bookcancel")
async def cancelEventAppointment(id: int, request: Request, db: Session = Depends(get_db), get_current_user: int = Depends(get_current_user)):
    myHeader = validateLanguageHeader(request)
    query = db.query(DB_Events_Appointments).filter(DB_Events_Appointments.id == id).filter(DB_Events_Appointments.client_id == get_current_user.user_id)
    
    if query.first() is None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail={"message": f"event id not valid or user not regiester on this event"})
    
    query.delete(synchronize_session=False)
    db.commit()
    return generalResponse(message="event appoitment canceled successfuly", data=None)

@router.post("/book")
async def bookEvent(id: int, request: Request, db: Session = Depends(get_db), get_current_user: int = Depends(get_current_user)):
    myHeader = validateLanguageHeader(request)
    
    query = db.query(DB_Events.max_number_of_attendance).filter(DB_Events.id == id).first()
    query_event_appointments = db.query(DB_Events_Appointments.id, DB_Events_Appointments.client_id, DB_Events_Appointments.event_id).all()
    if query is None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail={"message": f"event id not valid"})
    
    count = 0
    for _ in query_event_appointments:
        count = count + 1
    
    if count >= query["max_number_of_attendance"]:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail={"message": f"event reach the max number of attendance"})
    
    idCount = 1
    for item in query_event_appointments:
        idCount = idCount + 1
        if item["client_id"] == get_current_user.user_id and item["event_id"] == id:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail={"message": f"User already book on this event"})

    obj = DB_Events_Appointments(**{"id" : idCount, "event_id" : id, "client_id" : get_current_user.user_id })
    db.add(obj)
    db.commit()
    return generalResponse(message="event booked successfuly", data=None)