from fastapi import Request, Depends, APIRouter, HTTPException, status
from sqlalchemy.orm import Session
from app.utils.database import get_db
from app.utils.validation import validateLanguageHeader
from app.models.database.db_event import DB_Events
from app.models.respond.general import generalResponse
from app.models.database.mentor.db_mentor_user import DB_Mentor_Users
from app.models.database.db_category import DB_Categories


router = APIRouter(
    prefix="/event",
    tags=["Event"]
)

@router.get("/")
async def get_event_details(id :int ,request: Request, db: Session = Depends(get_db)):
    myHeader = validateLanguageHeader(request)
    if myHeader.language == "en" :
        query = db.query(DB_Events.image, DB_Events.owner_id, DB_Events.description, DB_Mentor_Users.id, 
                     DB_Mentor_Users.suffixe_name, DB_Mentor_Users.first_name, DB_Mentor_Users.last_name, 
                     DB_Events.max_number_of_attendance, DB_Events.date_to, DB_Events.state, 
                     DB_Events.title, DB_Events.joining_clients_ids, DB_Events.date_from, 
                     DB_Events.price, DB_Mentor_Users.profile_img,DB_Mentor_Users.category_id,
                     DB_Categories.name_english.label("category_name")
                     ).join(DB_Categories, DB_Categories.id == DB_Mentor_Users.category_id, isouter=True).filter(DB_Events.id == id).first()
    else:
        query = db.query(DB_Events.image, DB_Events.owner_id, DB_Events.description, DB_Mentor_Users.id, 
                     DB_Mentor_Users.suffixe_name, DB_Mentor_Users.first_name, DB_Mentor_Users.last_name, 
                     DB_Events.max_number_of_attendance, DB_Events.date_to, DB_Events.state, 
                     DB_Events.title, DB_Events.joining_clients_ids, DB_Events.date_from, 
                     DB_Events.price, DB_Mentor_Users.profile_img,DB_Mentor_Users.category_id,
                     DB_Categories.name_arabic.label("category_name")
                     ).join(DB_Categories, DB_Categories.id == DB_Mentor_Users.category_id, isouter=True).filter(DB_Events.id == id).first()
    if query is  None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail={"message": f"event id not valid"})

    return generalResponse(message="Event return successfully", data=query)