from sqlalchemy import TIMESTAMP, Column, Integer, String, Boolean, text, Enum
from app.utils.database import Base
import enum

class AccessLevel(enum.Enum):
    full_access = 1
    read_access = 2
    part_access = 3

class DB_Admin_Users(Base):
    __tablename__ = "admin"

    id = Column(Integer, primary_key=True, nullable=False, index=True, autoincrement=True)
    fullname = Column(String, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, unique=True)
    access_level = Column(Enum(AccessLevel))
    published = Column(Boolean, server_default='FALSE') 
    last_usage = Column(TIMESTAMP(timezone=True))
    api_key = Column(String, nullable=False, unique=True)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text("timezone('utc', now())"))
    
    
