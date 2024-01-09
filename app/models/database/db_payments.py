from sqlalchemy import TIMESTAMP, Column, Integer, ForeignKey, String, DECIMAL, text, Enum
from app.utils.database import Base
import enum 

class PaymentStatus(enum.Enum):
    pending = 1
    approved = 2


class DB_Mentor_Payments(Base):
    __tablename__ = "mentor_payments"

    id = Column(Integer, primary_key=True, nullable=False, index=True, autoincrement=True)
    mentor_id = Column(Integer, ForeignKey("mentor-users.id", ondelete="CASCADE"))
    appointment_id = Column(Integer, ForeignKey("appointments.id", ondelete="CASCADE"))
    status = Column(Enum(PaymentStatus), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text("timezone('utc', now())"))
    
class DB_Mentor_PaymentsـReports(Base):
    __tablename__ = "mentor_payments_reports"
    id = Column(Integer, primary_key=True, nullable=False, index=True, autoincrement=True)
    mentor_id = Column(Integer, ForeignKey("mentor-users.id", ondelete="CASCADE"))
    payment_id = Column(Integer, ForeignKey("mentor_payments.id", ondelete="CASCADE"))
    message = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text("timezone('utc', now())"))