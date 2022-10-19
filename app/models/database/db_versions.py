from sqlalchemy import TIMESTAMP, Column, Integer, String, Numeric, Boolean, text
from app.utils.database.database import Base

class DB_Versions(Base):
    __tablename__ = "versions"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    version = Column(Numeric, nullable=False)
    content_arabic = Column(String, nullable=False)
    content_english = Column(String, nullable=False)
    is_forced = Column(Boolean, server_default='FALSE')
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))