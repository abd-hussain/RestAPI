from fastapi import Request, Depends, status ,APIRouter, HTTPException
from sqlalchemy.orm import Session
from app.utils.validation import validateLanguageHeader
from app.utils.database import get_db
from app.models.database.db_client_banners import DB_Client_Banners
from app.models.database.db_story import DB_Stories, DB_StoryReports
from app.models.database.db_event import DB_Events, EventState, DB_EventReports, DB_Events_Appointments
from app.models.database.db_tips import DB_Tips, DB_TipsQuestions
from app.models.respond.general import generalResponse
from app.models.schemas.home import HomeResponse, Story, Event
from app.utils.oauth2 import get_current_user
from sqlalchemy import func
from datetime import datetime

router = APIRouter(
    prefix="/home",
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
    main_story = db.query(DB_Stories).filter(DB_Stories.language == myHeader.language).filter(DB_Stories.published == True).all()
    
    main_tips = db.query(DB_Tips.id, DB_Tips.category_id, DB_Tips.title_english.label("title"), DB_Tips.desc_english.label("desc"), 
                         DB_Tips.note_english.label("note"), DB_Tips.referance_english.label("referance"),  
                         DB_Tips.image, func.count(DB_TipsQuestions.tips_id).label("steps")).join(
        DB_TipsQuestions, DB_TipsQuestions.tips_id == DB_Tips.id, isouter=True).group_by(DB_Tips.id).all()
   
    if (myHeader.language == "ar"):
        main_tips = db.query(DB_Tips.id, DB_Tips.category_id, DB_Tips.title_arabic.label("title"), DB_Tips.desc_arabic.label("desc"), 
                         DB_Tips.note_arabic.label("note"), DB_Tips.referance_arabic.label("referance"),  
                         DB_Tips.image, func.count(DB_TipsQuestions.tips_id).label("steps")).join(
        DB_TipsQuestions, DB_TipsQuestions.tips_id == DB_Tips.id, isouter=True).group_by(DB_Tips.id).all()
                         

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

        
    respose = HomeResponse(main_banner = main_banner, main_story = main_story, main_tips = main_tips, main_event = listOfEvent) 
    return generalResponse(message="home return successfully", data=respose)


@router.post("/reportstory")
async def reportStory(storyId: int, request: Request,  db: Session = Depends(get_db), get_current_user: int = Depends(get_current_user)):
    myHeader = validateLanguageHeader(request)
   
    story = db.query(DB_Stories).filter(DB_Stories.id == storyId).first()
    
    if not story:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Story with id: {storyId} does not exist")
        
    report_story_query = db.query(DB_StoryReports).filter(
        DB_StoryReports.story_id == storyId, DB_StoryReports.user_id == get_current_user.user_id)
    
    alreadyReport = report_story_query.first()

    if alreadyReport:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                detail=f"user {get_current_user.user_id} has alredy report this story")
    
    obj = DB_StoryReports(**{"user_id" : get_current_user.user_id, "story_id" : storyId})
    db.add(obj)
    db.commit()
    
    story_query = db.query(DB_Stories).filter(DB_Stories.language == myHeader.language).filter(DB_Stories.published == True).all()
    report_query = db.query(DB_StoryReports).filter(DB_Stories.language == myHeader.language).filter(DB_Stories.published == True).all()
    
    newList : list[Story] = []

    for report in report_query:
        for story in story_query:
            if story.id != report.story_id:
                newList.append(Story(id = story.id, assets = story.assets))

    return generalResponse(message= "successfully report this story", data= newList)


@router.post("/reportevent")
async def reportStory(eventId: int, request: Request,  db: Session = Depends(get_db), get_current_user: int = Depends(get_current_user)):
    myHeader = validateLanguageHeader(request)
   
    event = db.query(DB_Events).filter(DB_Events.id == eventId).first()
    
    if not event:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Event with id: {eventId} does not exist")
        
    report_event_query = db.query(DB_EventReports).filter(
        DB_EventReports.event_id == eventId, DB_EventReports.user_id == get_current_user.user_id)
    
    alreadyReport = report_event_query.first()

    if alreadyReport:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                detail=f"user {get_current_user.user_id} has alredy report this event")
    
    obj = DB_EventReports(**{"user_id" : get_current_user.user_id, "event_id" : eventId})
    db.add(obj)
    db.commit()
    
    events_query = db.query(DB_Events).filter(DB_Events.state == EventState.active).filter(DB_Stories.published == True).all()
    report_query = db.query(DB_EventReports).filter(DB_EventReports.user_id == get_current_user.user_id).all()
    
    newList : list[Event] = []
    
    for report in report_query:
        for event in events_query:
            if event.id != report.event_id:
                event_appointment_query = db.query(DB_Events_Appointments).filter(DB_Events_Appointments.event_id == event.id).all()
                count = 0
                for _ in event_appointment_query:
                    count = count + 1

                newList.append(Event(id = event.id, title = event.title, image = event.image, 
                                     description = event.description, joining_clients = count, 
                                     max_number_of_attendance = event.max_number_of_attendance, 
                                     date_from = event.date_from, date_to = event.date_to, 
                                     price = event.price, state = event.state))

    return generalResponse(message= "successfully report this event", data= newList)