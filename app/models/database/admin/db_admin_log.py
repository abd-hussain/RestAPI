from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, text, Enum
from app.utils.database import Base
import enum

class LogEvents(enum.Enum):
    login = 1
    logout = 2
    edit_attorney_point = 3
    edit_attorney_review = 4

    
class DB_Admin_Users(Base):
    __tablename__ = "admin_log"

    id = Column(Integer, primary_key=True, nullable=False, index=True, autoincrement=True)
    admin_id = Column(Integer, ForeignKey(
        "admin.id", ondelete="CASCADE"), primary_key=True)
    event = Column(Enum(LogEvents))
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text("timezone('utc', now())"))
    
    
