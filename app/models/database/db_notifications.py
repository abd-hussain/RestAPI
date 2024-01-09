from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, String, text, Boolean
from app.utils.database import Base

class DB_Notifications(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, nullable=False, index=True, autoincrement=True)
    title_english = Column(String)
    title_arabic = Column(String)
    content_english = Column(String)
    content_arabic = Column(String)
    readed = Column(Boolean, server_default='FALSE')
    client_owner_id = Column(Integer, ForeignKey(
        "client-users.id", ondelete="CASCADE"))
    mentor_owner_id = Column(Integer, ForeignKey(
        "mentor-users.id", ondelete="CASCADE"))
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text("timezone('utc', now())"))