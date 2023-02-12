from sqlalchemy import TIMESTAMP, Column, Integer, String, Numeric, Boolean, text, Enum
from app.utils.database import Base
import enum


class Platform(enum.Enum):
    client = 1
    mentor = 2
    
class DB_Versions(Base):
    __tablename__ = "versions"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    version = Column(Numeric, nullable=False)
    content_arabic = Column(String, nullable=False)
    content_english = Column(String, nullable=False)
    is_forced = Column(Boolean, server_default='FALSE')
    platform = Column(Enum(Platform), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))