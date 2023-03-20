from fastapi import Request, Depends, status ,APIRouter, HTTPException
from sqlalchemy.orm import Session
from app.utils.validation import validateLanguageHeader
from app.utils.database import get_db
from app.models.database.db_client_banners import DB_Client_Banners
from app.models.database.db_event import DB_Events, EventState, DB_Events_Appointments
from app.models.respond.general import generalResponse
from app.models.schemas.home import HomeResponse, Event
from sqlalchemy import func
from datetime import datetime

router = APIRouter(
    prefix="/client-home",
    tags=["Home"]
)

@router.get("/")
async def get_home(request: Request, db: Session = Depends(get_db)):
    myHeader = validateLanguageHeader(request)
    
    main_events = db.query(DB_Events.id, 
                           DB_Events.title,
                           DB_Events.image,
                           DB_Events.description,
                           DB_Events.max_number_of_attendance,
                           DB_Events.date_from,
                           DB_Events.date_to,
                           DB_Events.price,
                           DB_Events.state).filter(DB_Events.state == EventState.active).filter(DB_Events.date_from > datetime.now()).all()
    main_banner = db.query(DB_Client_Banners).filter(DB_Client_Banners.language == myHeader.language).filter(DB_Client_Banners.published == True).all()
    
    listOfEvent : list[Event] = []
    for event in main_events:
        count = 0
        event_appointment_query = db.query(DB_Events_Appointments).filter(DB_Events_Appointments.event_id == event["id"]).all()
        for _ in event_appointment_query:
            count = count + 1
        listOfEvent.append(Event(id = event["id"], 
                                 title = event["title"],
                                 image = event["image"],
                                 description = event["description"],
                                 max_number_of_attendance = event["max_number_of_attendance"],
                                 date_from = event["date_from"],
                                 date_to = event["date_to"],
                                 price = event["price"],
                                 state = event["state"],
                                 joining_clients = count,
                                 ))

        
    respose = HomeResponse(main_banner = main_banner, main_event = listOfEvent) 
    return generalResponse(message="home return successfully", data=respose)
