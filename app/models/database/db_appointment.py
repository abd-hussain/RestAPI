from app.utils.database import Base
from sqlalchemy import DECIMAL, TIMESTAMP, ForeignKey, Column, Integer, DateTime, text
    
class DB_Mentors_Reservations(Base):
    __tablename__ = "mentors_appointment"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    mentor_id = Column(Integer, ForeignKey(
        "mentor-users.id", ondelete="CASCADE"), primary_key=True)
    client_id = Column(Integer, ForeignKey(
        "client-users.id", ondelete="CASCADE"), primary_key=True)
    date_from = Column(DateTime, nullable=False)
    date_to = Column(DateTime, nullable=False)
    price_before_discount = Column(DECIMAL, nullable=False, server_default=text('10.0'))
    discount_id = Column(Integer, ForeignKey(
        "discount.id", ondelete="CASCADE"))
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))