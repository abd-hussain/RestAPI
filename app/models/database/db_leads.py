from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, String, text
from app.utils.database import Base

class DB_Leads(Base):
    __tablename__ = "leads"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    full_name = Column(String)
    mobile_number = Column(String)
    email = Column(String)
    client_owner_id = Column(Integer, ForeignKey(
        "client-users.id", ondelete="CASCADE"))
    mentor_owner_id = Column(Integer, ForeignKey(
        "mentor-users.id", ondelete="CASCADE"))
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))