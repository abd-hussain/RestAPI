from fastapi import Request, Depends, status ,APIRouter, HTTPException, File, UploadFile, Form
from sqlalchemy.orm import Session
from app.utils.validation import validateLanguageHeader
from app.utils.database import get_db
from app.models.database.db_mentor_banners import DB_Mentor_Banners
from app.models.database.db_story import DB_Stories
from app.models.database.db_event import DB_Events, EventState, DB_Events_Appointments
from app.models.respond.general import generalResponse
from app.models.schemas.home import MentorHomeResponse, Event
from app.models.schemas.story import StoryPayload
from app.utils.oauth2 import get_current_user
from datetime import datetime
from app.utils.time import current_milli_time

router = APIRouter(
    prefix="/mentor-home",
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
    
    main_banner = db.query(DB_Mentor_Banners).filter(DB_Mentor_Banners.language == myHeader.language).filter(DB_Mentor_Banners.published == True).all()
    main_story = db.query(DB_Stories).filter(DB_Stories.language == myHeader.language).filter(DB_Stories.published == True).all()

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

    respose = MentorHomeResponse(main_banner = main_banner, main_story = main_story, main_event = listOfEvent) 
    return generalResponse(message="home return successfully", data=respose)

@router.post("/story", status_code=status.HTTP_201_CREATED)
async def create_story(request: Request, attach:  UploadFile = File(default=None), db: Session = Depends(get_db), get_current_user: int = Depends(get_current_user)):
        myHeader = validateLanguageHeader(request)
        payload = StoryPayload(owner_id = get_current_user.user_id, language = myHeader.language, published = True)

        if attach is not None:
            if attach.content_type not in ["image/jpeg", "image/png", "image/jpg"]:
                raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Attach Image Format is not valid")
            filename = f"{current_milli_time()}.png"
            file_location = f"static/story/{filename}"
            
            contents = attach.file.read()

        try:
            with open(file_location, 'wb+') as out_file:
                out_file.write(contents)   
            payload.assets = filename
        except Exception:
            return {"message": "There was an error uploading the file"}
        finally:
            attach.file.close()
            
        obj = DB_Stories(**payload.dict())
        db.add(obj)
        db.commit()
                
        return generalResponse(message= "successfully created story", data= None)