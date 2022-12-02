from fastapi import Request, Depends, APIRouter
from sqlalchemy.orm import Session
from app.utils.validation import validateLanguageHeader
from app.utils.database import get_db
from app.models.database.db_client_banners import DB_Client_Banners
from app.models.database.db_stories import DB_Stories
from app.models.respond.general import generalResponse



router = APIRouter(
    prefix="/home",
    tags=["Home"]
)

@router.get("/")
async def get_home(request: Request, db: Session = Depends(get_db)):
    myHeader = validateLanguageHeader(request)
    
    main_banner = db.query(DB_Client_Banners.image, DB_Client_Banners.action_type).filter(DB_Client_Banners.language == myHeader.language).filter(DB_Client_Banners.published == True).all()
    main_story = db.query(DB_Stories.assets1, DB_Stories.assets2, DB_Stories.assets3, DB_Stories.owner_id).filter(DB_Stories.language == myHeader.language).filter(DB_Stories.published == True).all()
    
    respose = {"banners" : main_banner, "stories" : main_story}
    print(main_banner)
    return generalResponse(message="home return successfully", data=respose)

