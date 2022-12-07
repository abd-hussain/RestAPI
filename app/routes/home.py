from fastapi import Request, Depends, status ,APIRouter, HTTPException
from sqlalchemy.orm import Session
from app.utils.validation import validateLanguageHeader
from app.utils.database import get_db
from app.models.database.db_client_banners import DB_Client_Banners
from app.models.database.mentor.db_mentor_user import DB_Stories, DB_StoryReports
from app.models.respond.general import generalResponse
from app.models.schemas.home import HomeResponse
from app.utils.oauth2 import get_current_user

router = APIRouter(
    prefix="/home",
    tags=["Home"]
)

@router.get("/")
async def get_home(request: Request, db: Session = Depends(get_db)):
    myHeader = validateLanguageHeader(request)
    
    main_banner = db.query(DB_Client_Banners).filter(DB_Client_Banners.language == myHeader.language).filter(DB_Client_Banners.published == True).all()
    main_story = db.query(DB_Stories).filter(DB_Stories.language == myHeader.language).filter(DB_Stories.published == True).all()
       
    respose = HomeResponse(main_banner = main_banner, main_story = main_story) 
    return generalResponse(message="home return successfully", data=respose)


@router.post("/reportstory")
async def reportStory(storyId: int, db: Session = Depends(get_db), get_current_user: int = Depends(get_current_user)):
   
   
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
    return generalResponse(message= "successfully report this story", data= None)