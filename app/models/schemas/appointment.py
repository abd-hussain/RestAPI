from pydantic import BaseModel
from typing import Optional
from app.models.database.db_appointment import AppointmentsType


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
    dateFrom : AppointmentFromTo
    dateTo: AppointmentFromTo
    note: Optional[str]
    discount_id: Optional[int]
    is_free: bool
    currency_english: str
    currency_arabic: str
    mentor_hour_rate: float
    price: float
    discounted_price: float

