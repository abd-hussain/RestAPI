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
    priceWithoutDescount: float
    descountId: Optional[int]
    dateFrom : AppointmentFromTo
    dateTo: AppointmentFromTo