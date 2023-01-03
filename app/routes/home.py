from fastapi import Request, Depends, status ,APIRouter, HTTPException
from sqlalchemy.orm import Session
from app.utils.validation import validateLanguageHeader
from app.utils.database import get_db
from app.models.database.db_client_banners import DB_Client_Banners
from app.models.database.mentor.db_mentor_user import DB_Stories, DB_StoryReports
from app.models.database.db_event import DB_Events, EventState
from app.models.database.db_tips import DB_Tips, DB_TipsQuestions
from app.models.respond.general import generalResponse
from app.models.schemas.home import HomeResponse, Story
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
    
    main_events = db.query(DB_Events).filter(DB_Events.state == EventState.active).filter(DB_Events.date_from > datetime.now()).all()
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
        
    respose = HomeResponse(main_banner = main_banner, main_story = main_story, main_tips = main_tips, main_event = main_events) 
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