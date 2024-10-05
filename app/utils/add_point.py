# from app.models.database.attorney.db_attorney_points import DB_Attorney_Points
# from app.models.database.customer.db_customer_points import DB_Customer_Points

# from app.models.database.customer.db_customer_user import DB_Customer_Users
# from app.models.database.attorney.db_attorney_user import DB_Attorney_Users
# from sqlalchemy.orm import Session

# def add_points_to_referer(referral_code: str, new_attorney_or_customer_id: int, db: Session):
#     if not referral_code:
#         return
    
#     referrer = find_referrer(referral_code, db)
#     if not referrer:
#         return
    
#     if isinstance(referrer, DB_Attorney_Users):
#         add_attorney_points(referrer.id, new_attorney_or_customer_id, db)
#     elif isinstance(referrer, DB_Customer_Users):
#         add_customer_points(referrer.id, new_attorney_or_customer_id, db)
        
# def find_referrer(referral_code: str, db: Session):
#     attorney_referrer = db.query(DB_Attorney_Users).filter(DB_Attorney_Users.invitation_code == referral_code).first()
#     if attorney_referrer:
#         return attorney_referrer

#     customer_referrer = db.query(DB_Customer_Users).filter(DB_Customer_Users.invitation_code == referral_code).first()
#     return customer_referrer

# def add_attorney_points(attorney_id: int, invited_attorney_id: int, db: Session):
#     new_point_entry = DB_Attorney_Points(
#         attorney_id=attorney_id, 
#         invited_attorney_id=invited_attorney_id, 
#         point=1, 
#         reason="Registration"
#     )
#     db.add(new_point_entry)
#     db.commit()

# def add_customer_points(customer_id: int, invited_attorney_id: int, db: Session):
#     new_point_entry = DB_Customer_Points(
#         user_customer_id=customer_id, 
#         invited_attorney_id=invited_attorney_id, 
#         point=1, 
#         reason="Registration"
#     )
#     db.add(new_point_entry)
#     db.commit()