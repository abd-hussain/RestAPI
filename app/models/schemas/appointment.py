from pydantic import BaseModel
from typing import Optional
from app.models.database.db_appointment import AppointmentsType, PaymentMethod


class AppointmentFromTo(BaseModel):
    year : int
    month: int
    day : int
    hour : int
    min : int
    class Config:
        orm_mode = True
        
        
class AppointmentRequest(BaseModel):
    mentorId: int
    type: AppointmentsType
    payment: PaymentMethod
    is_free: bool
    dateFrom : AppointmentFromTo
    dateTo: AppointmentFromTo
    note: Optional[str]
    discount_id: Optional[int]
    currency_id: int
    mentor_hour_rate: float
    price: float
    total_price: float

