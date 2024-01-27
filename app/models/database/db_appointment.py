from app.utils.database import Base
from sqlalchemy import DECIMAL, TIMESTAMP, ForeignKey, Column, Integer, String, DateTime, text, Enum, Boolean
import enum

class AppointmentsState(enum.Enum):
    active = 1
    mentor_cancel = 2
    client_cancel = 3
    client_miss = 4
    mentor_miss = 5
    completed = 6
    
class AppointmentsType(enum.Enum):
    schudule = 1
    instant = 2
    
class PaymentMethod(enum.Enum):
    apple = 1
    google = 2
    paypal = 3
    free = 4
    
class DB_Appointments(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, nullable=False, index=True, autoincrement=True)
    mentor_id = Column(Integer, ForeignKey(
        "mentor-users.id", ondelete="CASCADE"))
    client_id = Column(Integer, ForeignKey(
        "client-users.id", ondelete="CASCADE"))
    appointment_type = Column(Enum(AppointmentsType), nullable=False)
    date_from = Column(DateTime, nullable=False)
    date_to = Column(DateTime, nullable=False)
    state = Column(Enum(AppointmentsState), nullable=False)
    discount_id = Column(Integer, ForeignKey(
        "discount.id", ondelete="CASCADE"))
    is_free = Column(Boolean, server_default='FALSE', nullable=True)
    price = Column(DECIMAL, nullable=False)
    discounted_price = Column(DECIMAL, nullable=False)
    currency_english = Column(String, nullable=False)
    currency_arabic = Column(String, nullable=False)
    mentor_hour_rate = Column(DECIMAL, nullable=False)
    note_from_client = Column(String, nullable=True)
    note_from_mentor = Column(String, nullable=True)
    mentor_join_call = Column(DateTime, nullable=True)
    client_join_call = Column(DateTime, nullable=True)
    mentor_date_of_close = Column(DateTime, nullable=True)
    client_date_of_close = Column(DateTime, nullable=True)
    channel_id = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text("timezone('utc', now())"))