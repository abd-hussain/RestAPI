
from fastapi import Request, Depends, APIRouter, Form
from sqlalchemy.orm import Session
from app.utils.oauth2 import get_current_user
from app.utils.database import get_db
from app.utils.validation import validateLanguageHeader
from app.models.database.db_loyality_rules import DB_Loyality
from app.models.respond.general import generalResponse
from app.models.database.client.db_client_user import DB_Client_Users

router = APIRouter(
    prefix="/loyality",
    tags=["loyality"]
)

@router.get("/rules")
async def get_loyality_rules(request: Request, db: Session = Depends(get_db), get_current_user: int = Depends(get_current_user)):
    myHeader = validateLanguageHeader(request)
    
    data = db.query(DB_Loyality.id, DB_Loyality.content_english.label(
        "content"), DB_Loyality.points, DB_Loyality.action, DB_Loyality.created_at).all()
    if (myHeader.language == "ar"):
        data = db.query(DB_Loyality.id, DB_Loyality.content_arabic.label(
            "content"), DB_Loyality.points, DB_Loyality.action, DB_Loyality.created_at).all()
    return generalResponse(message="list of Loyality Rules return successfully", data=data)

@router.put("/")
async def update_account_point(request: Request, points: int = Form(None),
                         db: Session = Depends(get_db), get_current_user: int = Depends(get_current_user)):
    myHeader = validateLanguageHeader(request)
    query = db.query(DB_Client_Users).filter(DB_Client_Users.id == get_current_user.user_id)

    currentPoint = query.first().points
    
    if points != None:
        query.update({"points" :currentPoint + points}, synchronize_session=False)
        
    db.commit()
    
    return generalResponse(message="Profile updated successfully", data=query.first())