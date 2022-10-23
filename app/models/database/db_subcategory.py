
from sqlalchemy import TIMESTAMP, Boolean, Column, ForeignKey, Integer, String, text
from app.utils.database import Base

class DB_Subcategories(Base):
    __tablename__ = "subcategories"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    category_id = Column(Integer, ForeignKey(
        "categories.id", ondelete="CASCADE"), nullable=False)
    name_arabic = Column(String, nullable=False)
    name_english = Column(String, nullable=False)
    description_arabic = Column(String)
    description_english = Column(String)
    icon = Column(String, nullable=False)
    published = Column(Boolean, server_default='TRUE')
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))