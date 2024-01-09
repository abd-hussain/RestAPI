from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, String, text, Boolean
from app.utils.database import Base

class DB_Majors(Base):
    __tablename__ = "majors"

    id = Column(Integer, primary_key=True, nullable=False, index=True, autoincrement=True)
    name_english = Column(String)
    name_arabic = Column(String)
    categories_id = Column(Integer, ForeignKey(
        "categories.id", ondelete="CASCADE"))
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text("timezone('utc', now())"))
