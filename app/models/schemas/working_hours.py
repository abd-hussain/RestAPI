from pydantic import BaseModel

class WorkingHoursRequest(BaseModel) :
    dayName: str
    # working_hours: list[int]
