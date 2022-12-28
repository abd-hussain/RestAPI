from pydantic import BaseModel


class AppointmentRequest(BaseModel):
    mentorId: int
    dateYear : int
    dateMonth: int
    dateDay : int
    dateHour : int
    dateMin : int
    class Config:
        orm_mode = True