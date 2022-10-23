
from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, String, Boolean, text
from app.utils.database import Base

class DB_Main_banners(Base):
    __tablename__ = "main_banners"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    country_id = Column(Integer, ForeignKey(
        "countries.id", ondelete="CASCADE"), nullable=False)
    language = Column(String, nullable=False)
    image = Column(String, nullable=False)
    action_type = Column(String, nullable=False)
    published = Column(Boolean, server_default='TRUE')
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    
class DB_Secound_banners(Base):
    __tablename__ = "secound_banners"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    country_id = Column(Integer, ForeignKey(
        "countries.id", ondelete="CASCADE"), nullable=False)
    language = Column(String, nullable=False)
    image = Column(String, nullable=False)
    action_type = Column(String, nullable=False)
    published = Column(Boolean, server_default='TRUE')
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))