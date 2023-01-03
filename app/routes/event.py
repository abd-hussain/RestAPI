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
async def get_all_events(request: Request, db: Session = Depends(get_db)):
    myHeader = validateLanguageHeader(request)
    query = db.query(DB_Events).filter(DB_Events.state == EventState.active).filter(DB_Events.date_from > datetime.now()).all()
    return generalResponse(message="list of appointments return successfully", data=query)