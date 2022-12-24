from sqlalchemy import TIMESTAMP, Column, Integer, String, DECIMAL, text
from app.utils.database import Base

class DB_Discount(Base):
    __tablename__ = "discount"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    code = Column(String, nullable=False)
    percent_value = Column(DECIMAL, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))