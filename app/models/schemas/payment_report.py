from pydantic import BaseModel
from typing import Optional

class PaymentReport(BaseModel):
    payment_id: int
    message : str
    mentor_id: Optional[int] 