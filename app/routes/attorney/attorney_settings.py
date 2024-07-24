from fastapi import Depends ,APIRouter, HTTPException, status
from sqlalchemy.orm import Session
from app.utils.database import get_db
from app.models.database.attorney.db_attorney_review import DB_Attorney_Review
from app.utils.oauth2 import get_current_user
from app.models.respond.general import generalResponse
from app.models.database.customer.db_customer_user import DB_Customer_Users
from app.models.database.db_country import DB_Countries

router = APIRouter(
    prefix="/attorney-settings",
    tags=["Attorney"]
)

@router.get('/review')
def getAttorneyReview(db: Session = Depends(get_db), 
                         current_user: int = Depends(get_current_user)):
    
    query = db.query(DB_Attorney_Review.id, DB_Attorney_Review.customers_id, DB_Attorney_Review.stars, 
                      DB_Attorney_Review.comment, DB_Attorney_Review.attorney_response, 
                      DB_Attorney_Review.created_at,
                      DB_Customer_Users.profile_img, DB_Customer_Users.first_name, DB_Customer_Users.last_name,
                      DB_Customer_Users.country_id, DB_Countries.flag_image
                     ).join(DB_Customer_Users, DB_Customer_Users.id == DB_Attorney_Review.customers_id, isouter=True)\
                         .join(DB_Countries, DB_Countries.id == DB_Customer_Users.country_id, isouter=True).filter(
                         DB_Attorney_Review.attorney_id == current_user.user_id).all()
   
    return generalResponse(message= "All reviews return successfully", data=query)


@router.put('/review-response')
def EditAttorneyReview(id: int, response: str, db: Session = Depends(get_db), 
                         current_user: int = Depends(get_current_user)):
    

    review = db.query(DB_Attorney_Review).filter(DB_Attorney_Review.id == id, DB_Attorney_Review.attorney_id == current_user.user_id).first()
    
    if review is None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Review Not Exsist")
    
    review.attorney_response = response
    db.commit()
   
    return generalResponse(message= "Review updated successfully", data=None)

#############################################################################################


