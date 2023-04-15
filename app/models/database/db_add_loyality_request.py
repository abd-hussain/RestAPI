from app.utils.database import Base
from sqlalchemy import TIMESTAMP, ForeignKey, Column, Integer, String, text, Enum
import enum

class LoyalityRequestState(enum.Enum):
    active = 1
    approved = 2
    rejected = 3
    
class DB_AddLoyalityRequest(Base):
    __tablename__ = "add_loyality_request"

    id = Column(Integer, primary_key=True, nullable=False, index=True, autoincrement=True)
    client_id = Column(Integer, ForeignKey(
        "client-users.id", ondelete="CASCADE"), primary_key=True)
    request_title = Column(String, nullable=True)
    state = Column(Enum(LoyalityRequestState), nullable=False)
    number_of_point_requested = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))