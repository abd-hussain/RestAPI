from fastapi import Request, Depends ,APIRouter
from sqlalchemy.orm import Session
from app.utils.validation import validateLanguageHeader
from app.utils.database import get_db
from app.models.database.mentor.db_mentor_user import DB_Mentor_Users
from app.utils.oauth2 import get_current_user
from app.utils.validation import validateLanguageHeader
from app.models.respond.general import generalResponse

router = APIRouter(
    prefix="/mentor-account",
    tags=["Account"]
)


@router.delete("/delete")
async def delete_account(request: Request, db: Session = Depends(get_db), get_current_user: int = Depends(get_current_user)):
    myHeader = validateLanguageHeader(request)
    query = db.query(DB_Mentor_Users).filter(DB_Mentor_Users.id == get_current_user.user_id)

    if query.first() == None:
       return generalResponse(message="profile was not found", data=None)
   
    query.delete()
    db.commit()
    return generalResponse(message="Profile deleted successfully", data=None)