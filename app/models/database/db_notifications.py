from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, String, text
from app.utils.database import Base

class DB_Notifications(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, nullable=False, index=True, autoincrement=True)
    title_english = Column(String)
    title_arabic = Column(String)
    content_english = Column(String)
    content_arabic = Column(String)
    customers_owner_id = Column(Integer, ForeignKey(
        "customers.id", ondelete="CASCADE"), nullable=True)
    attorney_owner_id = Column(Integer, ForeignKey(
        "attorney.id", ondelete="CASCADE"), nullable=True)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text("timezone('utc', now())"))