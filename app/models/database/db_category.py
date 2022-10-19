
from app.utils.database.database import Base
from sqlalchemy import TIMESTAMP, Column, Integer, String, Boolean, text


class DB_Categories(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    name_arabic = Column(String, nullable=False)
    name_english = Column(String, nullable=False)
    description_arabic = Column(String)
    description_english = Column(String)
    published = Column(Boolean, server_default='TRUE')
    icon = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))