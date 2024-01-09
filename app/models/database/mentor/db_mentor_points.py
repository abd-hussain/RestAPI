from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, String, text
from app.utils.database import Base

class DB_Mentor_Points(Base):
    __tablename__ = "mentor_points"
    id = Column(Integer, primary_key=True, nullable=False, index=True, autoincrement=True)
    mentor_id = Column(Integer, ForeignKey(
        "mentor-users.id", ondelete="CASCADE"), primary_key=True)
    invited_client_id = Column(Integer, ForeignKey(
        "client-users.id", ondelete="CASCADE"))
    invited_mentor_id = Column(Integer, ForeignKey(
        "mentor-users.id", ondelete="CASCADE"))
    point = Column(Integer, server_default=text('1'))
    reason = Column(String)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text("timezone('utc', now())"))