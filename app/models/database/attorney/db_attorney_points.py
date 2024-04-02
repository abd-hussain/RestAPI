from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, String, text
from app.utils.database import Base

class DB_Attorney_Points(Base):
    __tablename__ = "attorney_points"
    id = Column(Integer, primary_key=True, nullable=False, index=True, autoincrement=True)
    attorney_id = Column(Integer, ForeignKey(
        "attorney.id", ondelete="CASCADE"), primary_key=True)
    invited_customers_id = Column(Integer, ForeignKey(
        "customers.id", ondelete="CASCADE"))
    invited_attorney_id = Column(Integer, ForeignKey(
        "attorney.id", ondelete="CASCADE"))
    point = Column(Integer, server_default=text('1'))
    reason = Column(String)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text("timezone('utc', now())"))