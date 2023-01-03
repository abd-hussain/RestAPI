from app.utils.database import Base
from sqlalchemy import DECIMAL, TIMESTAMP, ForeignKey, Column, Integer, String, DateTime, text, Enum, ARRAY
import enum

class EventState(enum.Enum):
    active = 1
    mentor_cancel = 2
    mentor_miss = 3
    completed = 4

class DB_Events(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    mentor_id = Column(Integer, ForeignKey(
        "mentor-users.id", ondelete="CASCADE"), primary_key=True)
    image = Column(String, nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    joining_clients_ids = Column(ARRAY(Integer))
    max_number_of_attendance = Column(Integer, nullable=False)
    date_from = Column(DateTime, nullable=False)
    date_to = Column(DateTime, nullable=False)
    price = Column(DECIMAL, nullable=False, server_default=text('10.0'))
    state = Column(Enum(EventState), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    
    