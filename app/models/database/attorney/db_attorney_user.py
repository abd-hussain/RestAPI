from sqlalchemy import ARRAY, TIMESTAMP, Column, ForeignKey, Integer, String, DECIMAL, Boolean, text, Enum
from app.utils.database import Base
import enum

class FreeCallTypes(enum.Enum):
    free_disabled = 1
    free_15_min = 2
    free_30_min = 3
    
class DB_Attorney_Users(Base):
    __tablename__ = "attorney"

    id = Column(Integer, primary_key=True, nullable=False, index=True, autoincrement=True)
    category_id = Column(Integer, ForeignKey(
        "categories.id", ondelete="CASCADE"), nullable=False)
    suffixe_name = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    bio = Column(String, nullable=False)
    speaking_language = Column(ARRAY(String), nullable=False)
    hour_rate = Column(DECIMAL, nullable=False)
    iban = Column(String)
    mobile_number = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    email = Column(String, unique=True)
    gender = Column(Integer)
    blocked = Column(Boolean, server_default='FALSE')     
    published = Column(Boolean, server_default='FALSE') 
    free_call = Column(Enum(FreeCallTypes))
    invitation_code = Column(String)
    profile_img = Column(String)
    id_img = Column(String)
    cv = Column(String)
    cert1 = Column(String)
    cert2 = Column(String)
    cert3 = Column(String)
    app_version = Column(String, nullable=False)
    date_of_birth = Column(String)
    experience_since = Column(String)
    last_usage = Column(TIMESTAMP(timezone=True))
    working_hours_saturday = Column(ARRAY(Integer))
    working_hours_sunday = Column(ARRAY(Integer))
    working_hours_monday = Column(ARRAY(Integer))
    working_hours_tuesday = Column(ARRAY(Integer))
    working_hours_wednesday = Column(ARRAY(Integer))
    working_hours_thursday = Column(ARRAY(Integer))
    working_hours_friday = Column(ARRAY(Integer))
    api_key = Column(String, nullable=False, unique=True)
    push_token = Column(String)
    country_id = Column(Integer, ForeignKey(
        "countries.id", ondelete="CASCADE"), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text("timezone('utc', now())"))
    
    
