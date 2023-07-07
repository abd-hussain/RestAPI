from fastapi import Request, Depends ,APIRouter
from sqlalchemy.orm import Session
from app.utils.validation import validateLanguageHeader
from app.utils.database import get_db
from app.models.database.db_mentor_banners import DB_Mentor_Banners
from app.models.respond.general import generalResponse
from app.models.schemas.home import HomeResponse

router = APIRouter(
    prefix="/mentor-home",
    tags=["Home"]
)

@router.get("/")
async def get_home(request: Request, db: Session = Depends(get_db)):
    myHeader = validateLanguageHeader(request)
    
    main_banner = db.query(DB_Mentor_Banners).filter(DB_Mentor_Banners.language == myHeader.language).filter(DB_Mentor_Banners.published == True).all()

    respose = HomeResponse(main_banner = main_banner) 
    return generalResponse(message="home return successfully", data=respose)
