from app.utils.database import Base
from sqlalchemy import TIMESTAMP, ForeignKey, Column, Integer,String, Boolean, DateTime, text

class DB_Mentors_WorkingHours(Base):
    __tablename__ = "appointment_hours"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    
    
    
# class DB_Mentors_Reservations(Base):
#     __tablename__ = "appointment_duration"

#     id = Column(Integer, primary_key=True, nullable=False, index=True)
#     mentor_id = Column(Integer, ForeignKey(
#         "mentor-users.id", ondelete="CASCADE"), primary_key=True)
#     date = Column(DateTime, nullable=False)
#     time = Column(DateTime, nullable=False)
#     created_at = Column(TIMESTAMP(timezone=True),
#                         nullable=False, server_default=text('now()'))