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
    attorney_id: int
    type: AppointmentsType
    payment: PaymentMethod
    is_free: bool
    date_from : AppointmentFromTo
    date_to: AppointmentFromTo
    note: Optional[str]
    discount_id: Optional[int]
    country_id: int
    attorney_hour_rate: float
    price: float
    total_price: float

