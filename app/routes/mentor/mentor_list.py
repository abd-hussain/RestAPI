
from fastapi import APIRouter, Depends, status, HTTPException, Request
from sqlalchemy.orm import Session
from app.utils.database import get_db
from app.utils.validation import validateLanguageHeader
from app.models.respond.general import generalResponse
from app.models.database.mentor.db_mentor_user import DB_Mentor_Users


router = APIRouter(
    prefix="/mentor-list",
    tags=["Mentor"]
)


@router.get("/")
async def get_accounts(categories_id :int ,request: Request, db: Session = Depends(get_db)):
    myHeader = validateLanguageHeader(request)
    query = db.query(DB_Mentor_Users).filter(DB_Mentor_Users.category_id == categories_id).all()

    if query == []:
       return generalResponse(message="No Mentors Founded", data=None)

    return generalResponse(message="Mentors return successfully", data=query)