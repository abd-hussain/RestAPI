
from fastapi import Request, Depends, APIRouter
from sqlalchemy.orm import Session
from app.utils.oauth2 import get_current_user
from app.utils.database import get_db
from app.utils.validation import validateLanguageHeader
from app.models.respond.general import generalResponse
from app.models.database.client.db_client_user import DB_Client_Users
from app.models.database.db_add_loyality_request import DB_AddLoyalityRequest, LoyalityRequestState
from app.models.schemas.loyality import Loyality

router = APIRouter(
    prefix="/loyality",
    tags=["loyality"]
)

@router.get("/")
async def get_account(request: Request, db: Session = Depends(get_db), get_current_user: int = Depends(get_current_user)):
    myHeader = validateLanguageHeader(request)
    query = db.query(DB_Client_Users.id, DB_Client_Users.points,).filter(DB_Client_Users.id == get_current_user.user_id)

    if query.first() == None:
       return generalResponse(message="profile was not found", data=None)

    return generalResponse(message="Profile point return successfully", data=query.first())

@router.post("/")
async def requestToAddPointInLoyality(payload: Loyality, request: Request, db: Session = Depends(get_db), get_current_user: int = Depends(get_current_user)):
    myHeader = validateLanguageHeader(request)
        
    obj = DB_AddLoyalityRequest(**{"client_id" : get_current_user.user_id, 
                                     "request_title" : payload.request_title, 
                                     "number_of_point_requested" : payload.number_of_point_requested, 
                                     "state" : LoyalityRequestState.active})
        
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return generalResponse(message="request added successfuly", data=None)
