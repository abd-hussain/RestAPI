from sqlalchemy import ARRAY, TIMESTAMP, Column, ForeignKey, Integer, String, DECIMAL, Boolean, text
from app.utils.database import Base

class DB_Mentor_Users(Base):
    __tablename__ = "mentor-users"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    category_id = Column(Integer, ForeignKey(
        "categories.id", ondelete="CASCADE"), nullable=False)
    suffixe_name = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    bio = Column(String, nullable=False)
    speaking_language = Column(ARRAY(String), nullable=False)
    majors = Column(ARRAY(Integer), nullable=False)
    hour_rate_by_JD = Column(DECIMAL, nullable=False, server_default=text('10.0'))
    mobile_number = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    email = Column(String, unique=True)
    gender = Column(Integer)
    blocked = Column(Boolean, server_default='FALSE') 
    referal_code = Column(String)
    invitation_code = Column(String)
    profile_img = Column(String)
    app_version = Column(String, nullable=False)
    date_of_birth = Column(String)
    last_usage = Column(String)
    last_otp = Column(String)
    working_hours_saturday = Column(ARRAY(Integer))
    working_hours_sunday = Column(ARRAY(Integer))
    working_hours_monday = Column(ARRAY(Integer))
    working_hours_tuesday = Column(ARRAY(Integer))
    working_hours_wednesday = Column(ARRAY(Integer))
    working_hours_thursday = Column(ARRAY(Integer))
    working_hours_friday = Column(ARRAY(Integer))
    api_key = Column(String, nullable=False, unique=True)
    country_id = Column(Integer, ForeignKey(
        "countries.id", ondelete="CASCADE"), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    
    
class DB_Mentor_Review(Base):
    __tablename__ = "mentor_review"
    id = Column(Integer, primary_key=True, nullable=False, index=True)
    mentor_id = Column(Integer, ForeignKey(
        "mentor-users.id", ondelete="CASCADE"), primary_key=True)
    client_id = Column(Integer, ForeignKey(
        "client-users.id", ondelete="CASCADE"), primary_key=True)
    stars = Column(DECIMAL, nullable=False, server_default=text('5.0'))
    comment = Column(String)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))