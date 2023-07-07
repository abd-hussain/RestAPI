from fastapi import Request, Depends ,APIRouter
from sqlalchemy.orm import Session
from app.utils.validation import validateLanguageHeader
from app.utils.database import get_db
from app.models.database.db_client_banners import DB_Client_Banners
from app.models.respond.general import generalResponse
from app.models.schemas.home import HomeResponse
from sqlalchemy import func
from datetime import datetime

router = APIRouter(
    prefix="/client-home",
    tags=["Home"]
)

@router.get("/")
async def get_home(request: Request, db: Session = Depends(get_db)):
    myHeader = validateLanguageHeader(request)
    
    main_banner = db.query(DB_Client_Banners).filter(DB_Client_Banners.language == myHeader.language).filter(DB_Client_Banners.published == True).all()
        
    respose = HomeResponse(main_banner = main_banner) 
    return generalResponse(message="home return successfully", data=respose)
