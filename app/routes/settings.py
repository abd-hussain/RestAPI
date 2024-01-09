
from fastapi import Depends, APIRouter, status
from sqlalchemy.orm import Session
from app.models.schemas.leads import ListLeads
from app.models.database.db_leads import DB_Leads
from app.models.respond.general import generalResponse
from app.utils.database import get_db

router = APIRouter(
    prefix="/settings",
    tags=["Settings"]
)

@router.post("/leads", status_code=status.HTTP_201_CREATED)
async def upload_leads(payload: ListLeads, db: Session = Depends(get_db)):    
    
    existing_mobile_numbers = db.query(DB_Leads.mobile_number).filter(
        DB_Leads.mobile_number.in_([lead.mobile_number for lead in payload.list])
    ).all()
    
    existing_mobile_numbers_set = {number[0] for number in existing_mobile_numbers}
    new_leads = [DB_Leads(**lead.dict()) for lead in payload.list if lead.mobile_number not in existing_mobile_numbers_set]

    if new_leads:
        db.add_all(new_leads)
        db.commit()
    return generalResponse(message= "successfully created leads", data= None)