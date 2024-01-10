from app.models.database.client.db_client_user import DB_Client_Users
from app.models.database.mentor.db_mentor_points import DB_Mentor_Points
from app.models.database.client.db_client_points import DB_Client_Points

from app.models.database.client.db_client_user import DB_Client_Users
from app.models.database.mentor.db_mentor_user import DB_Mentor_Users
from sqlalchemy.orm import Session

def add_points_to_referer(referral_code: str, new_mentor_client_id: int, db: Session):
    if not referral_code:
        return
    
    referrer = find_referrer(referral_code, db)
    if not referrer:
        return
    
    if isinstance(referrer, DB_Mentor_Users):
        add_mentor_points(referrer.id, new_mentor_client_id, db)
    elif isinstance(referrer, DB_Client_Users):
        add_client_points(referrer.id, new_mentor_client_id, db)
        
def find_referrer(referral_code: str, db: Session):
    mentor_referrer = db.query(DB_Mentor_Users).filter(DB_Mentor_Users.invitation_code == referral_code).first()
    if mentor_referrer:
        return mentor_referrer

    client_referrer = db.query(DB_Client_Users).filter(DB_Client_Users.invitation_code == referral_code).first()
    return client_referrer

def add_mentor_points(mentor_id: int, invited_mentor_id: int, db: Session):
    new_point_entry = DB_Mentor_Points(
        mentor_id=mentor_id, 
        invited_mentor_id=invited_mentor_id, 
        point=1, 
        reason="Registration"
    )
    db.add(new_point_entry)
    db.commit()


def add_client_points(client_id: int, invited_mentor_id: int, db: Session):
    new_point_entry = DB_Client_Points(
        client_id=client_id, 
        invited_mentor_id=invited_mentor_id, 
        point=1, 
        reason="Registration"
    )
    db.add(new_point_entry)
    db.commit()