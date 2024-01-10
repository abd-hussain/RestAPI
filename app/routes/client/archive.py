from app.models.respond.general import generalResponse
from sqlalchemy.orm import Session
from fastapi import Request, Depends, APIRouter
from app.utils.database import get_db
from app.models.database.db_archive import DB_Archive
from app.models.database.mentor.db_mentor_user import DB_Mentor_Users
from app.utils.validation import validateLanguageHeader
from app.utils.oauth2 import get_current_user
from app.models.database.db_category import DB_Categories

router = APIRouter(
    prefix="/archive",
    tags=["Archive"]
)

# //TODO

@router.get("/")
async def get_client_archives(request: Request, db: Session = Depends(get_db), get_current_user: int = Depends(get_current_user)):
    myHeader = validateLanguageHeader(request)
    query = db.query(DB_Archive.id, DB_Archive.client_id, 
                     DB_Archive.mentor_id, DB_Archive.appointment_type, 
                     DB_Archive.date_from, DB_Archive.date_to,
                     DB_Archive.price_before_discount, DB_Archive.price_after_discount,
                     DB_Archive.note_from_client, DB_Archive.note_from_mentor,
                     DB_Archive.attachment,
                     DB_Mentor_Users.profile_img, DB_Mentor_Users.suffixe_name, DB_Mentor_Users.first_name, DB_Mentor_Users.last_name, 
                     DB_Mentor_Users.category_id, DB_Categories.name_english.label("categoryName"), 
                     ).join(DB_Mentor_Users, DB_Mentor_Users.id == DB_Archive.mentor_id, isouter=True
                     ).join(DB_Categories, DB_Categories.id == DB_Mentor_Users.category_id, isouter=True
                     ).filter(DB_Archive.client_id == get_current_user.user_id).all()

    return generalResponse(message="Archives return successfully", data=query)
