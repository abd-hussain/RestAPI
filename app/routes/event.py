from fastapi import Request, Depends, APIRouter, HTTPException, status
from sqlalchemy.orm import Session
from app.utils.database import get_db
from app.utils.validation import validateLanguageHeader
from app.models.database.db_event import DB_Events, EventState
from datetime import datetime
from app.models.respond.general import generalResponse


router = APIRouter(
    prefix="/event",
    tags=["Event"]
)

@router.get("/")
async def get_event_details(id :int ,request: Request, db: Session = Depends(get_db)):
    myHeader = validateLanguageHeader(request)
    query = db.query(DB_Events).filter(DB_Events.id == id).first()
        
    if query is  None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail={"message": f"event id not valid"})

    return generalResponse(message="Event return successfully", data=query)