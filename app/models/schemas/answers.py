from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, EmailStr


class AnswerModel(BaseModel):
    question_id: int
    question : str
    answer: str
    point: int
    client_owner_id: Optional[int]

class AnswersModel(BaseModel):
    list: List[AnswerModel]
