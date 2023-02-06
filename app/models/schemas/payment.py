from pydantic import BaseModel
from typing import Optional


class Payment(BaseModel):
    payment_id: int
    message : str
    mentor_id: Optional[int] 