from pydantic import BaseModel
from app.models.database.db_messages import SendedFrom
from typing import Optional


class Message(BaseModel):
    message_id: int
    message : str
    sendit: Optional[SendedFrom] 