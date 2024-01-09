from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, String, DECIMAL, text
from app.utils.database import Base

class DB_Mentor_Review(Base):
    __tablename__ = "mentor_review"
    id = Column(Integer, primary_key=True, nullable=False, index=True, autoincrement=True)
    mentor_id = Column(Integer, ForeignKey(
        "mentor-users.id", ondelete="CASCADE"), primary_key=True)
    client_id = Column(Integer, ForeignKey(
        "client-users.id", ondelete="CASCADE"), primary_key=True)
    stars = Column(DECIMAL, nullable=False, server_default=text('5.0'))
    comment = Column(String)
    mentor_response = Column(String)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text("timezone('utc', now())"))