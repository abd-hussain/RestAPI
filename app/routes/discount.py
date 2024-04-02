from app.models.respond.general import generalResponse
from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter
from app.utils.database import get_db
from app.models.database.db_discount_type import DB_DiscountType

router = APIRouter(
    prefix="/discount",
    tags=["Discount"]
)

@router.get("/")
async def verify_discount(code: str, db: Session = Depends(get_db)):
   
    discountQuery = db.query(DB_DiscountType.id, DB_DiscountType.code, DB_DiscountType.percent_value).filter(DB_DiscountType.code == code).first()
    
    if not discountQuery:
         return generalResponse(message= "discount value not exsist", data= None)
    else:
        return generalResponse(message= "successfully return percent value", data= discountQuery)

