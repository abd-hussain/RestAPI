from sqlalchemy import TIMESTAMP, Column, Integer, String, text
from app.utils.database import Base

class DB_Loyality(Base):
    __tablename__ = "loyality"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    content_english = Column(String)
    content_arabic = Column(String)
    action = Column(String, nullable=False)
    points = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))