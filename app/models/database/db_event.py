from app.utils.database import Base
from sqlalchemy import  TIMESTAMP, ForeignKey, Column, Integer, String, text, Boolean, ARRAY, DateTime, Enum, DECIMAL
import enum 
from sqlalchemy.orm import relationship

class EventState(enum.Enum):
    active = 1
    mentor_cancel = 2
    mentor_miss = 3
    completed = 4

class DB_Events(Base):
    __tablename__ = "event"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    owner_id = Column(Integer, ForeignKey(
        "mentor-users.id", ondelete="CASCADE"), nullable=False)
    image = Column(String, nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    max_number_of_attendance = Column(Integer, nullable=False)
    date_from = Column(DateTime, nullable=False)
    date_to = Column(DateTime, nullable=False)
    price = Column(DECIMAL, nullable=False, server_default=text('10.0'))
    state = Column(Enum(EventState), nullable=False)
    published = Column(Boolean, server_default='TRUE')
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))    
    owner = relationship("DB_Mentor_Users")
    
    
class DB_Events_Appointments(Base):
    __tablename__ = "event_appointments"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    client_id = Column(Integer, ForeignKey(
        "client-users.id", ondelete="CASCADE"), primary_key=True)
    event_id = Column(Integer, ForeignKey("event.id", ondelete="CASCADE"), primary_key=True)
    
class DB_EventReports(Base):
    __tablename__ = "event_reports"
    id = Column(Integer, primary_key=True, nullable=False, index=True)
    user_id = Column(Integer, ForeignKey("client-users.id", ondelete="CASCADE"))
    mentor_id = Column(Integer, ForeignKey("mentor-users.id", ondelete="CASCADE"))
    event_id = Column(Integer, ForeignKey("event.id", ondelete="CASCADE"))
    
    
    