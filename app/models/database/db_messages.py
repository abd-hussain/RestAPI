
from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, String, text, Enum
from app.utils.database import Base
import enum 

class SendedFrom(enum.Enum):
    mentor = 1
    client = 2
    
class DB_Messages(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    client_id = Column(Integer, ForeignKey(
        "client-users.id", ondelete="CASCADE"))
    mentor_id = Column(Integer, ForeignKey(
        "mentor-users.id", ondelete="CASCADE"))
    sendit = Column(Enum(SendedFrom), nullable=False)
    message = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))