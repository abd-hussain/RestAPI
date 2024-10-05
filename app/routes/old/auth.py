# from fastapi import APIRouter, Depends, status, HTTPException
# from sqlalchemy.orm import Session
# from app.models.database.attorney.db_attorney_user import DB_Attorney_Users
# from app.models.database.customer.db_customer_user import DB_Customer_Users
# from app.models.schemas.attorney_account import AuthData
# from app.utils.database import get_db
# from app.models.respond.general import generalResponse
# from app.utils.oauth2 import create_access_token, verifyPassword
# from app.utils.generate import generateAPIKey
# from datetime import datetime

# router = APIRouter(
#     prefix="/auth",
#     tags=["Auth"]
# )

# @router.post('/')
# def login(payload: AuthData, db: Session = Depends(get_db)):
    
#     attorney_user = db.query(DB_Attorney_Users).filter(DB_Attorney_Users.email == payload.email)
#     customer_user = db.query(DB_Customer_Users).filter(DB_Customer_Users.email == payload.email)
    
#     if not attorney_user.first() and not customer_user.first():
#         raise HTTPException(
#             status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")
        
#     if attorney_user.first():
#         if not verifyPassword(payload.password, attorney_user.first().password):
#             raise HTTPException(
#                 status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Attorney Password")
#         else:
#             if attorney_user.first().published == False:
#                 raise HTTPException(
#                     status_code=status.HTTP_403_FORBIDDEN, detail="Attorney Under Review")
#             if attorney_user.first().blocked == True:
#                 raise HTTPException(
#                     status_code=status.HTTP_403_FORBIDDEN, detail="Attorney Blocked")
                
#             access_token = create_access_token(data={"api_key" : generateAPIKey(), "user_id" : attorney_user.first().id})
#             attorney_user.last_usage = datetime.utcnow()
#             db.commit()
#             return generalResponse(message="Attorney Logged In successfully", data={"Bearer": access_token, "user" : "attorney"})

#     if customer_user.first():
#         if not verifyPassword(payload.password, customer_user.first().password):
#             raise HTTPException(
#                 status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Customer Password")
#         else:
#             if customer_user.first().blocked == True:
#                 raise HTTPException(
#                     status_code=status.HTTP_403_FORBIDDEN, detail="customer Blocked")
                
#             access_token = create_access_token(data={"api_key" : generateAPIKey(), "user_id" : customer_user.first().id})
#             customer_user.last_usage = datetime.utcnow()
#             db.commit()
#             return generalResponse(message="customer Logged In successfully", data={"Bearer": access_token, "user" : "customer"})
