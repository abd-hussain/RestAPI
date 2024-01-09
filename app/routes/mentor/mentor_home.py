from fastapi import Request, Depends ,APIRouter
from sqlalchemy.orm import Session
from app.utils.validation import validateLanguageHeader
from app.utils.database import get_db
from app.models.database.mentor.db_mentor_banners import DB_Mentor_Banners
from app.models.respond.general import generalResponse

router = APIRouter(
    prefix="/mentor-home",
    tags=["Home"]
)

@router.get("/")
async def get_home(request: Request, db: Session = Depends(get_db)):
    language = validateLanguageHeader(request).language
    
    main_banners = db.query(DB_Mentor_Banners.image, DB_Mentor_Banners.action_type
                           ).filter_by(language=language, published=True
                                ).all()

    return generalResponse(message="Home returned successfully", data=main_banners)
