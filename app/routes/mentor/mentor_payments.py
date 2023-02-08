from fastapi import Request, Depends, status ,APIRouter, HTTPException
from app.utils.database import get_db
from sqlalchemy.orm import Session
from app.utils.validation import validateLanguageHeader
from app.models.respond.general import generalResponse
from app.utils.oauth2 import get_current_user
from app.models.database.db_payments import DB_Mentor_Payments, DB_Mentor_PaymentsـReports
from app.models.schemas.payment import Payment

router = APIRouter(
    prefix="/mentor-payments",
    tags=["Mentor-Payments"]
)


@router.get("/")
async def get_mentor_payments(request: Request, db: Session = Depends(get_db), get_current_user: int = Depends(get_current_user)):
    myHeader = validateLanguageHeader(request)
    
    query = db.query(DB_Mentor_Payments, DB_Mentor_PaymentsـReports.message.label("report_message")).join(DB_Mentor_PaymentsـReports, DB_Mentor_PaymentsـReports.payment_id == DB_Mentor_Payments.id, isouter=True).filter(DB_Mentor_Payments.mentor_id == get_current_user.user_id).all()
        
    return generalResponse(message="List of Working Hours", data= query)


@router.post("/report", status_code=status.HTTP_201_CREATED)
async def mentor_report_payment(payload: Payment, request: Request, db: Session = Depends(get_db), get_current_user: int = Depends(get_current_user)):
    myHeader = validateLanguageHeader(request)
    query = db.query(DB_Mentor_PaymentsـReports).filter(DB_Mentor_PaymentsـReports.payment_id == payload.payment_id)

    if query.first() is not None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail={"message": f"payment already reported"})
    
    payload.mentor_id =  get_current_user.user_id
    
    obj = DB_Mentor_PaymentsـReports(**payload.dict())

    db.add(obj)
    db.commit()
    
    return generalResponse(message="payment reported successfuly", data=None)