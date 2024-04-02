from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, String, text
from app.utils.database import Base

class DB_Leads(Base):
    __tablename__ = "leads"

    id = Column(Integer, primary_key=True, nullable=False, index=True, autoincrement=True)
    full_name = Column(String)
    mobile_number = Column(String)
    email = Column(String)
    customers_owner_id = Column(Integer, ForeignKey(
        "customers.id", ondelete="CASCADE"))
    attorney_owner_id = Column(Integer, ForeignKey(
        "attorney.id", ondelete="CASCADE"))
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text("timezone('utc', now())"))