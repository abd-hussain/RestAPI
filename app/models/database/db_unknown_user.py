from app.utils.database import Base
from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, String, Boolean, text

class DB_Unknown_Users(Base):
    __tablename__ = "unknown_users"

    id = Column(Integer, primary_key=True, nullable=False, index=True, autoincrement=True)
    api_key = Column(String, nullable=False, unique=True)
    allow_notifications = Column(Boolean, server_default='FALSE')
    blocked = Column(Boolean, server_default='FALSE')
    os_type = Column(String, nullable=False)
    os_version = Column(String, nullable=False)
    device_name = Column(String, nullable=False)
    app_version = Column(String, nullable=False)
    language = Column(String, nullable=False)
    push_token = Column(String)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text("timezone('utc', now())"))