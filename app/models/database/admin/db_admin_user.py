from sqlalchemy import TIMESTAMP, Column, Integer, String, Boolean, text
from app.utils.database import Base

class DB_Admin_Users(Base):
    __tablename__ = "admin"

    id = Column(Integer, primary_key=True, nullable=False, index=True, autoincrement=True)
    fullname = Column(String, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, unique=True)
    published = Column(Boolean, server_default='FALSE') 
    profile_img = Column(String)
    last_usage = Column(TIMESTAMP(timezone=True))
    api_key = Column(String, nullable=False, unique=True)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text("timezone('utc', now())"))
    
    
