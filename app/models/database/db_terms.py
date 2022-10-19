
from app.utils.database.database import Base
from sqlalchemy import TIMESTAMP, Column, Integer, String, text

class DB_Terms(Base):
    __tablename__ = "terms"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    title_arabic = Column(String, nullable=False)
    title_english = Column(String, nullable=False)
    content_arabic = Column(String, nullable=False)
    content_english = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))