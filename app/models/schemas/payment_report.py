from pydantic import BaseModel
from typing import Optional
from app.models.database.db_payments import PaymentStatus
class Payment(BaseModel):
    mentor_id: int
    appointment_id: int
    status : PaymentStatus 
    
class PaymentReport(BaseModel):
    payment_id: int
    message : str
    mentor_id: Optional[int] 