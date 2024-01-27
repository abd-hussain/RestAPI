from app.models.respond.general import generalResponse
from sqlalchemy.orm import Session
from fastapi import Request, Depends, APIRouter
from app.utils.database import get_db
from app.models.database.db_archive import DB_Archive
from app.models.database.mentor.db_mentor_user import DB_Mentor_Users
from app.utils.validation import validateLanguageHeader
from app.utils.oauth2 import get_current_user
from app.models.database.db_category import DB_Categories
from app.models.database.db_country import DB_Countries
from app.models.database.db_appointment import DB_Appointments

router = APIRouter(
    prefix="/archive",
    tags=["Archive"]
)

@router.get("/")
async def get_client_archives(request: Request, db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
    myHeader = validateLanguageHeader(request)

    category_column = DB_Categories.name_arabic if myHeader.language == "ar" else DB_Categories.name_english
    country_column = DB_Countries.name_arabic if myHeader.language == "ar" else DB_Countries.name_english
    currency_column = DB_Appointments.currency_arabic if myHeader.language == "ar" else DB_Appointments.currency_english

    query = db.query(DB_Archive.id, 
                     DB_Archive.client_id, 
                     DB_Archive.mentor_id, 
                     DB_Archive.appointment_id, 
                     DB_Archive.attachment,
                        DB_Mentor_Users.profile_img, 
                        DB_Mentor_Users.suffixe_name, 
                        DB_Mentor_Users.first_name, 
                        DB_Mentor_Users.last_name,
                        DB_Mentor_Users.gender,
                        country_column.label("countryName"), 
                        category_column.label("categoryName"),
                        DB_Appointments.appointment_type,
                        DB_Appointments.date_from,
                        DB_Appointments.date_to,
                        DB_Appointments.state,
                        DB_Appointments.discount_id,
                        DB_Appointments.is_free,
                        DB_Appointments.price,
                        DB_Appointments.total_price,
                        DB_Appointments.payment_type,
                        currency_column.label("currency"),
                        DB_Appointments.mentor_hour_rate,
                        DB_Appointments.note_from_client,
                        DB_Appointments.note_from_mentor,
                        DB_Appointments.mentor_join_call,
                        DB_Appointments.client_join_call,
                        DB_Appointments.mentor_date_of_close,
                        DB_Appointments.client_date_of_close,
                    ).join(DB_Mentor_Users, DB_Mentor_Users.id == DB_Archive.mentor_id, isouter=True
                    ).join(DB_Countries, DB_Countries.id == DB_Mentor_Users.country_id, isouter=True
                    ).join(DB_Categories, DB_Categories.id == DB_Mentor_Users.category_id, isouter=True
                    ).join(DB_Appointments, DB_Appointments.id == DB_Archive.appointment_id, isouter=True
                    ).filter(DB_Archive.client_id == current_user.user_id).all()

    return generalResponse(message="Archives return successfully", data=query)
