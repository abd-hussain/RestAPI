from typing import List
from pydantic import BaseModel

class WorkingHoursRequest(BaseModel) :
    working_hours_saturday: List[int]
    working_hours_sunday: List[int]
    working_hours_monday: List[int]
    working_hours_tuesday: List[int]
    working_hours_wednesday: List[int]
    working_hours_thursday: List[int]
    working_hours_friday: List[int]
