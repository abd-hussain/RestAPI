from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, String, text
from app.utils.database.database import Base

class DB_Notifications(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    title_english = Column(String)
    title_arabic = Column(String)
    content_english = Column(String)
    content_arabic = Column(String)
    receiver_id = Column(Integer, ForeignKey(
        "users.id", ondelete="CASCADE"), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))