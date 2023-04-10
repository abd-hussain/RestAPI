
from app.utils.database import Base
from sqlalchemy import TIMESTAMP, Column, Integer, String, Boolean, text

class DB_Countries(Base):
    __tablename__ = "countries"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    flag_image = Column(String, nullable=False)
    name_arabic = Column(String, nullable=False)
    name_english = Column(String, nullable=False)
    currency_arabic = Column(String, nullable=False)
    currency_english = Column(String, nullable=False)
    dialCode = Column(String, nullable=False)
    minLength = Column(Integer, nullable=False)
    maxLength = Column(Integer, nullable=False)
    published = Column(Boolean, server_default='TRUE')
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))