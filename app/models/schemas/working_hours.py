from typing import List
from pydantic import BaseModel

class WorkingHoursRequest(BaseModel) :
    dayName: str
    working_hours: List[int]
