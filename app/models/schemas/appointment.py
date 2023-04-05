from pydantic import BaseModel
from typing import Optional


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
    type: str
    priceBeforeDiscount: float
    priceAfterDiscount: float
    dateFrom : AppointmentFromTo
    dateTo: AppointmentFromTo