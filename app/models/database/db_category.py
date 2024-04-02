
from app.utils.database import Base
from sqlalchemy import TIMESTAMP, Column, Integer, String, Boolean, text


class DB_Categories(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, nullable=False, index=True, autoincrement=True)
    name_arabic = Column(String, nullable=False)
    name_english = Column(String, nullable=False)
    icon = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text("timezone('utc', now())"))