from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, String, Numeric, Boolean, text
from app.utils.database.database import Base

class DB_Leads(Base):
    __tablename__ = "leads"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    full_name = Column(String)
    mobile_number = Column(String)
    email = Column(String)
    owner_id = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))