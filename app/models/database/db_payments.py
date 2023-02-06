from sqlalchemy import TIMESTAMP, Column, Integer, ForeignKey, String, DECIMAL, text, Enum
from app.utils.database import Base
import enum 

class PaymentStatus(enum.Enum):
    pending = 1
    approved = 2
    rejected = 3
    
class TransactionType(enum.Enum):
    debit = 1
    credit = 2

class DB_Mentor_Payments(Base):
    __tablename__ = "mentor_payments"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    mentor_id = Column(Integer, ForeignKey(
        "mentor-users.id", ondelete="CASCADE"))
    status = Column(Enum(PaymentStatus), nullable=False)
    amount = Column(DECIMAL, nullable=False)
    durations = Column(Integer, nullable=False)
    currency_arabic = Column(String, nullable=False)
    currency_english = Column(String, nullable=False)
    descriptions = Column(String, nullable=False)
    notes = Column(String)
    type = Column(Enum(TransactionType), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    
class DB_Mentor_PaymentsـReports(Base):
    __tablename__ = "mentor_payments_reports"
    id = Column(Integer, primary_key=True, nullable=False, index=True)
    mentor_id = Column(Integer, ForeignKey("mentor-users.id", ondelete="CASCADE"))
    payment_id = Column(Integer, ForeignKey("mentor_payments.id", ondelete="CASCADE"))
    message = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))