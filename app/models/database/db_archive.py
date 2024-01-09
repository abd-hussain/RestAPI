from app.models.database.db_appointment import AppointmentsType
from app.utils.database import Base
from sqlalchemy import DECIMAL, TIMESTAMP, ForeignKey, Column, Integer, String, DateTime, text, Enum

class DB_Archive(Base):
    __tablename__ = "archive"

    id = Column(Integer, primary_key=True, nullable=False, index=True, autoincrement=True)
    mentor_id = Column(Integer, ForeignKey(
        "mentor-users.id", ondelete="CASCADE"), primary_key=True)
    client_id = Column(Integer, ForeignKey(
        "client-users.id", ondelete="CASCADE"), primary_key=True)
    appointment_type = Column(Enum(AppointmentsType), nullable=False)
    date_from = Column(DateTime, nullable=False)
    date_to = Column(DateTime, nullable=False)
    price_before_discount = Column(DECIMAL, nullable=False)
    price_after_discount = Column(DECIMAL, nullable=False)
    note_from_client = Column(String, nullable=True)
    note_from_mentor = Column(String, nullable=True)
    attachment = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text("timezone('utc', now())"))